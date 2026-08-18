# Recetas de Shaders GLSL para Efectos Visuales Web

Colección de fragmentos y shaders de vértices optimizados para WebGL y React Three Fiber.

---

## 1. Shader de Resplandor Holográfico (Fresnel Glow Shader)

Efecto de resplandor neón en los bordes de objetos 3D.

### Vertex Shader:
```glsl
varying vec3 vNormal;
varying vec3 vPosition;

void main() {
  vNormal = normalize(normalMatrix * normal);
  vPosition = vec3(modelViewMatrix * vec4(position, 1.0));
  gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
}
```

### Fragment Shader:
```glsl
uniform vec3 uColor;
uniform float uPower;
varying vec3 vNormal;
varying vec3 vPosition;

void main() {
  vec3 viewDirection = normalize(-vPosition);
  float fresnel = pow(1.0 - max(0.0, dot(viewDirection, vNormal)), uPower);
  gl_FragColor = vec4(uColor * fresnel, fresnel);
}
```

---

## 2. Onda Sinusoidal de Vértices (Vertex Wave Shader)

Efecto de superficie líquida o malla topográfica animada.

```glsl
uniform float uTime;
uniform float uFrequency;
uniform float uAmplitude;
varying vec2 vUv;

void main() {
  vUv = uv;
  vec3 pos = position;
  pos.z += sin(pos.x * uFrequency + uTime) * cos(pos.y * uFrequency + uTime) * uAmplitude;
  gl_Position = projectionMatrix * modelViewMatrix * vec4(pos, 1.0);
}
```
