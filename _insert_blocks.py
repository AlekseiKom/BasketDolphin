# -*- coding: utf-8 -*-
"""Insert new sections into index.html and append styles to css/style.css."""
import io

ROOT = r"c:\Users\Lep4i\Desktop\My GitHub\BasketDelfich"
PATH = ROOT + "\\index.html"
CSS_PATH = ROOT + "\\css\\style.css"

FACTS = '''\t\t\t\t<section id="court" class="facts">
\t\t\t\t\t<div class="container">
\t\t\t\t\t\t<h2 class="section-heading">О площадке</h2>
\t\t\t\t\t\t<p class="section-sub">Коротко о том, что тебя ждёт у моря</p>
\t\t\t\t\t\t<div class="facts__grid">
\t\t\t\t\t\t\t<div class="fact">
\t\t\t\t\t\t\t\t<svg class="fact__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M4 21V7l8-4 8 4v14"/><path d="M9 21v-6h6v6"/></svg>
\t\t\t\t\t\t\t\t<h3 class="fact__title">Бесплатно</h3>
\t\t\t\t\t\t\t\t<p class="fact__text">Вход свободный — всегда и для всех. Приходи с мячом и друзьями, остальное уже есть.</p>
\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t<div class="fact">
\t\t\t\t\t\t\t\t<svg class="fact__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M3 8c3-2.2 6-2.2 9 0s6 2.2 9 0"/><path d="M3 13c3-2.2 6-2.2 9 0s6 2.2 9 0"/><path d="M3 18c3-2.2 6-2.2 9 0s6 2.2 9 0"/></svg>
\t\t\t\t\t\t\t\t<h3 class="fact__title">Резиновое покрытие</h3>
\t\t\t\t\t\t\t\t<p class="fact__text">Современная резина: мягко к падениям, держит любой стиль игры и не скользит даже после дождя.</p>
\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t<div class="fact">
\t\t\t\t\t\t\t\t<svg class="fact__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="8" height="5"/><circle cx="7" cy="14" r="3.2"/><rect x="13" y="4" width="8" height="5"/><circle cx="17" cy="14" r="3.2"/></svg>
\t\t\t\t\t\t\t\t<h3 class="fact__title">Два кольца</h3>
\t\t\t\t\t\t\t\t<p class="fact__text">Можно играть в две игры одновременно или устроить жаркий 3×3 без очереди.</p>
\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t<div class="fact">
\t\t\t\t\t\t\t\t<svg class="fact__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a8 8 0 0 1-8 8H5l-2 2V12a8 8 0 0 1 8-8h2a8 8 0 0 1 8 8z"/><path d="M9 12h.01M13 12h.01M17 12h.01"/></svg>
\t\t\t\t\t\t\t\t<h3 class="fact__title">Диалог в Viber</h3>
\t\t\t\t\t\t\t\t<p class="fact__text">Есть общий чат площадки, но туда по приглашению. Напиши нам, если хочешь присоединиться.</p>
\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t</div>
\t\t\t\t\t</div>
\t\t\t\t</section>'''
STORY = '''\t\t\t\t<section id="history" class="story">
\t\t\t\t\t<div class="container">
\t\t\t\t\t\t<h2 class="section-heading">История площадки</h2>
\t\t\t\t\t\t<p class="section-sub">Из пустыря — в крутейшую площадку у моря</p>
\t\t\t\t\t\t<div class="story__row">
\t\t\t\t\t\t\t<div class="story__card story__card--before">
\t\t\t\t\t\t\t\t<span class="story__label">Раньше</span>
\t\t\t\t\t\t\t\t<h3 class="story__title">Пустырь у берега</h3>
\t\t\t\t\t\t\t\t<p>Ещё недавно здесь был обычный пустырь — заброшенная территория, где никто не задерживался. Ни разметки, ни колец, ни покрытия: только трава, песок и ветер с моря.</p>
\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t<div class="story__card story__card--now">
\t\t\t\t\t\t\t\t<span class="story__label">Сейчас</span>
\t\t\t\t\t\t\t\t<h3 class="story__title">Крутейшая площадка</h3>
\t\t\t\t\t\t\t\t<p>Теперь здесь резиновое покрытие, два кольца и свет. Пустырь превратился в место, куда приходят за игрой — и остаются: мяч отскакивает ровно, падение мягкое, а рядом шумит Чёрное море.</p>
\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t</div>
\t\t\t\t\t\t<div class="story__text">
\t\t\t\t\t\t\t<p>Раньше площадка стояла совсем в другом месте — рядом с трассой здоровья, там, где раньше была волейбольная площадка для пляжного волейбола. Там тоже играли, но покрытие было не то, а место — неудобное. Сейчас всё иначе: приходи, поиграй — и сам увидишь разницу.</p>
\t\t\t\t\t\t</div>
\t\t\t\t\t</div>
\t\t\t\t</section>'''

REVIEWS = '''\t\t\t\t<section id="reviews" class="reviews">
\t\t\t\t\t<div class="container">
\t\t\t\t\t\t<h2 class="section-heading">Отзывы</h2>
\t\t\t\t\t\t<p class="section-sub">Все, кто был, уходят восторженными</p>
\t\t\t\t\t\t<div class="reviews__grid">
\t\t\t\t\t\t\t<div class="review">
\t\t\t\t\t\t\t\t<p>«Резиновое покрытие — топ: мяч отскакивает ровно, падение мягкое. Два кольца — играем с друзьями без очереди.»</p>
\t\t\t\t\t\t\t\t<cite>— Постоянный игрок</cite>
\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t<div class="review">
\t\t\t\t\t\t\t\t<p>«Приехал на пляж, увидел площадку — остался до вечера. Свет, море в 20 метрах, атмосфера супер.»</p>
\t\t\t\t\t\t\t\t<cite>— Гость из Киева</cite>
\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t<div class="review">
\t\t\t\t\t\t\t\t<p>«Бесплатно и открыто всегда. Приехал на велике, поставил его на велопарковку — и сразу в игру.»</p>
\t\t\t\t\t\t\t\t<cite>— Играем всей компанией</cite>
\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t</div>
\t\t\t\t\t</div>
\t\t\t\t</section>'''
MAPSEC = '''\t\t\t\t<section id="how-to" class="map">
\t\t\t\t\t<div class="container">
\t\t\t\t\t\t<h2 class="section-heading">Как добраться</h2>
\t\t\t\t\t\t<p class="section-sub">Чкаловский пляж, Одесса — площадка в 20 метрах от моря</p>
\t\t\t\t\t\t<div class="map__wrap">
\t\t\t\t\t\t\t<iframe src="https://www.google.com/maps?q=%D0%A7%D0%BA%D0%B0%D0%BB%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9+%D0%BF%D0%BB%D1%8F%D0%B6%2C+%D0%9E%D0%B4%D0%B5%D1%81%D1%81%D0%B0&z=16&output=embed" loading="lazy" title="Карта: Чкаловский пляж, Одесса" allowfullscreen></iframe>
\t\t\t\t\t\t</div>
\t\t\t\t\t\t<p class="map__note">На карте — <b>Чкаловский пляж</b>. Площадка находится прямо у берега, в 20 метрах от моря.</p>
\t\t\t\t\t\t<div class="map__tips">
\t\t\t\t\t\t\t<div class="tip">
\t\t\t\t\t\t\t\t<svg class="tip__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3a6 6 0 0 1 3.9 10.5c-.7.7-1.4 1.4-1.4 2.5h-5c0-1.1-.7-1.8-1.4-2.5A6 6 0 0 1 12 3z"/><path d="M9.5 19h5"/><path d="M10.5 21.5h3"/></svg>
\t\t\t\t\t\t\t\t<h3 class="tip__title">Свет</h3>
\t\t\t\t\t\t\t\t<p class="tip__text">На площадке есть освещение — можно играть и вечером, когда солнце уже село.</p>
\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t<div class="tip">
\t\t\t\t\t\t\t\t<svg class="tip__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M7 9v6M7 12h4M11 9h-4"/><circle cx="16.5" cy="12" r="1"/></svg>
\t\t\t\t\t\t\t\t<h3 class="tip__title">Парковка</h3>
\t\t\t\t\t\t\t\t<p class="tip__text">Рядом с трассой здоровья есть парковка (платная).</p>
\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t<div class="tip">
\t\t\t\t\t\t\t\t<svg class="tip__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="5.5" cy="17" r="3.5"/><circle cx="18.5" cy="17" r="3.5"/><path d="M5.5 17L9 10h4l2.5-3H18"/></svg>
\t\t\t\t\t\t\t\t<h3 class="tip__title">На велике</h3>
\t\t\t\t\t\t\t\t<p class="tip__text">Многие приезжают на велосипеде — и это бесплатно. Рядом есть велопарковка: ставил и играешь.</p>
\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t</div>
\t\t\t\t\t</div>
\t\t\t\t</section>'''
CSS = '''
/* ===== New sections: facts / story / map / reviews ===== */
.section-heading { color:#353738; font-size:24px; font-weight:900; text-transform:uppercase; letter-spacing:3.6px; margin:0 0 14px 0; text-align:center; }
.section-sub { color:#848789; font-size:18px; font-style:italic; line-height:28px; margin:0 auto 50px auto; max-width:640px; text-align:center; }

/* ===== Facts / О площадке ===== */
.facts { padding:110px 0; background-color:#f7f7f7; }
.facts__grid { display:grid; grid-template-columns:repeat(2,1fr); gap:24px; margin-top:50px; }
.fact { background:#fff; border-radius:12px; padding:36px 32px; box-shadow:0 10px 30px rgba(53,55,56,.07); }
.fact__icon { width:44px; height:44px; color:#f07a28; margin-bottom:22px; }
.fact__title { color:#353738; font-size:18px; font-weight:900; text-transform:uppercase; letter-spacing:2.4px; margin:0 0 14px 0; }
.fact__text { color:#848789; font-size:16px; line-height:28px; margin:0; }

/* ===== Story / История ===== */
.story { padding:110px 0; background-color:#fff; }
.story__row { display:grid; grid-template-columns:repeat(2,1fr); gap:24px; }
.story__card { background:#f7f7f7; border-radius:12px; padding:40px 36px; }
.story__label { display:inline-block; color:#fff; background:#848789; font-size:12px; font-weight:900; text-transform:uppercase; letter-spacing:2.4px; padding:8px 16px; border-radius:999px; margin-bottom:20px; }
.story__card--now .story__label { background:#f07a28; }
.story__title { color:#353738; font-size:20px; font-weight:900; margin:0 0 16px 0; }
.story__card p, .story__text p { color:#848789; line-height:30px; font-size:16px; margin:0 0 14px 0; }
.story__text { max-width:820px; margin:40px auto 0 auto; text-align:center; }

/* ===== Map / Как добраться ===== */
.map { padding:110px 0; background-color:#f7f7f7; }
.map__wrap { margin-top:50px; border-radius:12px; overflow:hidden; box-shadow:0 16px 40px rgba(53,55,56,.12); }
.map__wrap iframe { display:block; width:100%; height:480px; border:0; }
.map__note { margin-top:22px; color:#848789; font-size:16px; line-height:28px; text-align:center; }
.map__note b { color:#353738; }
.map__tips { display:grid; grid-template-columns:repeat(3,1fr); gap:24px; margin-top:40px; }
.tip { background:#fff; border-radius:12px; padding:32px 28px; box-shadow:0 10px 30px rgba(53,55,56,.07); }
.tip__icon { width:40px; height:40px; color:#f07a28; margin-bottom:18px; }
.tip__title { color:#353738; font-size:16px; font-weight:900; text-transform:uppercase; letter-spacing:2.4px; margin:0 0 12px 0; }
.tip__text { color:#848789; font-size:15px; line-height:26px; margin:0; }

/* ===== Reviews / Отзывы ===== */
.reviews { padding:110px 0; background-color:#fff; }
.reviews__grid { display:grid; grid-template-columns:repeat(3,1fr); gap:24px; margin-top:50px; }
.review { background:#f7f7f7; border-radius:12px; padding:36px 30px; display:flex; flex-direction:column; gap:18px; }
.review p { color:#848789; line-height:28px; font-size:16px; margin:0; flex:1; }
.review cite { color:#f07a28; font-style:normal; font-weight:700; font-size:14px; letter-spacing:.5px; }

/* ===== Responsive (new sections) ===== */
@media (max-width:900px) {
  .facts__grid, .story__row { grid-template-columns:1fr; }
}
@media (max-width:600px) {
  .map__tips, .reviews__grid { grid-template-columns:1fr; }
  .map__wrap iframe { height:380px; }
}'''
with io.open(PATH, "r", encoding="utf-8") as f:
    html = f.read()
with io.open(CSS_PATH, "r", encoding="utf-8") as f:
    css = f.read()

# --- guards (idempotency) ---
if 'class="facts"' in html or ".facts__grid" in css:
    raise SystemExit("Sections/CSS already inserted - aborting without changes.")
footer_anchor = '\t\t\t\t<footer class="footer">'
assert footer_anchor in html, "footer anchor not found"

# --- insert sections before the footer ---
new_sections = FACTS + "\n\n" + STORY + "\n\n" + MAPSEC + "\n\n" + REVIEWS
html = html.replace(footer_anchor, new_sections + "\n" + footer_anchor)
with io.open(PATH, "w", encoding="utf-8") as f:
    f.write(html)

# --- append styles ---
css = css.rstrip("\n") + "\n\n" + CSS + "\n"
with io.open(CSS_PATH, "w", encoding="utf-8") as f:
    f.write(css)

print("OK: sections inserted into index.html and styles appended to style.css")
