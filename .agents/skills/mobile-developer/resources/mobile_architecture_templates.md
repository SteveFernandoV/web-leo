# Plantillas de Arquitectura Móvil: React Native & Flutter

Estructuras de proyectos limpias y modulares para aplicaciones de escala empresarial.

---

## 1. Plantilla React Native / Expo (Feature-First Architecture)

```text
my-mobile-app/
├── app/                       # Expo Router (File-based navigation)
│   ├── _layout.tsx            # Root Layout (Theme, Auth, QueryProvider)
│   ├── (auth)/                # Grupo de rutas de autenticación
│   │   ├── login.tsx
│   │   └── register.tsx
│   ├── (tabs)/                # Navegación principal por pestañas
│   │   ├── _layout.tsx
│   │   ├── index.tsx          # Home Feed
│   │   ├── explore.tsx
│   │   └── profile.tsx
│   └── modal/
├── src/
│   ├── features/              # Módulos por funcionalidad
│   │   ├── auth/              # api, components, hooks, stores
│   │   ├── payments/
│   │   └── products/
│   ├── components/ui/         # Átomos reutilizables (Button, Input, Card)
│   ├── hooks/                 # Hooks globales (useNetwork, usePushNotification)
│   ├── services/              # Cliente HTTP (Axios/Ky), SQLite, MMKV
│   └── types/                 # Interfaces y tipos globales de TypeScript
├── app.json                   # Configuración Expo, Plugins nativos e Iconos
└── package.json
```

---

## 2. Plantilla Flutter (Clean Architecture + Riverpod)

```text
flutter_app/
├── lib/
│   ├── main.dart              # Punto de entrada e inicialización
│   ├── app.dart               # MaterialApp.router y configuración global
│   ├── core/                  # Utilidades compartidas
│   │   ├── network/           # Dio client, Interceptores
│   │   ├── theme/             # AppTheme, Paleta de colores
│   │   └── routing/           # Configuración de go_router
│   └── features/              # Feature-Driven Design
│       └── auth/
│           ├── data/          # Repositorios, Data Sources (Remote/Local)
│           ├── domain/        # Modelos de entidad, Casos de uso
│           └── presentation/  # Pantallas, Widgets y Riverpod Notifiers
├── pubspec.yaml               # Dependencias (flutter_riverpod, go_router, isar)
└── analysis_options.yaml      # Linter estricto de Dart
```
