#!/usr/bin/env python3
"""Génère les voix off des reels avec ta voix clonée ElevenLabs.

1. Extrait le bloc ```voix-off``` de chaque script de reels/scripts/
   et l'écrit dans reels/voiceover/NN-nom.txt (toujours fait).
2. Si ELEVENLABS_API_KEY et ELEVENLABS_VOICE_ID sont définis, envoie chaque
   texte à ElevenLabs et enregistre reels/voiceover/audio/NN-nom.mp3.

Utilisation :
    python3 reels/tools/generate_voiceovers.py            # tous les reels
    python3 reels/tools/generate_voiceovers.py 01 03      # seulement 01 et 03
    python3 reels/tools/generate_voiceovers.py --force    # régénère les MP3 existants

Variables d'environnement optionnelles :
    ELEVENLABS_MODEL (défaut : eleven_multilingual_v2)
    ELEVENLABS_STABILITY, ELEVENLABS_SIMILARITY, ELEVENLABS_STYLE (0 à 1)
"""
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
OUT = ROOT / "voiceover"
AUDIO = OUT / "audio"
BLOCK = re.compile(r"```voix-off\n(.*?)```", re.S)


def extract(path: Path) -> str:
    m = BLOCK.search(path.read_text(encoding="utf-8"))
    if not m:
        raise ValueError(f"Pas de bloc voix-off dans {path.name}")
    return " ".join(line.strip() for line in m.group(1).splitlines() if line.strip())


def synthesize(text: str, dest: Path, key: str, voice: str) -> None:
    body = {
        "text": text,
        "model_id": os.environ.get("ELEVENLABS_MODEL", "eleven_multilingual_v2"),
        "voice_settings": {
            "stability": float(os.environ.get("ELEVENLABS_STABILITY", 0.5)),
            "similarity_boost": float(os.environ.get("ELEVENLABS_SIMILARITY", 0.8)),
            "style": float(os.environ.get("ELEVENLABS_STYLE", 0.15)),
            "use_speaker_boost": True,
        },
    }
    req = urllib.request.Request(
        f"https://api.elevenlabs.io/v1/text-to-speech/{voice}?output_format=mp3_44100_128",
        data=json.dumps(body).encode(),
        headers={"xi-api-key": key, "Content-Type": "application/json", "Accept": "audio/mpeg"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        dest.write_bytes(resp.read())


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    force = "--force" in sys.argv
    files = sorted(SCRIPTS.glob("*.md"))
    if args:
        files = [f for f in files if f.name[:2] in args]
    key = os.environ.get("ELEVENLABS_API_KEY")
    voice = os.environ.get("ELEVENLABS_VOICE_ID")
    OUT.mkdir(exist_ok=True)
    if key and voice:
        AUDIO.mkdir(exist_ok=True)
    else:
        print("Clé API ou Voice ID absent : seuls les textes sont générés.")

    for f in files:
        text = extract(f)
        (OUT / f"{f.stem}.txt").write_text(text + "\n", encoding="utf-8")
        words = len(re.sub(r"<[^>]+>", "", text).split())
        print(f"{f.stem}: {words} mots (~{words / 2.6:.0f} s)")
        if key and voice:
            dest = AUDIO / f"{f.stem}.mp3"
            if dest.exists() and not force:
                print("  MP3 déjà présent, ignoré (--force pour régénérer)")
                continue
            try:
                synthesize(text, dest, key, voice)
                print(f"  -> {dest.relative_to(ROOT)}")
            except urllib.error.HTTPError as e:
                print(f"  ERREUR {e.code}: {e.read().decode(errors='replace')[:300]}")
                return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
