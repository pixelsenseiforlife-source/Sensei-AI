"""Construit la bible graphique « La Voie du Pixel » : SVG séparés + bible.html (→ PDF) + maquette.
Utilisation : python3 -I reels/brand/build/build_bible.py && node reels/brand/build/render.js"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from art import *

HERE = os.path.dirname(os.path.abspath(__file__))
BRAND = os.path.dirname(HERE)
def write(rel, content):
    path = os.path.join(BRAND, rel); os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write(content)

VB_CHAR = "-10 0 220 430"
SENSEI_POSES = [("neutre", "serein"), ("enseigne", "malin"), ("stop", "severe"), ("camera", "rire")]
SENSEI_EXPR = ["serein", "severe", "malin", "rire"]
ELEVE_POSES = [("neutre", "confiant"), ("filme", "emerveille")]
ELEVE_EXPR = ["confiant", "confus", "emerveille"]
HEAD_S, HEAD_E = "0 10 200 195", "40 40 140 130"

# ---------- fichiers SVG séparés pour l'animation
for p, e in SENSEI_POSES: write(f"personnages/sensei-{p}.svg", svg(sensei(p, e), VB_CHAR))
for e in SENSEI_EXPR: write(f"personnages/sensei-tete-{e}.svg", svg(sensei_head(e), HEAD_S))
for p, e in ELEVE_POSES: write(f"personnages/eleve-{p}.svg", svg(eleve(p, e), VB_CHAR))
for e in ELEVE_EXPR: write(f"personnages/eleve-tete-{e}.svg", svg(eleve_head(e), HEAD_E))
for name, f in [("rue", decor_rue), ("studio", decor_studio), ("parc", decor_parc)]:
    write(f"decors/decor-{name}.svg", svg(f(), "0 0 270 480", 1080, 1920))
PROPS = [("camera", "Caméra", camera(40, 30), "0 0 80 60"), ("trepied", "Trépied", tripod(), "-4 -12 52 106"),
         ("gimbal", "Gimbal", gimbal(), "10 -18 54 116"), ("slider", "Slider", slider(), "-4 -10 128 106"),
         ("drone", "Drone", drone(), "-26 -6 172 52"), ("smartphone", "Smartphone", phone(14, 22), "0 0 28 44")]
for f, _, g, vb in PROPS: write(f"accessoires/{f}.svg", svg(g, vb))
write("accessoires/tampon-regle.svg", svg(stamp("RÈGLE N°1"), "-6 -20 216 104"))

# ---------- maquette d'un reel (9:16)
def mockup(safe=True):
    zones = ('<g><rect x="0" y="414" width="270" height="66" fill="#E63B2E" opacity=".18"/>'
             '<rect x="232" y="0" width="38" height="480" fill="#E63B2E" opacity=".18"/>'
             '<text x="10" y="472" font-family="Inter" font-size="8" fill="#E63B2E" font-weight="800">ZONE INTERDITE · LÉGENDE / BOUTONS</text>'
             '<text x="252" y="160" font-family="Inter" font-size="8" fill="#E63B2E" font-weight="800" transform="rotate(90 252 160)">ICÔNES</text></g>') if safe else ""
    return (decor_studio()
        + '<g transform="translate(20 40)"><rect width="210" height="44" rx="4" fill="#1B1B1B"/>'
          '<text x="105" y="32" text-anchor="middle" font-family="Anton, Inter" font-size="26" fill="#F2B33D">ARRÊTE DE ZOOMER</text></g>'
        + f'<g transform="translate(14 186) scale(.5)">{sensei("stop","severe")}</g>'
        + f'<g transform="translate(126 216) scale(.44)">{eleve("filme","confus")}</g>'
        + '<g transform="translate(22 368)"><rect width="206" height="30" rx="4" fill="#1B1B1B" opacity=".88"/>'
          '<text x="103" y="20" text-anchor="middle" font-family="Inter" font-weight="800" font-size="11" fill="#fff">Ces deux plans ont l\'air pareils…</text></g>'
        + '<g transform="translate(140 110) scale(.45)">' + stamp("RÈGLE N°2", 170) + '</g>' + zones)
write("maquettes/maquette-reel.svg", svg(mockup(False), "0 0 270 480", 1080, 1920))

# ---------- bible HTML
def sw_(c, n, h): return f'<div class="sw"><span style="background:{c}"></span><b>{n}</b><i>{h}</i></div>'
def card(content, vb, label): return f'<figure>{svg(content, vb)}<figcaption>{label}</figcaption></figure>'
def foot(n): return f'<div class="foot"><span>La Voie du Pixel · Bible graphique</span><span>@iampixelsensei · {n:02d}</span></div>'
css = open(os.path.join(HERE, "bible.css"), encoding="utf-8").read()
logo = "../logo-pixel-sensei.jpg"
P = []
P.append(f'''<section class="page cover"><div class="sun"></div>
  <div class="brandrow"><div class="logo" style="background-image:url({logo})"></div><div><div class="t1">LA VOIE DU PIXEL</div><div class="t2">par Pixel Sensei · Filmmaker &amp; Photographer</div></div></div>
  <h1>Bible<br><span>graphique</span></h1>
  <p class="sub">Personnages, décors, accessoires et règles visuelles de la série de reels animés 2D.</p>
  <div class="hero">{svg(sensei("camera","rire")+'<g transform="translate(230 60) scale(.86)">'+eleve("filme","emerveille")+'</g>', "-10 0 450 430")}</div>
</section>''')
P.append(f'''<section class="page"><div class="kicker">Personnage principal</div><h2>Le <em>Sensei</em></h2>
  <div class="grid2"><div class="big">{svg(sensei("neutre","serein"), VB_CHAR)}</div><div>
    <div class="headbig">{svg(sensei_head("serein"), HEAD_S)}</div>
    <p class="lead">Le maître du logo Pixel Sensei, en version animée. C'est ta voix, ton personnage, ta marque.</p>
    <ul class="notes">
      <li><b>Caractère :</b> calme, bienveillant, malicieux. Il n'élève la voix que pour « STOP ».</li>
      <li><b>Silhouette :</b> chapeau conique très large, barbe en pointe qui part vers la droite, robe longue. Reconnaissable en ombre chinoise.</li>
      <li><b>Proportions :</b> environ 2 têtes de haut, chapeau compris. La tête est grande pour que les expressions se lisent sur un téléphone.</li>
      <li><b>Animation :</b> la barbe suit la tête avec un léger retard. Le chapeau ne se déforme jamais.</li>
    </ul>
    <div class="swatches">{sw_(STRAW,"Paille","#D9A441")}{sw_(BEARD,"Barbe","#4A4A4A")}{sw_(SKIN_S,"Peau","#F1C9A0")}{sw_(SLATE,"Robe","#2F4858")}{sw_(RED,"Ceinture","#E63B2E")}{sw_(GOLD,"Col","#F2B33D")}</div>
  </div></div>{foot(2)}</section>''')
P.append(f'''<section class="page"><div class="kicker">Le Sensei</div><h2>Expressions <em>&amp; poses</em></h2>
  <div class="row4">{"".join(card(sensei_head(e), HEAD_S, l) for e, l in zip(SENSEI_EXPR, ["Serein · explique","Sévère · « STOP ! »","Malin · l'astuce","Rire · fier de l'élève"]))}</div>
  <div class="row4 poses">{"".join(card(sensei(p,e), VB_CHAR, l) for (p,e), l in zip(SENSEI_POSES, ["Neutre","Enseigne (doigt levé)","Stop (main levée)","Caméra (démonstration)"]))}</div>
  {foot(3)}</section>''')
P.append(f'''<section class="page"><div class="kicker">Personnage secondaire</div><h2>L'<em>élève</em></h2>
  <div class="grid2"><div class="row2">{"".join(card(eleve(p,e), VB_CHAR, l) for (p,e), l in zip(ELEVE_POSES, ["Neutre","Filme (téléphone levé)"]))}</div><div>
    <p class="lead">Le spectateur à l'écran : un jeune créateur qui filme tout au téléphone. Il fait les erreurs que ton public fait, et le Sensei les corrige.</p>
    <ul class="notes">
      <li><b>Caractère :</b> enthousiaste, pressé, un peu maladroit. Il progresse d'un reel à l'autre.</li>
      <li><b>Signes distinctifs :</b> cheveux bouclés, sweat à capuche or, smartphone toujours en main.</li>
      <li><b>Proximité :</b> il ressemble à ton audience. Le spectateur doit se dire « c'est moi ».</li>
    </ul>
    <div class="row3">{"".join(card(eleve_head(e), HEAD_E, l) for e, l in zip(ELEVE_EXPR, ["Confiant","Confus","Émerveillé"]))}</div>
    <div class="swatches">{sw_(SKIN_E,"Peau","#8D5A3B")}{sw_(GOLD,"Sweat","#F2B33D")}{sw_(SLATE,"Jean","#2F4858")}{sw_(INK,"Cheveux","#1B1B1B")}</div>
  </div></div>{foot(4)}</section>''')
P.append(f'''<section class="page"><div class="kicker">Les lieux</div><h2>Les <em>décors</em></h2>
  <div class="row3 decors">{card(decor_studio(), "0 0 270 480", "Le studio du Sensei · explications, règles")}{card(decor_rue(), "0 0 270 480", "La rue · travelling, panoramique, zoom")}{card(decor_parc(), "0 0 270 480", "Le parc · drone, parallaxe, profondeur")}</div>
  <p class="small">Format 9:16, 1080 × 1920. Chaque élément du décor (bâtiments, arbres, soleil) est un objet séparé dans le SVG : on peut les décaler à des vitesses différentes pour créer de la parallaxe.</p>
  {foot(5)}</section>''')
P.append(f'''<section class="page"><div class="kicker">Mise en page</div><h2>Un reel <em>type</em></h2>
  <div class="grid2"><div class="mock">{svg(mockup(True), "0 0 270 480")}</div><div>
    <ul class="notes">
      <li><b>Titre :</b> en haut, Anton or sur bandeau noir. 3 à 4 mots maximum.</li>
      <li><b>Personnages :</b> au centre. Le Sensei à gauche (celui qui sait), l'élève à droite.</li>
      <li><b>Sous-titres :</b> Inter Bold blanc sur bandeau noir, 2 lignes maximum, juste au-dessus de la zone basse.</li>
      <li><b>Tampon rouge :</b> la règle du jour s'imprime avec un coup de gong. Toujours incliné de −8°.</li>
      <li><b>Zones interdites (en rouge) :</b> les 250 px du bas (légende, boutons) et les 150 px de droite (icônes j'aime, partage). Rien d'important dedans.</li>
      <li><b>Logo :</b> petit, en haut à gauche, pendant les 2 premières et les 2 dernières secondes seulement.</li>
    </ul></div></div>{foot(6)}</section>''')
P.append(f'''<section class="page"><div class="kicker">Boîte à outils</div><h2>Accessoires <em>&amp; charte</em></h2>
  <div class="props">{"".join(card(g, vb, n) for _, n, g, vb in PROPS)}</div>
  <div class="grid2 bottom"><div><div class="kicker">Le tampon</div>{svg(stamp("RÈGLE N°1"), "-6 -20 216 104", 260)}
      <div class="kicker" style="margin-top:6mm">Typographies</div>
      <p><span class="anton">ANTON</span> pour les titres et tampons · <b>Inter Bold</b> pour les sous-titres et textes.</p></div>
    <div><div class="kicker">Palette</div><div class="swatches">{sw_(PAPER,"Papier","#F4EDE1")}{sw_(INK,"Encre","#1B1B1B")}{sw_(RED,"Vermillon","#E63B2E")}{sw_(GOLD,"Or","#F2B33D")}{sw_(SLATE,"Ardoise","#2F4858")}{sw_(GREEN,"Végétal","#7FA37A")}</div>
      <p class="small">Fichiers fournis : <b>personnages/</b>, <b>decors/</b>, <b>accessoires/</b>, <b>maquettes/</b>. SVG vectoriels avec calques nommés (hat, beard, eyes, mouth, arm-left, arm-right…).</p></div>
  </div>{foot(7)}</section>''')
write("build/bible.html", '<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>Bible graphique La Voie du Pixel</title>'
      '<link href="https://fonts.googleapis.com/css2?family=Anton&display=swap" rel="stylesheet"><style>' + css + '</style></head><body>' + "".join(P) + '</body></html>')
print("ok")
