# Cloner ta voix sur ElevenLabs

Le clonage, c'est **toi qui le fais** dans ton compte : ElevenLabs demande que ce soit ta propre voix, et pour le clonage pro, il te fait lire une phrase de vérification en direct. Ça prend 20 minutes de préparation et quelques clics.

## Quel type de clone ?

| | **Instant Voice Clone** | **Professional Voice Clone** |
|---|---|---|
| Audio nécessaire | 1 à 3 min (pas plus de 5) | 30 min minimum, idéalement 1 à 3 h |
| Délai | Immédiat | Quelques heures d'entraînement |
| Ressemblance | Bonne | Quasi identique, garde ton accent et ton rythme |
| Pour qui | Tester tout de suite | La série officielle |

**Recommandation :** fais un **Instant** aujourd'hui pour produire les 3 premiers reels, et lance un **Professional** en parallèle (si ton forfait l'inclut) pour la suite.

## Enregistrer de bons échantillons

Le clone copie **tout** : ta voix, mais aussi l'écho de la pièce, le souffle du ventilateur, ta fatigue. Ce qui rentre, c'est ce qui ressort.

- **Pièce** : petite, avec des tissus (chambre, dressing). Pas de cuisine ni de salle de bain.
- **Micro** : ton meilleur (micro-cravate ou USB), à 15–20 cm de la bouche, toujours le même.
- **Format** : WAV ou MP3 haute qualité, 44,1 ou 48 kHz, crêtes autour de −6 dB, jamais dans le rouge.
- **Rien d'autre** : pas de musique, pas de réverbération, pas de débruitage agressif.
- **Le ton** : parle **comme dans tes reels**, en Sensei, énergique et posé. Si tu lis platement, le clone sera plat.
- Coupe les longs silences et les erreurs, garde les respirations naturelles.

## Texte à lire (≈ 2 min 30)

Lis-le 2 fois : une fois calme, une fois avec énergie. Pour le Professional, ajoute la lecture des 10 scripts du dossier `scripts/` et des improvisations sur ton métier jusqu'à 30 min minimum.

> Bienvenue sur la Voie du Pixel. Ici, on n'apprend pas à filmer pour faire joli. On apprend à filmer pour raconter.
> Une caméra qui bouge, ce n'est jamais neutre. Elle avance, et on entre dans l'émotion. Elle recule, et on quitte la scène. Elle monte, et tout devient plus grand. Elle descend, et l'histoire commence.
> Tu crois que le matériel fait tout ? Faux. Un téléphone bien tenu vaut mieux qu'une caméra de cinéma qui tremble sans raison.
> Alors, première question : pourquoi tu bouges ? Si tu n'as pas de réponse, reste fixe. Pose ta caméra. Laisse ton sujet vivre dans le cadre.
> Deuxième question : est-ce que ton monteur va pouvoir couper ? Deux secondes avant, deux secondes après. Toujours.
> Troisième question : est-ce que ton geste est régulier ? Lent, fluide, sans à-coup. Répète-le trois fois avant d'appuyer sur REC.
> Photographie, vidéo, réseaux sociaux : la règle est la même. L'image doit servir le message. Pas l'inverse.
> Un mariage, une marque, un portrait : chaque client mérite une image qui lui ressemble. Et chaque créateur mérite de savoir la fabriquer.
> Allez. On s'entraîne. Un, deux, trois… Action !
> Tu as aimé cette leçon ? Abonne-toi, partage-la à un ami vidéaste, et écris-moi en commentaire quel mouvement tu vas tester en premier. On se retrouve demain, sur la Voie du Pixel.

## Créer le clone

1. ElevenLabs → **Voices** → **Add a new voice** → **Instant Voice Clone** (ou **Professional Voice Clone**).
2. Nom : `Sensei - FR`. Ajoute tes fichiers, coche la case qui confirme que c'est ta voix.
3. Langue : **français**. Description : « voix masculine/féminine, française, chaleureuse, énergique, pédagogue » (adapte).
4. Pour le Professional : suis l'étape de vérification (lecture d'une phrase au micro).
5. Une fois prêt : ouvre la voix → copie son **Voice ID**.

## Réglages de départ pour les reels

| Réglage | Valeur | Pourquoi |
|---|---|---|
| Modèle | **Multilingual v2** | Le plus fiable en français, gère les pauses `<break>` |
| Stability | 45–50 % | Plus bas = plus expressif mais instable |
| Similarity | 80 % | Fidélité à ta voix |
| Style | 10–20 % | Un peu d'intention, sans exagérer |
| Speaker boost | Activé | |

Si un mot est mal prononcé (anglicisme, « gimbal », « tilt »…), écris-le comme il se dit (« guimbal ») uniquement dans le texte envoyé à ElevenLabs.

## Générer les voix des 10 reels

Deux options :
- **À la main** : copie le bloc « Voix off » de chaque script dans le Text to Speech d'ElevenLabs.
- **En automatique** : `tools/generate_voiceovers.py` (voir l'en-tête du fichier). Il faut ta clé API (ElevenLabs → Settings → API Keys) et ton Voice ID.
