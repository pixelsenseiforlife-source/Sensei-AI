"""Construit la scène animée du reel 01 (HTML + SVG piloté par render(t)).
Utilisation : python3 -I reels/animation/build_reel01.py && node reels/animation/render_reel.js 01"""
import json, math, os, re, struct, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); REELS = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(REELS, "brand", "build"))
from art import *

FPS = 30
D = os.path.join(HERE, "01")
timing = json.load(open(os.path.join(D, "timing.json"), encoding="utf-8"))
audio = os.path.join(REELS, "voiceover", "audio", "01-plan-fixe.mp3")

# --- enveloppe de la voix (pour la bouche du Sensei), une valeur par image
raw = subprocess.run(["ffmpeg", "-v", "error", "-i", audio, "-ac", "1", "-ar", "16000", "-f", "s16le", "-"], capture_output=True).stdout
n = len(raw) // 2; s = struct.unpack(f"<{n}h", raw); spf = 16000 // FPS
amp = [math.sqrt(sum(x * x for x in s[i:i + spf]) / spf) / 32768 for i in range(0, n - spf, spf)]
peak = max(amp); amp = [round(a / peak, 3) for a in amp]
duration = n / 16000

# --- mots → sous-titres (la ponctuation seule est rattachée au mot précédent)
words = []
for w in timing["words"]:
    if re.fullmatch(r"[?!:;.,…]+", w["w"]) and words:
        words[-1]["w"] += " " + w["w"] if w["w"] in "?!:;" else w["w"]; continue
    words.append(dict(w))
chunks, cur = [], []
for w in words:
    cur.append(w)
    if len(cur) >= 4 or (re.search(r"[.?!…:,]$", w["w"]) and len(cur) >= 2) or re.search(r"[.?!…]$", w["w"]):
        chunks.append(cur); cur = []
if cur: chunks.append(cur)

def variants(fn, combos, cls):
    return "".join(f'<g class="{cls}" data-k="{p}-{e}" style="display:none">{fn(p, e)}'
                   + (f'<ellipse class="talk" cx="100" cy="140" rx="6.5" ry="0" fill="{MOUTH}"/>' if cls == "sv" else "")
                   + '</g>' for p, e in combos)

sensei_v = variants(sensei, [("stop", "severe"), ("neutre", "serein"), ("enseigne", "malin"), ("camera", "rire")], "sv")
eleve_v = variants(eleve, [("filme", "confiant"), ("filme", "confus"), ("neutre", "confus"), ("neutre", "confiant"),
                           ("neutre", "emerveille"), ("filme", "emerveille")], "ev")
mini_v = variants(eleve, [("neutre", "confiant"), ("filme", "emerveille"), ("neutre", "emerveille")], "mv")

svg_stage = f'''<svg id="stage" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 270 480" width="1080" height="1920">
<defs><clipPath id="vfclip"><rect x="0" y="0" width="230" height="262" rx="6"/></clipPath></defs>
<g id="world">
  <g id="bg">{decor_studio()}</g>
  <g id="sensei" transform="translate(-200 186) scale(.5)">{sensei_v}</g>
  <g id="eleve" transform="translate(128 222) scale(.44)">{eleve_v}</g>
  <g id="tripod" style="display:none"><g transform="translate(-22 -10)">{tripod()}</g>{camera(0, -16, .7)}</g>
  <g id="vf" style="display:none">
    <rect x="-4" y="-4" width="238" height="270" rx="9" fill="{INK}"/>
    <g clip-path="url(#vfclip)">
      <g transform="translate(0 -100) scale(.852)">{decor_rue()}</g>
      <g id="mini" transform="translate(-80 100) scale(.32)">{mini_v}</g>
      <rect width="230" height="262" fill="none" stroke="#000" stroke-opacity=".25" stroke-width="10"/>
    </g>
    <g fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round">
      <path d="M10 28 V10 H28"/><path d="M202 10 H220 V28"/><path d="M10 234 V252 H28"/><path d="M220 234 V252 H202"/></g>
    <g id="rec"><circle cx="22" cy="22" r="4.5" fill="{RED}"/><text x="31" y="26" font-family="Inter" font-weight="800" font-size="11" fill="#fff">REC</text></g>
    <text id="tc" x="208" y="26" text-anchor="end" font-family="JetBrains Mono, monospace" font-size="9" fill="#fff">00:00:00:00</text>
    <rect x="72" y="236" width="86" height="16" rx="3" fill="{GOLD}"/><text x="115" y="248" text-anchor="middle" font-family="Anton, Inter" font-size="11" fill="{INK}">CAMÉRA IMMOBILE</text>
  </g>
  <g id="title"><rect id="tbg" x="20" y="40" width="230" height="44" rx="4" fill="{INK}"/>
    <text id="ttx" x="135" y="72" text-anchor="middle" font-family="Anton, Inter" font-size="26" fill="{GOLD}"></text></g>
  <g id="stamp" style="display:none" transform="translate(135 170)"><g transform="rotate(-8)">
    <rect x="-110" y="-46" width="220" height="92" rx="7" fill="{PAPER}" stroke="{RED}" stroke-width="7"/>
    <text y="-4" text-anchor="middle" font-family="Anton, Inter" font-size="34" fill="{RED}" letter-spacing="1">RÈGLE N°1</text>
    <text y="28" text-anchor="middle" font-family="Anton, Inter" font-size="17" fill="{INK}">PAS DE RAISON = PLAN FIXE</text></g></g>
  <g id="sub" transform="translate(135 388)"><rect id="sbg" x="-100" y="-17" width="200" height="30" rx="5" fill="{INK}" fill-opacity=".88"/>
    <text id="stx" y="4" text-anchor="middle" font-family="Inter" font-weight="800" font-size="12.5" fill="#fff"></text></g>
  <g id="subbtn" style="display:none" transform="translate(135 138)">
    <rect id="btnbg" x="-62" y="-17" width="124" height="34" rx="17" fill="{RED}"/>
    <text id="btntx" y="6" text-anchor="middle" font-family="Inter" font-weight="800" font-size="14" fill="#fff">S'ABONNER</text>
    <g id="cursor" transform="translate(60 40)"><path d="M0 0 L0 22 L6 16 L10 25 L14 23 L10 14 L18 14Z" fill="#fff" stroke="{INK}" stroke-width="1.6" stroke-linejoin="round"/></g>
  </g>
</g></svg>'''

data = {"amp": amp, "fps": FPS, "duration": round(duration, 3),
        "chunks": [{"s": c[0]["s"], "e": c[-1]["e"], "w": [[w["w"], w["s"]] for w in c]} for c in chunks]}
js = open(os.path.join(HERE, "reel01.js"), encoding="utf-8").read()
html = ('<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Anton&display=swap" rel="stylesheet">'
        '<style>html,body{margin:0;background:#000;width:1080px;height:1920px;overflow:hidden}</style></head><body>'
        + svg_stage + f'<script>const DATA={json.dumps(data, ensure_ascii=False)};\n{js}</script></body></html>')
open(os.path.join(D, "scene.html"), "w", encoding="utf-8").write(html)
print(f"scène ok · {len(chunks)} sous-titres · {duration:.2f}s")
