#!/usr/bin/env python3
"""
Motor de Humanizacao de Prompts para AI Studio Image.
Injeta sistematicamente as 5 camadas de realismo fotografico.
"""

import argparse
import sys

MODES = {
    "influencer": (
        "Candid authentic smartphone photo taken on iPhone 15 Pro, "
        "natural ambient window lighting, soft organic shadows, subtle film grain, "
        "shallow depth of field with realistic background bokeh, genuine facial expression, "
        "natural skin texture with visible pores and subtle imperfections, non-studio casual setting."
    ),
    "educacional": (
        "Clean, professional and authentic photo in educational setting, "
        "balanced natural daylight, crisp focus on key elements, clear subject composition, "
        "candid and engaging posture, high clarity without artificial studio glare."
    )
}

HUMANIZATION_LEVELS = {
    "ultra": "Raw unedited mobile camera capture, slight sensor noise, imperfect candid framing, 100% natural candid realism.",
    "natural": "Balanced smartphone photography, realistic lighting, natural skin texture, authentic colors.",
    "polished": "High quality photography with natural aesthetics, clean composition, vibrant yet realistic color grading.",
    "editorial": "Magazine-style lifestyle photography, curated natural lighting, artistic depth of field."
}

TIME_OF_DAY = {
    "morning": "Crisp morning sunlight, soft cool-to-warm tones, gentle light rays.",
    "golden-hour": "Warm golden hour sunset lighting, soft glowing highlights, long delicate shadows.",
    "midday": "Bright natural daylight, defined realistic shadows, clear vibrant colors.",
    "overcast": "Soft diffused overcast daylight, even flattering light distribution, no harsh shadows.",
    "night": "Warm indoor ambient lighting, cozy low-light atmosphere, authentic ISO grain.",
    "indoor": "Soft mixed indoor lighting, gentle bounce light from walls and windows."
}

def humanize_prompt(user_prompt: str, mode: str = "influencer", level: str = "natural", time: str = "golden-hour") -> str:
    base_modifiers = MODES.get(mode, MODES["influencer"])
    level_modifiers = HUMANIZATION_LEVELS.get(level, HUMANIZATION_LEVELS["natural"])
    time_modifiers = TIME_OF_DAY.get(time, TIME_OF_DAY["golden-hour"])
    
    full_prompt = f"{user_prompt}. {base_modifiers} {time_modifiers} {level_modifiers}"
    return full_prompt

def main():
    parser = argparse.ArgumentParser(description="Humanizador de prompts para AI Studio Image")
    parser.add_argument("--prompt", required=True, help="Prompt original do usuario")
    parser.add_argument("--mode", default="influencer", choices=["influencer", "educacional"], help="Modo visual")
    parser.add_argument("--level", default="natural", choices=["ultra", "natural", "polished", "editorial"], help="Nivel de humanizacao")
    parser.add_argument("--time", default="golden-hour", choices=["morning", "golden-hour", "midday", "overcast", "night", "indoor"], help="Hora do dia")
    
    args = parser.parse_args()
    humanized = humanize_prompt(args.prompt, mode=args.mode, level=args.level, time=args.time)
    print(humanized)

if __name__ == "__main__":
    main()
