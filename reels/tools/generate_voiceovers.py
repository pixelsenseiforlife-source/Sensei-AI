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
    ELEVENLABS_MODEL (défaut : eleven_v3 ; sinon eleven_multilingual_v2)
    ELEVENLABS_OUT   (sous-dossier de sortie, défaut : audio)

Avec eleven_v3, le bloc ```voix-off-v3``` du script est utilisé s'il existe : il contient
des indications de jeu entre crochets ([firmly], [whispers]...) et des MAJUSCULES d'insistance.
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
AUDIO = OUT / os.environ.get("ELEVENLABS_OUT", "audio")
BLOCK = re.compile(r"```voix-off\n(.*?)```", re.S)
BLOCK_V3 = re.compile(r"```voix-off-v3\n(.*?)```", re.S)

# Corrections de prononciation : appliquées uniquement au texte envoyé à ElevenLabs.
PRONONCIATION = {
    "tout le temps": "tou le temps",
    "Tout le temps": "Tou le temps",
}


def is_v3() -> bool:
    return os.environ.get("ELEVENLABS_MODEL", "eleven_v3").startswith("eleven_v3")


def for_tts(text: str) -> str:
    for a, b in PRONONCIATION.items():
        text = text.replace(a, b)
    if is_v3():  # v3 ne lit pas les balises <break> : on les remplace par une pause écrite
        text = re.sub(r"\s*<break[^>]*/>\s*", "… ", text)
    return text


def extract(path: Path) -> str:
    content = path.read_text(encoding="utf-8")
    m = (BLOCK_V3.search(content) if is_v3() else None) or BLOCK.search(content)
    if not m:
        raise ValueError(f"Pas de bloc voix-off dans {path.name}")
    return " ".join(line.strip() for line in m.group(1).splitlines() if line.strip())


def synthesize(text: str, dest: Path, key: str, voice: str) -> None:
    body = {
        "text": for_tts(text),
        "model_id": os.environ.get("ELEVENLABS_MODEL", "eleven_v3"),
        "voice_settings": {
            "stability": float(os.environ.get("ELEVENLABS_STABILITY", 0.5 if is_v3() else 0.3)),
            "similarity_boost": float(os.environ.get("ELEVENLABS_SIMILARITY", 0.8)),
            "style": float(os.environ.get("ELEVENLABS_STYLE", 0.0 if is_v3() else 0.45)),
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
