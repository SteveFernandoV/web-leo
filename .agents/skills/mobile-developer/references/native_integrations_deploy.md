# Integraciones Nativas, Permisos y Despliegue en App Store & Google Play

Guía técnica de configuración para acceso a hardware, notificaciones push, enlaces profundos y automatización de publicaciones.

---

## 1. Configuración de Permisos Nativos

### iOS (`ios/Runner/Info.plist` / `app.json` en Expo):
```xml
<!-- Cámara -->
<key>NSCameraUsageDescription</key>
<string>Necesitamos acceso a la cámara para escanear documentos y capturar fotos de perfil.</string>

<!-- Ubicación -->
<key>NSLocationWhenInUseUsageDescription</key>
<string>Requerimos tu ubicación para mostrarte servicios cercanos en tiempo real.</string>

<!-- Galería / Fotos -->
<key>NSPhotoLibraryUsageDescription</key>
<string>Acceso a la galería para adjuntar comprobantes.</string>
```

### Android (`android/app/src/main/AndroidManifest.xml`):
```xml
<uses-permission android:name="android.permission.CAMERA" />
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.POST_NOTIFICATIONS" />
<uses-permission android:name="android.permission.INTERNET" />
```

---

## 2. Notificaciones Push & Deep Linking

- **Push Notifications:**
  - Firebase Cloud Messaging (FCM) para Android.
  - Apple Push Notification service (APNs) con certificado / clave `.p8` para iOS.
  - Gestión de tokens de dispositivo en el login/logout del usuario.
- **Deep Linking / Universal Links:**
  - Configuración de `apple-app-site-association` (AASA) para iOS Universal Links.
  - Configuración de `assetlinks.json` para Android App Links.
  - Enrutamiento interno con Expo Router (`app/profile/[id].tsx`) o `go_router` en Flutter.

---

## 3. Automatización de Publicación con Fastlane

### `Fastfile` (iOS & Android):
```ruby
default_platform(:ios)

platform :ios do
  desc "Construir y subir a TestFlight"
  lane :beta do
    match(type: "appstore")
    build_app(workspace: "App.xcworkspace", scheme: "App")
    upload_to_testflight
  end
end

platform :android do
  desc "Construir App Bundle y subir a Google Play Internal Track"
  lane :beta do
    gradle(task: "bundleRelease")
    upload_to_play_store(track: "internal")
  end
end
```
