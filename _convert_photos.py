# -*- coding: utf-8 -*-
"""Convert jpg images referenced by index.html to webp (quality 80),
keep originals, then point index.html refs at .webp."""
import io, os
from PIL import Image

ROOT = r"c:\Users\Lep4i\Desktop\My GitHub\BasketDelfich"
REFS = [
    "img/delf/02.jpg", "img/delf/03.jpg", "img/delf/04.jpg", "img/delf/05.jpg",
    "img/delf/06.jpg", "img/delf/071.jpg", "img/delf/081.jpg", "img/main/main1.jpg",
]

for r in REFS:
    p = os.path.join(ROOT, *r.split("/"))
    if not os.path.exists(p):
        print("MISSING (skipped):", r)
        continue
    w = p[:-4] + ".webp"
    im = Image.open(p).convert("RGB")
    im.save(w, "WEBP", quality=80)
    print("%-22s %6d KB -> %5d KB" % (r, os.path.getsize(p) // 1024, os.path.getsize(w) // 1024))

hp = os.path.join(ROOT, "index.html")
html = io.open(hp, encoding="utf-8").read()
changed = 0
for r in REFS:
    old, new = 'src="%s"' % r, 'src="%s"' % (r[:-4] + ".webp")
    wp = os.path.join(ROOT, *(new.split('src="')[1].strip('"').split("/")))
    if old in html and os.path.exists(wp):
        n = html.count(old)
        html = html.replace(old, new)
        changed += n
io.open(hp, "w", encoding="utf-8").write(html)
print("index.html refs updated:", changed)
