# -*- coding: utf-8 -*-
"""Convert jpg images referenced by CourtGall/deifich.html to webp (quality 80),
keep originals, then point deifich.html refs at .webp.

- Fixes EXIF orientation before saving (phone photos).
- Downsizes anything larger than 2400px on the long side (lightbox is screen-sized).
- Idempotent: skips files that already have a .webp next to them.
"""
import io, os, re
from PIL import Image, ImageOps

ROOT = r"c:\Users\Lep4i\Desktop\My GitHub\BasketDelfich"
GALL_DIR = os.path.join(ROOT, "CourtGall")
HP = os.path.join(GALL_DIR, "deifich.html")
MAX_SIDE = 2400
QUALITY = 80

html = io.open(HP, encoding="utf-8").read()
refs = sorted(set(re.findall(r'(?:src|href)="(img/[^"]+\.jpg)"', html)))
print("referenced jpgs:", len(refs))

total_before = total_after = 0
converted = skipped = missing = 0
for r in refs:
    p = os.path.join(GALL_DIR, *r.split("/"))
    w = p[:-4] + ".webp"
    if not os.path.exists(p):
        print("MISSING (skipped):", r)
        missing += 1
        continue
    if os.path.exists(w):
        skipped += 1
        total_before += os.path.getsize(p)
        total_after += os.path.getsize(w)
        continue
    im = Image.open(p)
    im2 = ImageOps.exif_transpose(im)
    if im2 is not None:
        im = im2
    im = im.convert("RGB")
    im.thumbnail((MAX_SIDE, MAX_SIDE))
    im.save(w, "WEBP", quality=QUALITY)
    converted += 1
    total_before += os.path.getsize(p)
    total_after += os.path.getsize(w)
    print("%-24s %7d KB -> %6d KB" % (r, os.path.getsize(p) // 1024, os.path.getsize(w) // 1024))

changed = 0
for r in refs:
    old = '"%s"' % r
    new = '"%s.webp"' % r[:-4]
    wp = os.path.join(GALL_DIR, *new.strip('"').split("/"))
    if old in html and os.path.exists(wp):
        n = html.count(old)
        html = html.replace(old, new)
        changed += n

io.open(HP, "w", encoding="utf-8").write(html)
print("converted: %d, skipped(existing webp): %d, missing: %d" % (converted, skipped, missing))
print("deifich.html refs updated:", changed)
print("total jpg  : %.1f MB" % (total_before / 1048576.0))
print("total webp : %.1f MB (%+.0f%%)" % (total_after / 1048576.0, (total_after - total_before) * 100.0 / total_before))
