# La Voie du Pixel — Série de reels animés 2D par Pixel Sensei (@iampixelsensei)

Série de reels courts (25–35 s) sur les **mouvements de caméra**, en animation 2D, avec **ta voix clonée** sur ElevenLabs.
Diffusion : Instagram Reels, TikTok, Facebook Reels, YouTube Shorts.

> Inspiration : le cours « 5 mouvements de caméra » de la page National Video Conception.
> On reprend **le sujet**, pas la forme : univers, personnages, couleurs, textes et structure sont 100 % originaux.

---

## 1. Objectifs (dans cet ordre)

| Objectif | Comment la série y répond |
|---|---|
| **Grossir l'audience** | 1 notion = 1 reel, accroche en 2 s, format « erreur → correction » qui pousse au partage et à l'enregistrement |
| **Vendre la formation** | Aimant à prospects : « Commente SENSEI » → guide PDF gratuit → liste e-mail → formation |
| **Vendre les prestations** | Chaque reel prouve ton expertise. CTA prestation dans la légende sur les reels « client » (portrait, mariage, marque) |

Rotation des appels à l'action : **70 %** engagement / abonnement · **20 %** aimant (SENSEI) · **10 %** prestation.

---

## 2. Le concept : le Sensei et l'élève

Là où la vidéo d'origine est un **cours magistral**, on fait une **mini-histoire** à chaque reel :

1. **L'élève** (jeune créateur, smartphone à la main) fait une erreur classique.
2. **Le Sensei** l'arrête — « Stop. » C'est le maître du logo Pixel Sensei : chapeau conique, sourcils épais, longue barbe, une caméra à la main. Le personnage animé = ta marque.
3. **Démonstration** : l'écran se divise, on voit le bon mouvement et son effet.
4. **Le tampon rouge** : la règle du jour s'imprime à l'écran comme un sceau (« RÈGLE N°3 »).

La voix off, c'est **toi** = le Sensei. Tu parles au spectateur en le tutoyant, comme à ton élève.

### Charte visuelle (originale, différente du modèle)

| Élément | Choix |
|---|---|
| Logo | `brand/logo-pixel-sensei.jpg` : gris anthracite sur crème |
| Fond | Papier crème `#F4EDE1` (texture légère), comme le logo |
| Encre / traits | Noir encre `#1B1B1B` |
| Accent principal | Rouge vermillon `#E63B2E` (tampons, erreurs, flèches) |
| Accent secondaire | Or `#F2B33D` (règles, titres) |
| Schémas caméra | Bleu ardoise `#2F4858` |
| Titres | Anton (ou toute police condensée grasse) |
| Sous-titres | Inter Bold, blanc sur bandeau noir, 2 lignes max |
| Signature sonore | Un « gong » court au tampon final |

### Zone de sécurité 9:16 (1080 × 1920)
- Rien d'important dans les **250 px du bas** (légendes et boutons) ni les **150 px de droite** (icônes like/partage).
- Titres dans le tiers haut, action au centre, sous-titres juste au-dessus de la zone basse.

---

## 3. Les 10 premiers reels

| # | Titre | Notion | CTA |
|---|---|---|---|
| 01 | Le mouvement le plus puissant | Plan fixe | Abonnement |
| 02 | Arrête de zoomer | Zoom vs travelling | Commentaire |
| 03 | L'effet qui déforme le décor | Effet Vertigo | Enregistrer |
| 04 | Même scène, deux émotions | Travelling avant / arrière | Commentaire |
| 05 | Pourquoi tes vidéos sont plates | Travelling latéral + parallaxe | Partage + **prestation** |
| 06 | Rends quelqu'un puissant | Panoramique + tilt | Abonnement + **prestation** |
| 07 | Caméra qui tremble : erreur ? | Épaule vs stabilisé | Commentaire + **prestation** |
| 08 | Ton drone, au début ou à la fin ? | Grue / drone | Enregistrer |
| 09 | Ton monteur te déteste | Règle des 2 secondes | Enregistrer |
| 10 | Les 4 règles de la Voie | Récap des règles d'or | **SENSEI → guide → formation** |

Scripts complets : dossier [`scripts/`](scripts/).

---

## 4. Calendrier de publication (5 semaines)

| Semaine | Lundi | Mercredi | Vendredi |
|---|---|---|---|
| 1 | 01 Plan fixe | 02 Zoom vs travelling | 03 Vertigo |
| 2 | 04 Avant / arrière | 05 Parallaxe | 06 Panoramique |
| 3 | 07 Épaule / stabilisé | 08 Drone | 09 Règle des 2 s |
| 4 | 10 Les 4 règles (SENSEI) | Repost du meilleur reel | **Version longue YouTube** (compilation 3–4 min) |

- **Même vidéo sur les 4 plateformes**, sans filigrane TikTok (exporter depuis ton logiciel, pas depuis l'appli).
- Heures à tester : 12 h et 19 h. On ajuste après 2 semaines selon les stats.
- La compilation YouTube longue regroupe les 10 reels + intro/outro : un seul montage, une vidéo de plus.

---

## 5. Production d'un reel — le circuit

1. **Script** → `scripts/NN-*.md` (voix off + découpage animation)
2. **Voix** → `tools/generate_voiceovers.py` génère les MP3 avec ta voix clonée (voir [`elevenlabs/GUIDE_CLONAGE.md`](elevenlabs/GUIDE_CLONAGE.md))
3. **Animation** → on cale l'animation sur la voix (la voix d'abord, toujours)
4. **Sous-titres** → auto (CapCut / Premiere) puis correction manuelle
5. **Musique** → lo-fi japonisante discrète, −20 dB sous la voix
6. **Signature de fin** → chaque reel se termine par l'outro animée du logo (3,5 s, avec gong) : `brand/outro/outro-pixel-sensei.mp4`
7. **Export** → 1080 × 1920, 30 i/s, H.264, ~15 Mb/s

## 6. À préparer pour l'entonnoir
- [ ] Guide PDF gratuit « La Voie du Pixel : les mouvements de caméra » (aimant à prospects)
- [ ] Réponse automatique au mot « SENSEI » (ManyChat pour Instagram / Facebook, message épinglé sur TikTok)
- [ ] Page de capture e-mail → séquence de 5 e-mails → offre formation
- [ ] Lien en bio : formation + « Réserver une prestation »

## 7. Identité graphique
- Bible graphique : [`brand/Bible-graphique-La-Voie-du-Pixel.pdf`](brand/Bible-graphique-La-Voie-du-Pixel.pdf)
- Fichiers vectoriels pour l'animation : `brand/personnages/`, `brand/decors/`, `brand/accessoires/`, `brand/maquettes/`
- Pour regénérer : `python3 -I reels/brand/build/build_bible.py && node reels/brand/build/render.js`
- Logo détouré (fond transparent) : `brand/logo-pixel-sensei-{noir,creme,gris}.png`
- Outro animée : `brand/outro/outro-pixel-sensei.mp4` (regénérer : `node reels/brand/outro/render_outro.js`)

## 8. Contacts et liens (à utiliser partout)
| | |
|---|---|
| Réseaux | **@iampixelsensei** (Instagram, TikTok, Facebook, YouTube) |
| Formation | **Pixel Creative Hub**, bientôt sur Udemy (ajouter le lien à la sortie) |
| WhatsApp | +235 85 68 44 41 · https://wa.me/23585684441 |
| WhatsApp | +235 95 84 46 95 · https://wa.me/23595844695 |
| Mot-clé aimant | **SENSEI** → guide gratuit « La Voie du Pixel » |
