# Pipeline de Optimización y Rendimiento 3D para la Web

Guía técnica para garantizar 60 FPS estables y tiempos de carga mínimos en experiencias Three.js y React Three Fiber.

---

## 1. Presupuestos de Rendimiento (Performance Budgets)

| Plataforma / Dispositivo | FPS Objetivo | Máx. Triángulos (Polígonos) | Máx. Draw Calls | Tamaño GLB Recomendado |
| :--- | :--- | :--- | :--- | :--- |
| **Desktop de Gama Media/Alta** | 60 FPS | 500,000 | < 100 | < 5 MB |
| **Móviles Modernos (iOS/Android)** | 30 - 60 FPS | 100,000 | < 40 | < 2.5 MB |
| **Móviles de Gama Baja / Tablets** | 30 FPS | 50,000 | < 20 | < 1.5 MB |

---

## 2. Flujo de Optimización con `gltf-transform`

1. **Modelado y Reducción de Mallas (Blender):**
   - Aplicar modificador *Decimate* para reducir conteo de caras.
   - Hornear (*bake*) mapas de normales, rugosidad y oclusión ambiental en un solo canal de texturas (ORM: Occlusion-Roughness-Metallic).
2. **Exportar a formato `.glb` binario.**
3. **Compresión Draco & Texturas KTX2 / WebP:**

```bash
# Instalar herramienta globalmente
npm install -g @gltf-transform/cli

# Pipeline de optimización automatizada
gltf-transform optimize entrada.glb salida_optimizada.glb \
  --compress draco \
  --texture-compress webp \
  --texture-size 1024
```

---

## 3. Estrategias en Código (Quick Wins)

- **InstancedMesh:** Para renderizar cientos de objetos repetidos (partículas, árboles, luces) en una sola llamada de dibujo (*1 draw call*).
- **Control de DPR (Device Pixel Ratio):** Limitar el DPR a `1` en dispositivos móviles (`dpr={[1, 1.5]}`) para evitar sobrecargar la GPU.
- **Nivel de Detalle (LOD):** Cambiar a geometrías simplificadas cuando la cámara se aleja del objeto.
- **Limitación de Luces:** Evitar más de 1-2 luces dinámicas con sombras habilitadas. Preferir mapas de entorno HDR (*Environment maps*) o iluminación pre-horneada.
