"""Construit la scène animée d'un reel (02 à 10) à partir du moteur commun.
Utilisation : python3 -I reels/animation/build_reel.py 02 [03 ...] puis node reels/animation/render_reel.js 02"""
import glob, json, math, os, re, struct, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); REELS = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(REELS, "brand", "build")); sys.path.insert(0, HERE)
from art import *
from demos import DEMOS, EXTRAS
FPS = 30

CTA_SVG = f'''
<g class="cv" data-k="subscribe"><rect id="btnbg" x="-62" y="-17" width="124" height="34" rx="17" fill="{RED}"/>
  <text id="btntx" y="6" text-anchor="middle" font-family="Inter" font-weight="800" font-size="14" fill="#fff">S'ABONNER</text>
  <g id="cursor"><path d="M0 0 L0 22 L6 16 L10 25 L14 23 L10 14 L18 14Z" fill="#fff" stroke="{INK}" stroke-width="1.6" stroke-linejoin="round"/></g></g>
<g class="cv" data-k="chips"><rect x="-104" y="-22" width="208" height="30" rx="15" fill="{INK}"/>
  <path d="M-88 -14 h16 a3 3 0 0 1 3 3 v8 a3 3 0 0 1 -3 3 h-9 l-5 4 v-4 h-2 a3 3 0 0 1 -3 -3 v-8 a3 3 0 0 1 3 -3z" fill="{GOLD}"/>
  <text id="cqtx" x="8" y="-2" text-anchor="middle" font-family="Inter" font-weight="800" font-size="10.5" fill="#fff"></text>
  <g id="chip1"><rect x="-44" y="-1" width="88" height="26" rx="13" fill="{RED}"/><text id="c1tx" y="17" text-anchor="middle" font-family="Anton, Inter" font-size="14" fill="#fff"></text></g>
  <g id="chip2"><rect x="-44" y="-1" width="88" height="26" rx="13" fill="{GOLD}"/><text id="c2tx" y="17" text-anchor="middle" font-family="Anton, Inter" font-size="14" fill="{INK}"></text></g></g>
<g class="cv" data-k="save"><circle r="24" fill="{INK}"/><g id="bkicon"><path id="bkm" d="M-8 -11 h16 v23 l-8 -6 l-8 6z" fill="none" stroke="{GOLD}" stroke-width="2.6" stroke-linejoin="round"/></g>
  <rect x="-62" y="30" width="124" height="22" rx="11" fill="{RED}"/><text y="45" text-anchor="middle" font-family="Anton, Inter" font-size="12" fill="#fff">ENREGISTRE CE REEL</text></g>
<g class="cv" data-k="share"><circle r="24" fill="{INK}"/><g id="plane"><path d="M-11 1 L12 -10 L4 12 L1 3z" fill="{GOLD}"/></g>
  <g id="sharedone"><circle cx="17" cy="-17" r="8" fill="#3FA34D"/><path d="M13 -17 l3 3 l5 -6" stroke="#fff" stroke-width="2" fill="none"/></g>
  <rect x="-70" y="30" width="140" height="22" rx="11" fill="{RED}"/><text y="45" text-anchor="middle" font-family="Anton, Inter" font-size="12" fill="#fff">ENVOIE-LE À UN AMI</text></g>
<g class="cv" data-k="keyword"><rect x="-100" y="-18" width="200" height="34" rx="17" fill="#fff" stroke="{INK}" stroke-width="2"/>
  <text id="kwtx" x="-86" y="5" font-family="Inter" font-weight="800" font-size="15" fill="{INK}"></text>
  <g id="kwsend"><circle cx="82" cy="-1" r="12" fill="{RED}"/><path d="M76 -1 L88 -7 L84 6 L82 0z" fill="#fff"/></g>
  <g id="kwgift"><rect x="-74" y="24" width="148" height="24" rx="12" fill="{GOLD}"/><text y="40" text-anchor="middle" font-family="Anton, Inter" font-size="13" fill="{INK}">→ LE GUIDE GRATUIT</text></g></g>'''

def build(rid):
    D = os.path.join(HERE, rid)
    slug = os.path.basename(glob.glob(os.path.join(REELS, "scripts", f"{rid}-*.md"))[0])[:-3]
    timing = json.load(open(os.path.join(D, "timing.json"), encoding="utf-8"))
    audio = os.path.join(REELS, "voiceover", "audio", slug + ".mp3")
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", audio, "-ac", "1", "-ar", "16000", "-f", "s16le", "-"], capture_output=True).stdout
    n = len(raw) // 2; s = struct.unpack(f"<{n}h", raw); spf = 16000 // FPS
    amp = [math.sqrt(sum(x * x for x in s[i:i + spf]) / spf) / 32768 for i in range(0, n - spf, spf)]
    peak = max(amp); amp = [round(a / peak, 3) for a in amp]
    words = []
    for w in timing["words"]:
        if re.fullmatch(r"[?!:;.,…]+", w["w"]) and words:
            words[-1]["w"] += (" " + w["w"]) if w["w"] in "?!:;" else w["w"]; continue
        words.append(dict(w))
    chunks, cur = [], []
    for w in words:
        cur.append(w)
        if len(cur) >= 4 or (re.search(r"[.?!…:,]$", w["w"]) and len(cur) >= 2) or re.search(r"[.?!…]$", w["w"]):
            chunks.append(cur); cur = []
    if cur: chunks.append(cur)

    def variants(fn, combos, cls):
        return "".join(f'<g class="{cls}" data-k="{p}-{e}" style="display:none">{fn(p, e)}'
                       + (f'<ellipse class="talk" cx="100" cy="140" rx="6.5" ry="0" fill="{MOUTH}"/>' if cls == "sv" else "") + '</g>'
                       for p, e in combos)
    sv = variants(sensei, [(p, e) for p in ("neutre", "enseigne", "stop", "camera") for e in ("serein", "severe", "malin", "rire")], "sv")
    ev = variants(eleve, [(p, e) for p in ("neutre", "filme") for e in ("confiant", "confus", "emerveille")], "ev")
    demo = DEMOS.get(rid, lambda: "")()
    stage = f'''<svg id="stage" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 270 480" width="1080" height="1920">
<defs><clipPath id="vfclip"><rect x="0" y="0" width="230" height="262" rx="6"/></clipPath></defs>
<g id="world"><g id="bg">{decor_studio()}</g>
  <g id="sensei" transform="translate(-200 186) scale(.5)">{sv}</g>
  <g id="eleve" transform="translate(128 222) scale(.44)">{ev}</g>
  <g id="panel" style="display:none"><rect x="-4" y="-4" width="238" height="270" rx="9" fill="{INK}"/>
    <g clip-path="url(#vfclip)">{demo}</g>
    <g fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" opacity=".9"><path d="M10 28 V10 H28"/><path d="M202 10 H220 V28"/><path d="M10 234 V252 H28"/><path d="M220 234 V252 H202"/></g>
    <g id="rec"><circle cx="22" cy="22" r="4.5" fill="{RED}"/><text x="31" y="26" font-family="Inter" font-weight="800" font-size="11" fill="#fff">REC</text></g>
    <text id="tc" x="208" y="26" text-anchor="end" font-family="JetBrains Mono, monospace" font-size="9" fill="#fff">00:00:00:00</text>
    <g id="plabel" style="display:none"><rect id="plbg" x="60" y="232" width="110" height="18" rx="3" fill="{GOLD}"/><text id="pltx" x="115" y="245.5" text-anchor="middle" font-family="Anton, Inter" font-size="12" fill="{INK}"></text></g>
  </g>
  <g id="extra">{EXTRAS.get(rid, lambda: "")()}</g>
  <g id="title"><rect x="20" y="40" width="230" height="44" rx="4" fill="{INK}"/><text id="ttx" x="135" y="72" text-anchor="middle" font-family="Anton, Inter" font-size="26" fill="{GOLD}"></text></g>
  <g id="stamp" style="display:none"><g transform="rotate(-8)"><rect x="-110" y="-46" width="220" height="92" rx="7" fill="{PAPER}" stroke="{RED}" stroke-width="7"/>
    <text id="st1" y="-4" text-anchor="middle" font-family="Anton, Inter" font-size="34" fill="{RED}" letter-spacing="1"></text>
    <text id="st2" y="28" text-anchor="middle" font-family="Anton, Inter" font-size="17" fill="{INK}"></text></g></g>
  <g id="cta" style="display:none">{CTA_SVG}</g>
  <g id="sub" transform="translate(135 388)"><rect id="sbg" x="-100" y="-17" width="200" height="30" rx="5" fill="{INK}" fill-opacity=".88"/>
    <text id="stx" y="4" text-anchor="middle" font-family="Inter" font-weight="800" font-size="12.5" fill="#fff"></text></g>
</g></svg>'''
    data = {"amp": amp, "fps": FPS, "duration": round(n / 16000, 3), "slug": slug,
            "words": [[w["w"], w["s"]] for w in words],
            "chunks": [{"s": c[0]["s"], "e": c[-1]["e"], "w": [[w["w"], w["s"]] for w in c]} for c in chunks]}
    js = open(os.path.join(HERE, "engine.js"), encoding="utf-8").read() + "\n" + open(os.path.join(HERE, "defs", f"{rid}.js"), encoding="utf-8").read()
    html = ('<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Anton&display=swap" rel="stylesheet">'
            '<style>html,body{margin:0;background:#000;width:1080px;height:1920px;overflow:hidden}</style></head><body>'
            + stage + f'<script>const DATA={json.dumps(data, ensure_ascii=False)};\n{js}</script></body></html>')
    open(os.path.join(D, "scene.html"), "w", encoding="utf-8").write(html)
    print(f"{rid} scène ok · {len(chunks)} sous-titres · {data['duration']:.1f}s")

for rid in sys.argv[1:]:
    build(rid)
