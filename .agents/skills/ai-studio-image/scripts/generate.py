#!/usr/bin/env python3
"""
Script de geracao de imagens via Google AI Studio / Google GenAI SDK.
"""

import argparse
import os
import sys
from pathlib import Path

def generate_image(prompt: str, mode: str = "influencer", aspect_ratio: str = "1:1", model: str = "imagen-3.0-generate-002", output_dir: str = "outputs"):
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Erro: Variavel de ambiente GEMINI_API_KEY nao configurada.", file=sys.stderr)
        print("Defina com: export GEMINI_API_KEY='sua_chave'", file=sys.stderr)
        sys.exit(1)

    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    
    print(f"[*] Gerando imagem...")
    print(f"    Modelo: {model}")
    print(f"    Modo: {mode}")
    print(f"    Formato: {aspect_ratio}")
    print(f"    Prompt: {prompt[:80]}...")

    try:
        from google import genai
        from google.genai import types

        client = genai.Client(api_key=api_key)
        
        result = client.models.generate_images(
            model=model,
            prompt=prompt,
            config=types.GenerateImagesConfig(
                number_of_images=1,
                aspect_ratio=aspect_ratio,
                person_generation="ALLOW_ADULT",
                safety_filter_level="BLOCK_MEDIUM_AND_ABOVE",
            )
        )

        for i, generated_image in enumerate(result.generated_images):
            file_name = out_path / f"generated_{mode}_{i+1}.png"
            with open(file_name, "wb") as f:
                f.write(generated_image.image.image_bytes)
            print(f"[✓] Imagem salva com sucesso em: {file_name}")

    except ImportError:
        print("[!] SDK 'google-genai' nao encontrado. Instale com: pip install google-genai", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"[!] Erro durante a geracao: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Gerador de imagens com Google AI Studio")
    parser.add_argument("--prompt", required=True, help="Prompt da imagem")
    parser.add_argument("--mode", default="influencer", choices=["influencer", "educacional"], help="Modo visual")
    parser.add_argument("--format", default="square", choices=["square", "portrait", "landscape", "stories"], help="Formato")
    parser.add_argument("--model", default="imagen-3.0-generate-002", help="Modelo a utilizar")
    parser.add_argument("--output", default="outputs", help="Diretorio de saida")

    format_map = {
        "square": "1:1",
        "portrait": "3:4",
        "landscape": "16:9",
        "stories": "9:16"
    }

    args = parser.parse_args()
    ratio = format_map.get(args.format, "1:1")
    generate_image(prompt=args.prompt, mode=args.mode, aspect_ratio=ratio, model=args.model, output_dir=args.output)

if __name__ == "__main__":
    main()
