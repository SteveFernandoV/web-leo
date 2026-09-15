# Gestión global y segura de fotografías

## Objetivo

Permitir que el propietario cambie las fotografías desde `admin.html` y que el resultado se vea en cualquier navegador o dispositivo, sin volver a desplegar la web por cada cambio de contenido.

## Situación actual

La aplicación combina `localStorage`, IndexedDB y Firestore como fuentes de datos. Las imágenes se convierten a Base64 y se intentan guardar dentro de documentos de Firestore. Esto produce estados distintos entre navegadores, supera con facilidad las cuotas locales y acerca los documentos al límite de tamaño de Firestore. El acceso administrativo también se valida en el cliente y guarda el PIN dentro de datos públicamente legibles.

## Arquitectura aprobada

### Fuente de verdad

- Firebase Storage almacenará los archivos de imagen.
- Firestore almacenará únicamente metadatos: URL pública, ruta del archivo, encuadre, título y fecha de actualización.
- El sitio público leerá primero Firestore y usará las imágenes incluidas en el repositorio solo como respaldo.
- `localStorage` e IndexedDB dejarán de decidir qué fotografía está activa. Podrán conservarse temporalmente solo para migración o caché tolerante a fallos.

### Administración y seguridad

- El panel utilizará Firebase Authentication con correo y contraseña.
- Las reglas permitirán lectura pública de la configuración necesaria para mostrar el sitio.
- Solo un usuario autenticado y autorizado podrá modificar Firestore o subir y eliminar archivos en Storage.
- El PIN y las credenciales administrativas dejarán de almacenarse en el código, `localStorage` y Firestore.
- Las credenciales privadas nunca se incorporarán al repositorio.

### Flujo de actualización

1. El propietario inicia sesión en el Centro de Mando.
2. Selecciona una fotografía y ve una previsualización local.
3. Al guardar, el panel comprime la imagen a un formato web razonable y la sube a Firebase Storage.
4. Cuando la subida termina, actualiza en Firestore la URL y los metadatos del espacio correspondiente.
5. El panel muestra confirmación solo después de que ambos pasos hayan terminado correctamente.
6. Las páginas abiertas reciben el cambio mediante el listener de Firestore; las nuevas visitas descargan el mismo estado global.

## Alcance inicial

Esta fase cubrirá:

- Logo principal.
- Imagen de portada.
- Imagen de la sección institucional.
- Imágenes de los tres cursos.
- Fotografías de la galería.
- Eliminación o restablecimiento de una fotografía.
- Estados visibles de carga, éxito y error.
- Compatibilidad con las fotografías actuales mediante valores de respaldo.

La mejora estética general del sitio queda fuera de esta fase y se abordará después.

## Estructura de datos

Cada espacio fijo tendrá un documento con:

- `url`: dirección de descarga de Firebase Storage.
- `storagePath`: ruta estable del archivo para poder reemplazarlo o eliminarlo.
- `fit`, `position` y `scale`: encuadre visual.
- `updatedAt`: marca de tiempo del servidor.

Cada elemento de galería tendrá identificador, título, categoría, ubicación, descripción, `url`, `storagePath` y `updatedAt`. Ningún documento guardará contenido Base64.

## Manejo de errores

- Si falla la compresión, no se inicia la subida.
- Si falla la subida, no se modifica Firestore ni la imagen visible.
- Si falla la actualización de Firestore después de subir, el panel informa el error y evita presentar el cambio como publicado.
- Si Firebase no está disponible al cargar la web, se muestran las imágenes de respaldo incluidas en el proyecto.
- Los botones de guardado permanecen desactivados durante operaciones en curso para evitar duplicados.

## Migración

- Se conservarán las rutas locales actuales como respaldo.
- Las imágenes Base64 existentes que todavía sean recuperables se subirán una sola vez a Storage.
- Después de verificar las nuevas URL, se eliminarán de los documentos activos los campos Base64 obsoletos.
- No se borrará contenido remoto anterior hasta comprobar que la web pública muestra correctamente las nuevas imágenes.

## Verificación

- Probar subida y reemplazo de cada tipo de imagen.
- Abrir la web en otra sesión o navegador sin datos locales y confirmar que muestra los cambios.
- Recargar con caché limpia y verificar que no reaparecen imágenes antiguas.
- Confirmar que un visitante no autenticado puede leer el sitio, pero no escribir ni subir archivos.
- Revisar funcionamiento móvil del panel de fotografías.
- Publicar primero una versión de prueba en Vercel y promoverla a producción después de validar el flujo completo.

## Despliegue

El repositorio seguirá publicándose en el proyecto Vercel existente. Los cambios de código requerirán un despliegue, pero los cambios posteriores de fotografías se publicarán desde el Centro de Mando sin necesitar un nuevo despliegue de Vercel.
