"""Éléments graphiques vectoriels de « La Voie du Pixel » (personnages, décors, accessoires).
Chaque fonction renvoie un fragment SVG dans son propre repère, avec des groupes nommés (id/class)
pour faciliter l'animation (After Effects, Illustrator, Rive...)."""

INK = "#1B1B1B"; PAPER = "#F4EDE1"; RED = "#E63B2E"; GOLD = "#F2B33D"; SLATE = "#2F4858"
SLATE_D = "#24394A"; BEARD = "#4A4A4A"; SKIN_S = "#F1C9A0"; SKIN_E = "#8D5A3B"
STRAW = "#D9A441"; STRAW_L = "#F2C766"; STRAW_D = "#8A6420"; MOUTH = "#7A2A22"; GREEN = "#7FA37A"

def sw(c=INK, w=3.5):
    return f'fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"'

# ---------------------------------------------------------------- SENSEI
def sensei_head(expr="serein"):
    brows = {
        "serein":  ("M70 101 Q83 89 97 99 Q84 95 70 101Z", "M130 101 Q117 89 103 99 Q116 95 130 101Z"),
        "severe":  ("M69 92 L97 103 L96 97 L71 86Z", "M131 92 L103 103 L104 97 L129 86Z"),
        "malin":   ("M70 101 Q83 89 97 99 Q84 95 70 101Z", "M130 92 Q117 79 103 89 Q116 85 130 92Z"),
        "rire":    ("M70 98 Q83 86 97 96 Q84 92 70 98Z", "M130 98 Q117 86 103 96 Q116 92 130 98Z"),
    }[expr]
    if expr == "serein":
        eyes = f'<path d="M76 109 Q84 103 92 109" {sw()}/><path d="M108 109 Q116 103 124 109" {sw()}/>'
    elif expr == "rire":
        eyes = f'<path d="M76 111 Q84 101 92 111" {sw(w=4)}/><path d="M108 111 Q116 101 124 111" {sw(w=4)}/>'
    else:
        eyes = (f'<ellipse cx="84" cy="109" rx="4.2" ry="5" fill="{INK}"/><circle cx="85.5" cy="107.3" r="1.3" fill="#fff"/>'
                f'<ellipse cx="116" cy="109" rx="4.2" ry="5" fill="{INK}"/><circle cx="117.5" cy="107.3" r="1.3" fill="#fff"/>')
    mouth = {
        "serein": f'<path d="M95 138 Q100 141 105 138" {sw(w=2.5)}/>',
        "severe": f'<ellipse cx="100" cy="140" rx="6" ry="8" fill="{MOUTH}"/>',
        "malin":  f'<path d="M93 136 Q101 144 108 134" {sw(w=2.5)}/>',
        "rire":   f'<path d="M91 134 Q100 152 109 134Z" fill="{MOUTH}"/>',
    }[expr]
    return f'''<g class="sensei-head" data-expression="{expr}">
  <g id="hair"><path d="M54 84 Q46 124 72 152 L76 96Z" fill="{BEARD}"/><path d="M146 84 Q154 124 128 152 L124 96Z" fill="{BEARD}"/></g>
  <path id="face" d="M68 84 H132 V124 Q132 154 100 154 Q68 154 68 124Z" fill="{SKIN_S}"/>
  <g id="brows" fill="{BEARD}"><path d="{brows[0]}"/><path d="{brows[1]}"/></g>
  <g id="eyes">{eyes}</g>
  <path id="nose" d="M96 119 Q100 123 104 119" {sw(c="#B9875E", w=2.5)}/>
  <path id="beard" d="M70 122 Q78 130 90 127 Q100 123 110 127 Q122 130 130 122 Q138 152 124 174 Q114 188 120 198 Q100 196 90 180 Q72 160 70 122Z" fill="{BEARD}"/>
  <path id="mouth-area" d="M87 129 Q100 125 113 129 Q111 147 100 153 Q89 147 87 129Z" fill="{SKIN_S}"/>
  <g id="mouth">{mouth}</g>
  <path id="mustache" d="M78 126 Q90 118 100 125 Q110 118 122 126 Q112 133 100 129 Q88 133 78 126Z" fill="{BEARD}"/>
  <path d="M92 158 L100 172 L108 158" fill="{SKIN_S}" opacity=".0"/>
  <g id="hat">
    <path d="M12 84 L100 20 L188 84 Q100 99 12 84Z" fill="{STRAW}"/>
    <path d="M103 32 Q121 45 116 58 Q134 54 146 64 Q128 72 104 72 Q131 65 124 62 Q106 64 112 54 Q116 44 103 32Z" fill="{STRAW_L}"/>
    <path d="M30 86 Q100 98 170 86 Q100 104 30 86Z" fill="{STRAW_D}"/>
    <path d="M12 84 L100 20 L188 84" {sw(c=STRAW_D, w=2)}/>
  </g>
</g>'''

def camera(cx=0, cy=0, s=1.0):
    return f'''<g class="prop-camera" transform="translate({cx} {cy}) scale({s})">
  <rect x="-20" y="-24" width="16" height="9" rx="2" fill="#3A3A3A"/>
  <rect x="-30" y="-17" width="60" height="34" rx="5" fill="{INK}"/>
  <rect x="-30" y="-8" width="60" height="5" fill="{GOLD}"/>
  <circle r="13" fill="#3A3A3A"/><circle r="8" fill="{SLATE}"/><circle cx="-3" cy="-3" r="2.5" fill="#fff" opacity=".8"/>
  <circle cx="22" cy="-11" r="2.5" fill="{RED}"/>
</g>'''

def sensei(pose="neutre", expr="serein"):
    robe = f'''<g id="robe">
  <path d="M62 160 Q100 150 138 160 L156 408 Q100 418 44 408Z" fill="{SLATE}"/>
  <path d="M84 160 L100 214 L116 160Z" fill="{PAPER}"/>
  <path d="M78 160 L100 222 L122 160" {sw(c=GOLD, w=5)}/>
  <path d="M100 222 L102 408" {sw(c=SLATE_D, w=3)}/>
  <path d="M50 262 Q100 272 150 262 L151 284 Q100 294 49 284Z" fill="{RED}"/>
  <path d="M96 282 L88 318 M104 282 L112 318" {sw(c=RED, w=6)}/>
  <ellipse cx="78" cy="414" rx="17" ry="7" fill="{INK}"/><ellipse cx="122" cy="414" rx="17" ry="7" fill="{INK}"/>
</g>'''
    L_down = f'<g id="arm-left"><path d="M64 166 Q34 222 40 300 L72 300 Q66 240 78 198Z" fill="{SLATE_D}"/><circle cx="56" cy="308" r="10" fill="{SKIN_S}"/></g>'
    R_down = f'<g id="arm-right"><path d="M136 166 Q166 222 160 300 L128 300 Q134 240 122 198Z" fill="{SLATE_D}"/><circle cx="144" cy="308" r="10" fill="{SKIN_S}"/></g>'
    if pose == "neutre":
        arms, extra = L_down + R_down, ""
    elif pose == "enseigne":
        arms = L_down + f'''<g id="arm-right"><path d="M134 166 Q170 150 178 112 L196 118 Q190 170 142 206Z" fill="{SLATE_D}"/>
  <rect x="180" y="74" width="7" height="26" rx="3.5" fill="{SKIN_S}"/><circle cx="187" cy="106" r="11" fill="{SKIN_S}"/></g>'''
        extra = ""
    elif pose == "stop":
        arms = L_down + f'''<g id="arm-right"><path d="M134 166 Q172 176 178 214 L160 222 Q154 196 128 200Z" fill="{SLATE_D}"/>
  <g fill="{SKIN_S}"><rect x="160" y="168" width="28" height="34" rx="9"/><rect x="161" y="150" width="6" height="24" rx="3"/><rect x="168" y="146" width="6" height="26" rx="3"/><rect x="175" y="148" width="6" height="24" rx="3"/><rect x="182" y="154" width="6" height="20" rx="3"/><rect x="152" y="176" width="14" height="7" rx="3.5" transform="rotate(-30 159 179)"/></g></g>'''
        extra = ""
    else:  # camera
        arms = (f'<g id="arm-left"><path d="M64 166 Q44 222 78 252 L96 236 Q70 214 80 192Z" fill="{SLATE_D}"/></g>'
                f'<g id="arm-right"><path d="M136 166 Q156 222 122 252 L104 236 Q130 214 120 192Z" fill="{SLATE_D}"/></g>')
        extra = camera(100, 236, 1.0) + f'<circle cx="72" cy="244" r="10" fill="{SKIN_S}"/><circle cx="128" cy="244" r="10" fill="{SKIN_S}"/>'
    return f'<g class="sensei" data-pose="{pose}">{robe}{arms}{sensei_head(expr)}{extra}</g>'

# ---------------------------------------------------------------- ÉLÈVE
def eleve_head(expr="confiant"):
    curls = "".join(f'<circle cx="{x}" cy="{y}" r="11" fill="{INK}"/>' for x, y in
                    [(58, 86), (68, 68), (84, 57), (100, 53), (116, 57), (132, 68), (142, 86)])
    if expr == "emerveille":
        eyes = (f'<ellipse cx="84" cy="106" rx="8" ry="10" fill="#fff"/><circle cx="84" cy="107" r="5" fill="{INK}"/><circle cx="86" cy="104" r="1.6" fill="#fff"/>'
                f'<ellipse cx="116" cy="106" rx="8" ry="10" fill="#fff"/><circle cx="116" cy="107" r="5" fill="{INK}"/><circle cx="118" cy="104" r="1.6" fill="#fff"/>')
    else:
        eyes = (f'<ellipse cx="84" cy="107" rx="7" ry="8" fill="#fff"/><circle cx="85" cy="108" r="4.5" fill="{INK}"/><circle cx="86.5" cy="106" r="1.4" fill="#fff"/>'
                f'<ellipse cx="116" cy="107" rx="7" ry="8" fill="#fff"/><circle cx="117" cy="108" r="4.5" fill="{INK}"/><circle cx="118.5" cy="106" r="1.4" fill="#fff"/>')
    brows = {
        "confiant":   f'<path d="M75 93 Q84 88 93 92" {sw(w=4)}/><path d="M107 92 Q116 88 125 93" {sw(w=4)}/>',
        "confus":     f'<path d="M75 90 L93 95" {sw(w=4)}/><path d="M107 94 Q116 86 125 91" {sw(w=4)}/>',
        "emerveille": f'<path d="M74 87 Q84 80 94 86" {sw(w=4)}/><path d="M106 86 Q116 80 126 87" {sw(w=4)}/>',
    }[expr]
    mouth = {
        "confiant":   f'<path d="M88 128 Q100 140 112 128" {sw(w=3.5)}/>',
        "confus":     f'<path d="M88 132 L94 128 L100 132 L106 128 L112 132" {sw(w=3)}/>',
        "emerveille": f'<ellipse cx="100" cy="132" rx="8" ry="10" fill="{MOUTH}"/>',
    }[expr]
    q = f'<text x="150" y="60" font-family="Anton, Inter, sans-serif" font-size="34" fill="{RED}">?</text>' if expr == "confus" else ""
    return f'''<g class="eleve-head" data-expression="{expr}">
  <circle cx="52" cy="110" r="9" fill="{SKIN_E}"/><circle cx="148" cy="110" r="9" fill="{SKIN_E}"/>
  <circle id="face" cx="100" cy="106" r="48" fill="{SKIN_E}"/>
  <g id="hair"><path d="M54 98 Q54 58 100 56 Q146 58 146 98 Q132 76 100 74 Q68 76 54 98Z" fill="{INK}"/>{curls}</g>
  <g id="brows">{brows}</g><g id="eyes">{eyes}</g>
  <path id="nose" d="M97 116 Q100 120 103 116" {sw(c="#5E3A26", w=2.5)}/>
  <g id="mouth">{mouth}</g>{q}
</g>'''

def phone(x, y, rot=0):
    return (f'<g class="prop-phone" transform="translate({x} {y}) rotate({rot})">'
            f'<rect x="-11" y="-19" width="22" height="38" rx="4" fill="{INK}"/><rect x="-8" y="-15" width="16" height="28" rx="2" fill="{SLATE}"/>'
            f'<circle cx="5" cy="-11" r="2" fill="{RED}"/></g>')

def eleve(pose="neutre", expr="confiant"):
    body = f'''<g id="body">
  <rect x="92" y="148" width="16" height="40" fill="{SKIN_E}"/>
  <path d="M74 178 Q100 196 126 178 Q118 196 100 200 Q82 196 74 178Z" fill="#C98F1F"/>
  <path d="M60 192 Q100 178 140 192 L148 304 Q100 312 52 304Z" fill="{GOLD}"/>
  <path d="M74 262 H126 L122 290 H78Z" fill="#E0A42E"/>
  <path d="M94 200 L92 236 M106 200 L108 236" {sw(c=PAPER, w=3)}/>
  <path d="M56 302 H144 L140 404 H106 L100 330 L94 404 H60Z" fill="{SLATE}"/>
  <ellipse cx="78" cy="410" rx="20" ry="9" fill="#fff" stroke="{INK}" stroke-width="2.5"/>
  <ellipse cx="122" cy="410" rx="20" ry="9" fill="#fff" stroke="{INK}" stroke-width="2.5"/>
</g>'''
    L = f'<g id="arm-left"><path d="M62 196 Q42 240 46 296 L66 296 Q64 248 76 214Z" fill="{GOLD}"/><circle cx="56" cy="304" r="10" fill="{SKIN_E}"/></g>'
    if pose == "filme":
        R = (f'<g id="arm-right"><path d="M138 196 Q186 196 190 162 L174 156 Q170 184 128 214Z" fill="{GOLD}"/>'
             f'{phone(186, 142, 90)}<circle cx="182" cy="158" r="10" fill="{SKIN_E}"/></g>')
    else:
        R = (f'<g id="arm-right"><path d="M138 196 Q158 240 154 296 L134 296 Q136 248 124 214Z" fill="{GOLD}"/>'
             f'{phone(146, 300, -10)}<circle cx="144" cy="308" r="10" fill="{SKIN_E}"/></g>')
    return f'<g class="eleve" data-pose="{pose}">{body}{L}{R}{eleve_head(expr)}</g>'

# ---------------------------------------------------------------- DÉCORS (9:16, 270 x 480)
def decor_rue():
    win = lambda x, y, n, c: "".join(f'<rect x="{x+i*22}" y="{y}" width="12" height="16" rx="2" fill="{c}"/>' for i in range(n))
    return f'''<g class="decor" id="decor-rue">
  <rect width="270" height="480" fill="#F7E9D2"/><circle cx="210" cy="90" r="34" fill="{GOLD}" opacity=".7"/>
  <rect x="0" y="150" width="90" height="250" fill="#C9B79C"/>{win(12,170,3,PAPER)}{win(12,205,3,PAPER)}{win(12,240,3,PAPER)}
  <rect x="90" y="120" width="96" height="280" fill="{SLATE}"/>{win(102,140,4,GOLD)}{win(102,178,4,"#3E5D72")}{win(102,216,4,GOLD)}
  <rect x="186" y="170" width="84" height="230" fill="#D98C6A"/>{win(198,190,3,PAPER)}{win(198,226,3,PAPER)}
  <rect x="120" y="340" width="30" height="60" fill="{INK}"/>
  <rect x="0" y="400" width="270" height="80" fill="#BFAE93"/><rect x="0" y="398" width="270" height="6" fill="#A8977C"/>
  <rect x="226" y="300" width="5" height="100" fill="{INK}"/><circle cx="228" cy="296" r="8" fill="{GOLD}"/>
  <circle cx="40" cy="330" r="30" fill="{GREEN}"/><rect x="37" y="350" width="6" height="50" fill="#6B4A2B"/>
</g>'''

def decor_studio():
    return f'''<g class="decor" id="decor-studio">
  <rect width="270" height="480" fill="{PAPER}"/>
  {"".join(f'<line x1="{x}" y1="0" x2="{x}" y2="330" stroke="#E2D6C2" stroke-width="2"/>' for x in range(45,270,45))}
  <line x1="0" y1="110" x2="270" y2="110" stroke="#E2D6C2" stroke-width="2"/><line x1="0" y1="220" x2="270" y2="220" stroke="#E2D6C2" stroke-width="2"/>
  <circle cx="135" cy="170" r="92" fill="{RED}"/>
  <rect x="200" y="40" width="44" height="120" fill="#FBF6EC" stroke="{STRAW_D}" stroke-width="3"/>
  <text x="222" y="118" font-family="IPAGothic, sans-serif" font-size="34" text-anchor="middle" fill="{INK}">道</text>
  <rect x="0" y="330" width="270" height="150" fill="#C99A5B"/>
  {"".join(f'<line x1="0" y1="{y}" x2="270" y2="{y}" stroke="#B5864A" stroke-width="2"/>' for y in range(360,480,30))}
  <rect x="0" y="326" width="270" height="8" fill="{STRAW_D}"/>
  <g transform="translate(40 250)"><path d="M0 80 L18 0 L36 80 M18 0 L18 80" {sw(c=INK, w=3)}/>{camera(18,-10,.55)}</g>
</g>'''

def decor_parc():
    return f'''<g class="decor" id="decor-parc">
  <rect width="270" height="480" fill="#EAF0E1"/><circle cx="60" cy="80" r="26" fill="{GOLD}" opacity=".8"/>
  <path d="M0 260 Q70 200 140 250 Q210 190 270 240 V480 H0Z" fill="#A9C39A"/>
  <path d="M0 330 Q90 290 170 330 Q230 300 270 320 V480 H0Z" fill="{GREEN}"/>
  <path d="M110 480 Q130 400 150 330 L162 330 Q156 400 170 480Z" fill="#E6D6B4"/>
  <g><rect x="206" y="250" width="8" height="90" fill="#6B4A2B"/><circle cx="210" cy="240" r="34" fill="#5E8A5A"/></g>
  <g><rect x="40" y="300" width="6" height="60" fill="#6B4A2B"/><circle cx="43" cy="292" r="24" fill="#5E8A5A"/></g>
  <g transform="translate(180 380)"><rect width="60" height="8" rx="2" fill="#8A5A3A"/><rect y="-16" width="60" height="6" rx="2" fill="#8A5A3A"/><rect x="6" y="8" width="5" height="16" fill="{INK}"/><rect x="49" y="8" width="5" height="16" fill="{INK}"/></g>
</g>'''

# ---------------------------------------------------------------- ACCESSOIRES
def tripod():
    return f'<g class="prop-tripod"><path d="M0 90 L22 0 L44 90 M22 0 L22 90" {sw(c=INK, w=4)}/><rect x="10" y="-8" width="24" height="10" rx="2" fill="#3A3A3A"/></g>'

def gimbal():
    return (f'<g class="prop-gimbal"><rect x="16" y="40" width="12" height="54" rx="6" fill="{INK}"/>'
            f'<path d="M22 40 V22 H44 V6" {sw(c="#3A3A3A", w=6)}/><rect x="30" y="-14" width="30" height="20" rx="3" fill="{INK}"/>'
            f'<rect x="34" y="-10" width="22" height="12" rx="2" fill="{SLATE}"/><circle cx="22" cy="62" r="3" fill="{RED}"/></g>')

def slider():
    return (f'<g class="prop-slider"><rect x="0" y="40" width="120" height="8" rx="3" fill="#3A3A3A"/>'
            f'<rect x="0" y="48" width="6" height="22" fill="{INK}"/><rect x="114" y="48" width="6" height="22" fill="{INK}"/>'
            f'<rect x="44" y="30" width="30" height="12" rx="2" fill="{GOLD}"/>{camera(59,14,.6)}'
            f'<path d="M20 86 H100" {sw(c=GOLD, w=4)}/><path d="M92 80 L100 86 L92 92" {sw(c=GOLD, w=4)}/></g>')

def drone():
    rot = lambda x: f'<ellipse cx="{x}" cy="0" rx="22" ry="4" fill="#9a9a9a" opacity=".7"/><rect x="{x-2}" y="0" width="4" height="10" fill="{INK}"/>'
    return (f'<g class="prop-drone"><path d="M0 12 H120" {sw(c=INK, w=5)}/>{rot(0)}{rot(120)}'
            f'<rect x="40" y="4" width="40" height="22" rx="8" fill="{INK}"/><circle cx="60" cy="34" r="8" fill="#3A3A3A"/><circle cx="60" cy="34" r="4" fill="{SLATE}"/></g>')

def stamp(text="RÈGLE N°1", w=200):
    return (f'<g class="prop-stamp" transform="rotate(-8)"><rect x="0" y="0" width="{w}" height="56" rx="6" fill="{PAPER}" stroke="{RED}" stroke-width="7"/>'
            f'<text x="{w/2}" y="40" text-anchor="middle" font-family="Anton, Inter, sans-serif" font-size="30" fill="{RED}" letter-spacing="1">{text}</text></g>')

def svg(content, vb, w=None, h=None):
    size = (f' width="{w}"' if w else "") + (f' height="{h}"' if h else "")
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}"{size}>{content}</svg>'
