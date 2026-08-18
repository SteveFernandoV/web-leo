#!/usr/bin/env python3
"""
Script de busqueda y generacion de sistemas de diseno para UIUX Designer.
Permite buscar estilos, paletas, fuentes y directrices tecnicas por stack.
"""

import argparse
import sys
import json

DESIGN_STYLES = {
    "dark-futurist": {
        "name": "Dark Futurist / Cyber Minimal",
        "description": "Fondo espacial oscuro (#030014), resplandores neon focalizados (#A855F7, #3B82F6), micro-estrellas y arcos de luz.",
        "best_for": ["ai", "crypto", "devtools", "startups"],
        "palette": {
            "background": "#030014",
            "surface": "#0C0728",
            "primary": "#A855F7",
            "secondary": "#3B82F6",
            "text": "#FFFFFF",
            "muted": "#94A3B8"
        },
        "typography": {"heading": "Outfit", "body": "Inter"}
    },
    "bento-grid": {
        "name": "Bento Grid Modern",
        "description": "Tarjetas asimetricas redondeadas con sutiles bordes translúcidos y sombras suaves.",
        "best_for": ["saas", "dashboard", "features", "analytics"],
        "palette": {
            "background": "#090A0F",
            "surface": "#12141F",
            "primary": "#6366F1",
            "secondary": "#EC4899",
            "text": "#F8FAFC",
            "muted": "#64748B"
        },
        "typography": {"heading": "Plus Jakarta Sans", "body": "Inter"}
    },
    "clean-saas": {
        "name": "Clean Corporate SaaS",
        "description": "Fondos claros minimalistas, azul real de alta confianza y acentos esmeralda.",
        "best_for": ["b2b", "fintech", "enterprise", "healthcare"],
        "palette": {
            "background": "#F8FAFC",
            "surface": "#FFFFFF",
            "primary": "#2563EB",
            "secondary": "#10B981",
            "text": "#0F172A",
            "muted": "#64748B"
        },
        "typography": {"heading": "Inter", "body": "Inter"}
    },
    "neobrutalism": {
        "name": "Neobrutalism High Contrast",
        "description": "Bordes negros de 2-3px, sombras duras sin blur (4px 4px 0px #000) y colores pastel vibrantes.",
        "best_for": ["creative", "ecommerce", "gen-z", "marketing"],
        "palette": {
            "background": "#FEF08A",
            "surface": "#FFFFFF",
            "primary": "#FF6B6B",
            "secondary": "#4ECDC4",
            "text": "#000000",
            "muted": "#333333"
        },
        "typography": {"heading": "Space Grotesk", "body": "DM Sans"}
    }
}

STACK_GUIDELINES = {
    "html-tailwind": {
        "recommendations": [
            "Usa clases semánticas de Tailwind como text-balance en títulos y text-pretty en párrafos.",
            "Aplica transition-all duration-200 ease-out en todos los botones y enlaces interactivos.",
            "Para fondos oscuros usa bg-[#030014] o bg-slate-950 con border-white/10.",
            "Usa backdrop-blur-xl en navbars y modales flotantes."
        ]
    },
    "nextjs": {
        "recommendations": [
            "Optimiza tipografías usando next/font/google para cero Cumulative Layout Shift (CLS).",
            "Usa componentes de servidor (RSC) por defecto y agrega 'use client' solo en islas interactivas.",
            "Usa next/image con tamaños explícitos o fill con aspect-ratio para optimizar Largest Contentful Paint (LCP)."
        ]
    },
    "react-native": {
        "recommendations": [
            "Usa NativeWind para clases consistentes de Tailwind.",
            "Asegura áreas táctiles mínimas de 44x44 en TouchableOpacity / Pressable.",
            "Usa react-native-reanimated para animaciones a 60fps."
        ]
    },
    "flutter": {
        "recommendations": [
            "Aplica ThemeData con Material 3 habilitado (useMaterial3: true).",
            "Usa GoogleFonts package para cargar fuentes de forma eficiente.",
            "Evita rebuilds innecesarios usando ConsumerWidget de Riverpod."
        ]
    }
}

def generate_design_system(keywords: str, project_name: str = "Mi Proyecto"):
    kw_lower = keywords.lower()
    selected_key = "dark-futurist"
    for key, data in DESIGN_STYLES.items():
        if any(w in kw_lower for w in data["best_for"]) or key in kw_lower:
            selected_key = key
            break

    style = DESIGN_STYLES[selected_key]
    print("=" * 60)
    print(f"🎨 SISTEMA DE DISEÑO GENERADO: {project_name.upper()}")
    print("=" * 60)
    print(f"• Estilo Visual: {style['name']}")
    print(f"• Descripción:   {style['description']}")
    print(f"• Tipografía:    Headings: {style['typography']['heading']} | Body: {style['typography']['body']}")
    print("\n--- PALETA DE COLORES RECOMENDADA ---")
    for role, color in style["palette"].items():
        print(f"  {role.capitalize():<12}: {color}")
    print("\n--- EJEMPLO DE TOKENS TAILWIND ---")
    print(f"  bg-['{style['palette']['background']}'] text-['{style['palette']['text']}']")
    print(f"  bg-['{style['palette']['primary']}'] shadow-[0_0_25px_{style['palette']['primary']}80]")
    print("=" * 60)

def search_query(keyword: str, domain: str = None, stack: str = None):
    print(f"[*] Resultados de búsqueda para: '{keyword}'")
    if stack and stack in STACK_GUIDELINES:
        print(f"\n--- DIRECTRICES PARA STACK: {stack.upper()} ---")
        for rec in STACK_GUIDELINES[stack]["recommendations"]:
            print(f"  ✓ {rec}")
    else:
        for key, style in DESIGN_STYLES.items():
            if keyword.lower() in key or keyword.lower() in style["name"].lower() or any(keyword.lower() in b for b in style["best_for"]):
                print(f"\n[+] Coincidencia: {style['name']}")
                print(f"    {style['description']}")
                print(f"    Fuentes: {style['typography']['heading']} / {style['typography']['body']}")

def main():
    parser = argparse.ArgumentParser(description="Buscador de diseño y generador de Design Systems")
    parser.add_argument("query", nargs="?", default="", help="Palabras clave de estilo o industria")
    parser.add_argument("--design-system", action="store_true", help="Genera un sistema de diseño completo")
    parser.add_argument("-p", "--project", default="Nuevo Proyecto", help="Nombre del proyecto")
    parser.add_argument("--domain", help="Dominio o industria (saas, fintech, ai, etc.)")
    parser.add_argument("--stack", default="html-tailwind", help="Tecnología frontend (html-tailwind, nextjs, react-native, flutter)")

    args = parser.parse_args()
    if args.design_system:
        generate_design_system(args.query, args.project)
    else:
        search_query(args.query, domain=args.domain, stack=args.stack)

if __name__ == "__main__":
    main()
