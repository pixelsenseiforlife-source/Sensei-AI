"""Synthétise un coup de gong court (WAV 44,1 kHz) frappé à IMPACT secondes."""
import sys, wave
import numpy as np
DUR, IMPACT, SR = float(sys.argv[2]), float(sys.argv[3]), 44100
t = np.arange(int(DUR * SR)) / SR
x = np.zeros_like(t); tt = t - IMPACT; on = tt >= 0
partials = [(98, 1.0, 1.6), (151, .7, 2.0), (212, .55, 2.6), (287, .4, 3.2), (366, .3, 4.0), (471, .22, 5.0), (598, .15, 6.5), (761, .1, 8.0)]
rng = np.random.default_rng(7)
for f, a, d in partials:
    wob = 1 + .004 * np.sin(2 * np.pi * 3.1 * tt)  # léger battement
    x[on] += a * np.exp(-tt[on] * d) * np.sin(2 * np.pi * f * wob[on] * tt[on] + rng.uniform(0, 6))
strike = rng.normal(0, 1, on.sum()) * np.exp(-tt[on] * 40) * .35  # attaque du maillet
x[on] += strike
x *= np.clip(tt / .004, 0, 1)                       # attaque sans clic
fade = np.clip((DUR - t) / .3, 0, 1); x *= fade      # fin propre
x = x / np.abs(x).max() * .7
pcm = (x * 32767).astype(np.int16)
with wave.open(sys.argv[1], "wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
