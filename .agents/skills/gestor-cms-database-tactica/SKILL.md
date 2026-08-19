---
name: gestor-cms-database-tactica
description: >-
  Sub-agente especialista en Arquitectura de Contenidos (CMS), Gestión de Medios y Base de Datos Local (IndexedDB & LocalStorage).
  Úsalo para crear o modificar módulos en admin.html, gestionar la carga y compresión de fotos/videos, sincronizar cursos y fechas de calendario, estructurar esquemas JSON y mantener la persistencia segura de datos sin límites de cuota.
---

# Gestor CMS & Base de Datos Táctica // Sub-Agente de Gestión de Contenidos

Este sub-agente actúa como **Arquitecto de Datos y Administrador del Centro de Mando**, responsable de la persistencia, compresión, indexación y sincronización en tiempo real de todo el contenido del sitio web.

---

## 1. Arquitectura de Almacenamiento Dual

```text
┌─────────────────────────────────────────────────────────────┐
│                    CENTRO DE MANDO (CMS)                    │
└──────────────┬───────────────────────────────┬──────────────┘
               │                               │
               ▼                               ▼
    ┌──────────────────────┐        ┌──────────────────────┐
    │  IndexedDB (Media)   │        │     LocalStorage     │
    │ HappyTacticalMediaDB │        │  HT_OWNER_CONFIG_V2  │
    │  - Fotos HD (Base64) │        │  - Textos & Títulos  │
    │  - Logos & Portadas  │        │  - Cursos & Fechas   │
    │  - Videos & Enlaces  │        │  - URLs & Metadatos  │
    │  - Sin límite cuota  │        │  - Claves Ligeras    │
    └──────────────────────┘        └──────────────────────┘
               │                               │
               └───────────────┬───────────────┘
                               ▼
            ┌────────────────────────────────────┐
            │ BroadcastChannel: 'happy_tactical' │
            │   - type: 'gallery_updated'        │
            │   - type: 'config_updated'         │
            │   - type: 'video_updated'          │
            └─────────────────┬──────────────────┘
                              ▼
            ┌────────────────────────────────────┐
            │        WEB PRINCIPAL (INDEX)       │
            │  Actualización en vivo sin recarga │
            └────────────────────────────────────┘
```

---

## 2. Esquema de Datos Canónico

### Estructura del Objeto Global `HT_OWNER_CONFIG_V2`
```json
{
  "user": "admin",
  "pin": "7788",
  "whatsApp": "51977331267",
  "whatsAppDisplay": "+51 977 331 267",
  "phone": "+51 977 331 267",
  "email": "contacto@happytactical.com",
  "hudBanner": "SISTEMA OPERATIVO TÁCTICO // CONVOCATORIAS 2026 ABIERTAS",
  "heroBadge": "CERTIFICACIÓN OFICIAL SUCAMEC & MININTER",
  "galleryImages": [
    {
      "id": "gal-1723456789",
      "title": "Prácticas de Tiro Defensivo en Polígono",
      "badge": "POLÍGONO",
      "location": "Lima, Perú • Sede Central",
      "url": "data:image/jpeg;base64,...",
      "desc": "Entrenamiento con munición real y tiro bajo estrés.",
      "createdAt": "19/08/2026"
    }
  ],
  "videos": [
    {
      "id": "vid-1",
      "title": "Demostración de Tiro Táctico y Reacción",
      "badge": "TIRO DEFENSIVO",
      "duration": "04:20",
      "category": "seguridad",
      "videoUrl": "https://www.youtube.com/watch?v=...",
      "thumbnail": "https://img.youtube.com/vi/.../maxresdefault.jpg",
      "desc": "Técnicas de tiro reactivo.",
      "featured": true
    }
  ],
  "schedule": [
    {
      "id": 1723456789,
      "isoDate": "2026-04-25",
      "date": "25 ABR",
      "group": "GRUPO 2026",
      "title": "Curso Integral de Manejo de Armas de Fuego (L10)",
      "details": "Modalidad Presencial Lima • Certificación Oficial",
      "category": "seguridad",
      "status": "open",
      "statusText": "CONVOCATORIA ABIERTA"
    }
  ]
}
```

---

## 3. Protocolo de Guardado y Prevención de Errores

1. **Compresión Automática en Canvas:**
   - Redimensionar imágenes a un máximo de **1400px** con calidad **0.85 JPEG**.
   - Garantizar que cada imagen pese menos de **180 KB**.
2. **Escritura Dual con Captura de Cuota:**
   ```javascript
   // 1. Guardar en IndexedDB
   await saveImageToDB(photoId, base64Data);

   // 2. Guardar en LocalStorage con fallback sanitizado
   try {
     localStorage.setItem(STORAGE_KEY, JSON.stringify(APP_CONFIG));
   } catch (eQuota) {
     const sanitized = JSON.parse(JSON.stringify(APP_CONFIG));
     sanitized.galleryImages.forEach(img => {
       if (img.url && img.url.startsWith('data:') && img.url.length > 500) {
         img.url = 'HappyTacticalMediaDB:' + img.id;
       }
     });
     localStorage.setItem(STORAGE_KEY, JSON.stringify(sanitized));
   }
   ```
3. **Notificación Conforme al Usuario:**
   - Siempre mostrar `alert('✅ ¡GUARDADO CONFORME!...')` para que el usuario tenga certeza visual inmediata de que la base de datos se actualizó.
