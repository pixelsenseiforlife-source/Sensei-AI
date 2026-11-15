"""Démonstrations (SVG) affichées dans le cadre caméra 230 × 262 de chaque reel, + éléments spéciaux."""
from art import *

def mini(pose="neutre", expr="confiant", gid="mini", x=0, y=0, k=.3):
    return f'<g id="{gid}" transform="translate({x} {y}) scale({k})">{eleve(pose, expr)}</g>'

def badge(x, y, txt, fill=GOLD, color=INK):
    w = len(txt) * 6.2 + 14
    return (f'<g transform="translate({x} {y})"><rect x="0" y="0" width="{w}" height="15" rx="3" fill="{fill}"/>'
            f'<text x="{w/2}" y="11" text-anchor="middle" font-family="Anton, Inter" font-size="10" fill="{color}">{txt}</text></g>')

def split(top, bottom, lt, lb):
    return f'''<defs><clipPath id="hA"><rect x="0" y="0" width="230" height="128"/></clipPath><clipPath id="hB"><rect x="0" y="134" width="230" height="128"/></clipPath></defs>
<rect width="230" height="262" fill="{INK}"/>
<g clip-path="url(#hA)">{top}<rect id="dimA" width="230" height="128" fill="{INK}" opacity="0"/></g>
<g clip-path="url(#hB)">{bottom}<rect id="dimB" y="134" width="230" height="128" fill="{INK}" opacity="0"/></g>
{badge(8, 108, lt, RED, "#fff")}{badge(8, 242, lb)}'''

RUE_STREET = '<g transform="translate(-20 -225) scale(.852)">' + "{d}" + '</g>'

def demo_02():
    top = f'<g id="zA">{RUE_STREET.format(d=decor_rue())}{mini("neutre","confiant","mA",86,12,.25)}</g>'
    bot = (f'<g transform="translate(0 134)"><g id="bBg">{RUE_STREET.format(d=decor_rue())}</g>'
           f'<g id="bSub">{mini("neutre","confiant","mB",86,12,.25)}</g></g>')
    return split(top, bot, "ZOOM", "TRAVELLING")

def demo_03():
    return (f'<rect width="230" height="262" fill="#F7E9D2"/><g id="vBg"><g transform="translate(-47 -330) scale(1.2)">{decor_rue()}</g></g>'
            f'{mini("neutre","emerveille","vS",79,92,.34)}')

def demo_04():
    return (f'<rect width="230" height="262" fill="#EAF0E1"/><g id="tAll">{decor_parc()}{mini("neutre","confus","tS",150,272,.3)}</g>')

def demo_05():
    far = "".join(f'<g transform="translate({i*270} -170)">{decor_rue()}</g>' for i in range(3))
    fore = ""
    for i in range(4):
        x = i * 120
        fore += (f'<g transform="translate({x} 0)"><rect x="10" y="0" width="18" height="262" fill="{INK}"/>'
                 f'<circle cx="70" cy="-10" r="44" fill="#4F7A4B"/><rect x="40" y="226" width="70" height="40" rx="4" fill="#8A5A3A"/></g>')
    return (f'<rect width="230" height="262" fill="#F7E9D2"/><g id="pFar">{far}</g>'
            f'{mini("filme","confiant","pS",85,107,.3)}<g id="pFore">{fore}</g>')

def demo_06():
    tilt = f'<g id="tiltG"><rect width="230" height="262" fill="{PAPER}"/><g id="tiltS">{sensei("neutre","serein")}</g></g>'
    pano = (f'<g id="panoG"><rect width="230" height="262" fill="#F7E9D2"/><g id="panoS"><g transform="translate(0 -70) scale(.7)">{decor_rue()}</g>'
            f'<g transform="translate(189 -70) scale(.7)">{decor_parc()}</g></g>{mini("filme","confiant","panoM",85,95,.28)}</g>')
    sky = f'<g id="skyG"><g id="skyS" transform="translate(-20 0) scale(1)">{decor_rue()}</g></g>'
    return tilt + pano + sky

def demo_07():
    top = f'<g id="shA"><g transform="translate(-10 -10)"><g id="shBgA">{RUE_STREET.format(d=decor_rue())}</g></g>{mini("filme","emerveille","shMA",86,12,.25)}</g>'
    bot = (f'<g transform="translate(0 134)"><g id="shBgB">{RUE_STREET.format(d=decor_rue())}</g>'
           f'{mini("filme","emerveille","shMB",86,12,.25)}</g>')
    return split(top, bot, "ÉPAULE", "STABILISÉ")

def demo_08():
    return (f'<rect width="230" height="262" fill="#EAF0E1"/><g id="dAll">{decor_parc()}{mini("filme","emerveille","dS",150,272,.3)}</g>'
            f'<g id="dDrone"><g transform="scale(.55)">{drone()}</g></g>')

def demo_09():
    blk = lambda x, w, fill, txt, tc="#fff": (f'<rect x="{x}" y="0" width="{w}" height="34" rx="3" fill="{fill}"/>'
                                            f'<text x="{x + w/2}" y="22" text-anchor="middle" font-family="Anton, Inter" font-size="11" fill="{tc}">{txt}</text>')
    sc = ('<g><circle cx="-6" cy="0" r="5" fill="none" stroke="#fff" stroke-width="2.5"/><circle cx="6" cy="0" r="5" fill="none" stroke="#fff" stroke-width="2.5"/>'
          '<path d="M-3 -4 L8 -20 M3 -4 L-8 -20" stroke="#fff" stroke-width="3" stroke-linecap="round"/></g>')
    return f'''<rect width="230" height="262" fill="#16232E"/>
<g transform="translate(15 12)"><rect width="200" height="112" rx="4" fill="#000"/><g clip-path="url(#monC)"><g transform="translate(-30 -235) scale(.95)">{decor_rue()}</g>
  <g id="monM">{mini("filme","confiant","monMi",70,10,.24)}</g></g>
  <defs><clipPath id="monC"><rect width="200" height="112"/></clipPath></defs>
  <text x="8" y="14" font-family="JetBrains Mono, monospace" font-size="8" fill="#fff">MONITEUR</text></g>
<text x="15" y="146" font-family="Inter" font-weight="800" font-size="9" fill="#9fb3c2" letter-spacing="1">TIMELINE</text>
<g transform="translate(15 154)"><rect width="200" height="34" rx="3" fill="#24394A"/>
  <g id="clipBad">{blk(0, 200, RED, "MOUVEMENT DÈS LA 1RE IMAGE")}</g>
  <g id="clipGood" style="display:none">{blk(0, 44, "#7d8a94", "2 S FIXE")}{blk(46, 108, GOLD, "MOUVEMENT", INK)}{blk(156, 44, "#7d8a94", "2 S FIXE")}</g></g>
<rect id="playhead" x="15" y="150" width="2.5" height="42" fill="#fff"/>
<g id="cut1" transform="translate(15 212)">{sc}</g><g id="cut2" transform="translate(215 212)">{sc}</g>
<g id="verdictBad" style="display:none"><circle cx="198" cy="140" r="11" fill="{RED}"/><path d="M193 135 L203 145 M203 135 L193 145" stroke="#fff" stroke-width="4" stroke-linecap="round"/></g>
<g id="verdictGood" style="display:none"><circle cx="198" cy="140" r="11" fill="#3FA34D"/><path d="M192 140 L196 144 L204 135" stroke="#fff" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/></g>'''

def extra_10():
    rows = ["UN MOUVEMENT = UNE INTENTION", "2 SECONDES AVANT ET APRÈS", "LENT ET RÉGULIER", "RÉPÈTE AVANT DE FILMER"]
    out = '<g id="rules">'
    for i, r in enumerate(rows):
        y = 96 + i * 31
        out += (f'<g id="r{i+1}" transform="translate(135 {y})"><rect x="-112" y="-13" width="224" height="27" rx="4" fill="{PAPER}" stroke="{RED}" stroke-width="3"/>'
                f'<rect x="-112" y="-13" width="27" height="27" rx="4" fill="{RED}"/><text x="-98.5" y="7" text-anchor="middle" font-family="Anton, Inter" font-size="17" fill="#fff">{i+1}</text>'
                f'<text x="-78" y="6" font-family="Anton, Inter" font-size="13" fill="{INK}">{r}</text></g>')
    out += '</g>'
    out += f'''<g id="guide" transform="translate(135 165)"><g transform="rotate(-4)">
  <rect x="-62" y="-80" width="124" height="160" rx="5" fill="{INK}"/><circle cx="20" cy="-20" r="58" fill="{RED}"/>
  <image href="../../brand/logo-pixel-sensei-creme.png" x="-30" y="-70" width="100" height="100"/>
  <text x="-52" y="44" font-family="Anton, Inter" font-size="16" fill="{GOLD}">LA VOIE DU PIXEL</text>
  <text x="-52" y="62" font-family="Inter" font-weight="800" font-size="8.5" fill="{PAPER}">LES MOUVEMENTS DE CAMÉRA</text>
  <rect x="-52" y="-74" width="58" height="14" rx="2" fill="{PAPER}"/><text x="-23" y="-64" text-anchor="middle" font-family="Anton, Inter" font-size="9" fill="{RED}">GRATUIT</text>
</g></g>'''
    return out

DEMOS = {"02": demo_02, "03": demo_03, "04": demo_04, "05": demo_05, "06": demo_06, "07": demo_07, "08": demo_08, "09": demo_09}
EXTRAS = {"10": extra_10}
