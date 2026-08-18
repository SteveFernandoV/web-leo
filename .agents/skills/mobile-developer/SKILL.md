---
name: mobile-developer
description: Use this skill when building React Native or Flutter apps with native integrations. For cross-platform UI, offline-first sync, push notifications, and App Store deployment workflows.
---

# Mobile Developer

Cross-platform mobile development expertise for React Native and Flutter applications.

---

## 1. Documentación de Referencia y Recursos

- 🔄 **[Arquitectura Offline-First y Sincronización](./references/offline_first_sync.md)**: SQLite, MMKV, Isar, colas de mutación y resolución de conflictos.
- 📱 **[Integraciones Nativas y Despliegue](./references/native_integrations_deploy.md)**: Permisos (`Info.plist` y `AndroidManifest`), notificaciones push (FCM/APNs), deep linking y Fastlane.
- 🧱 **[Plantillas de Arquitectura Móvil](./resources/mobile_architecture_templates.md)**: Estructuras *Feature-First* en React Native (Expo Router) y Flutter (Riverpod).

---

## 2. Overview

This skill guides you through building **production-grade mobile apps** that work seamlessly on both iOS and Android. It covers:

- **React Native / Flutter** component architecture
- **Native module integration** for device-specific features
- **Offline-first design** for unreliable network conditions
- **Push notifications & deep linking** for user engagement
- **App Store & Google Play submission** with compliance checks

---

## 3. Protocols

### Protocol 1: Analyze Requirements
- Identify target platforms (iOS only, Android only, or cross-platform).
- List required native device features (Camera, Biometrics/FaceID, Bluetooth, GPS/Location, Storage).
- Determine offline requirements (local caching, mutation queue, background sync).
- Plan push notification strategy (FCM / APNs / OneSignal) and deep linking paths.

### Protocol 2: Set Up Project Structure
- Initialize React Native (Expo SDK Managed / Bare) or Flutter project.
- Configure TypeScript / Dart in strict mode.
- Set up linting, formatting and code quality checks.
- Create feature-based modular directory structure (`app/`, `src/features/` or `lib/features/`).

### Protocol 3: Implement Core Features
- Build reusable, touch-friendly UI components following iOS Human Interface Guidelines and Material Design 3.
- Implement robust navigation flows (Stack, Tabs, Modals, Drawer).
- Add data fetching with smart caching (TanStack Query, Riverpod streams).
- Gracefully handle platform-specific differences (`Platform.OS === 'ios'` or `Platform.isAndroid`).

### Protocol 4: Add Native Integrations
- Configure required runtime permissions in `Info.plist` and `AndroidManifest.xml` with clear user justifications.
- Integrate native SDKs (Camera, SQLite, HealthKit/Google Fit, File System).
- Test thoroughly on physical devices and simulators across multiple screen sizes and orientations.

### Protocol 5: Prepare for Release
- Generate adaptive app icons and native splash screens.
- Configure code signing certificates (Apple Developer Provisioning Profiles & Android Keystores).
- Set up automated CI/CD pipelines with Fastlane / GitHub Actions.
- Create App Store Connect and Google Play Store listings with compliance disclosures.
