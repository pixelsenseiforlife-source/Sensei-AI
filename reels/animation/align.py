"""Horodatage mot à mot d'une voix off (API forced-alignment d'ElevenLabs) → animation/NN/timing.json
Utilisation : python3 -I reels/animation/align.py 02 03 ..."""
import glob, json, os, re, sys, urllib.request, uuid
REELS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for rid in sys.argv[1:]:
    script = glob.glob(os.path.join(REELS, "scripts", f"{rid}-*.md"))[0]
    slug = os.path.basename(script)[:-3]
    txt = open(script, encoding="utf-8").read()
    v3 = re.search(r"```voix-off-v3\n(.*?)```", txt, re.S).group(1)
    plain = " ".join(l.strip() for l in re.sub(r"\[[^\]]*\]\s*", "", v3).splitlines() if l.strip())
    audio = open(os.path.join(REELS, "voiceover", "audio", slug + ".mp3"), "rb").read()
    b = uuid.uuid4().hex
    body = (f"--{b}\r\nContent-Disposition: form-data; name=\"text\"\r\n\r\n{plain}\r\n--{b}\r\n"
            f"Content-Disposition: form-data; name=\"file\"; filename=\"a.mp3\"\r\nContent-Type: audio/mpeg\r\n\r\n").encode() + audio + f"\r\n--{b}--\r\n".encode()
    req = urllib.request.Request("https://api.elevenlabs.io/v1/forced-alignment", data=body, method="POST",
                                 headers={"xi-api-key": os.environ.get("ELEVENLABS_API_KEY", "proxy-injected"), "Content-Type": f"multipart/form-data; boundary={b}"})
    d = json.load(urllib.request.urlopen(req, timeout=180))
    words = [{"w": w["text"], "s": round(w["start"], 3), "e": round(w["end"], 3)} for w in d["words"] if w["text"].strip()]
    os.makedirs(os.path.join(REELS, "animation", rid), exist_ok=True)
    json.dump({"text": plain, "words": words}, open(os.path.join(REELS, "animation", rid, "timing.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print(rid, len(words), "mots,", words[-1]["e"], "s")
