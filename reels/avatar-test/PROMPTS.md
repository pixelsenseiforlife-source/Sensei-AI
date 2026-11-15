# Test avatar : « Vibrance vs Saturation »

## Étape 1 : l'image studio (Magnific / Freepik)

Références : photos 4, 5, 3 et 2 (pas la photo 1, visage levé).
Si l'outil le permet, crée un **personnage personnalisé** à partir de ces 4 photos, puis réutilise-le pour toutes les vidéos.

**Prompt (anglais) :**
```
Vertical 9:16 cinematic portrait of the same man as in the reference photos: Black African man in his early 40s,
long dreadlocks tied back, short goatee with a few grey hairs, warm friendly eyes, confident gentle smile.
He wears a plain black t-shirt. Medium shot from mid-chest up, framed in the lower two thirds of the image,
looking straight into the camera like a YouTube host, mouth relaxed and slightly open as if about to speak.
Setting: a moody filmmaker studio at night, softly blurred background with warm red and amber neon lights,
a camera on a gimbal and a softbox in the background, shallow depth of field, creamy bokeh.
Lighting: soft key light from the left, subtle red rim light on the hair and shoulders, natural skin texture,
realistic pores, no plastic look. Shot on a full-frame cinema camera, 50mm, f/1.8, photorealistic.
Empty dark space in the top third of the frame for a title.
```
**À éviter (negative prompt) :** `hands in frame, extra fingers, text, logo, watermark, cartoon, plastic skin, distorted face, sunglasses`

**Puis l'agrandissement (Magnific Upscaler) :** échelle 2×, Creativity au minimum (0 à 1), Resemblance au maximum, HDR moyen.
Le but : plus de netteté sans changer ton visage.

## Étape 2 : l'animation (Kling)

Image → vidéo, 10 s, format 9:16, mode qualité/pro.

**Prompt :**
```
The man talks naturally to the camera like a friendly YouTube host, subtle head movements, natural blinking,
small eyebrow raises on key words, gentle breathing, warm smile at the end. The camera stays still.
Background neon lights flicker very softly. Realistic, no hand gestures, no camera movement.
```
**À éviter :** `hand gestures, morphing face, camera shake, zoom, extra people`

Puis **Lip Sync** (ou mode Avatar) avec le fichier audio `voix-test-vibrance.mp3`.

## Étape 3 : le montage (Claude)

Envoie le clip Kling : j'ajoute le titre « VIBRANCE vs SATURATION », les sous-titres, une illustration avant/après et l'outro Pixel Sensei.
