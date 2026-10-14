#!/usr/bin/env python3
"""Generates the six pages of the Dental Solutions of Winter Haven site from one set of shared parts.
Run `python3 build.py` after editing; the .html files are the output.

The one motif is the outline of Lake Eloise (assets/data/lakes.json), the lake behind the office.
It is the hero shape, the mask of every photograph, the button, the bullet and the footer."""
import json, pathlib, random, urllib.parse

ROOT = pathlib.Path(__file__).parent
LAKES = json.load(open(ROOT / 'assets/data/lakes.json'))
MOTIF = LAKES['motif']

def t(en, es):
    """One piece of text in both languages. CSS shows the active one."""
    return f'<span data-l="en">{en}</span><span data-l="es">{es}</span>'

PHONE = '(863) 324‑7121'
TEL = 'tel:+18633247121'
MAIL = 'maria@dentalsolutionsofwh.com'
ADDR1 = '6390 Cypress Gardens Blvd, Suite B'
ADDR2 = 'Winter Haven, FL 33884'
MAPS = 'https://www.google.com/maps/dir/?api=1&destination=6390+Cypress+Gardens+Blvd+Winter+Haven+FL+33884'
REVIEW = 'https://www.google.com/search?q=Dental+Solutions+of+Winter+Haven+reviews'

PAGES = [
    ('index.html', 'Home', 'Inicio'),
    ('services.html', 'Services', 'Servicios'),
    ('sleep-apnea.html', 'Sleep apnea', 'Apnea del sueño'),
    ('doctors.html', 'Doctors', 'Doctores'),
    ('reviews.html', 'Reviews', 'Opiniones'),
    ('contact.html', 'Contact', 'Contacto'),
]

CREDITS = json.load(open(ROOT / 'assets/credits.json'))

# --------------------------------------------------------------------------- shared parts
def svg_data(path_d, fill='black'):
    svg = f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1 1' preserveAspectRatio='none'><path d='{path_d}' fill='{fill}'/></svg>"
    return 'url("data:image/svg+xml,' + urllib.parse.quote(svg, safe="'/:=<>, ") .replace(' ', '%20') + '")'

CHEV = 'url("data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 16 16%27%3E%3Cpath d=%27M3 6l5 5 5-5%27 fill=%27none%27 stroke=%27%2310282b%27 stroke-width=%272%27/%3E%3C/svg%3E")'
CHEV_LIGHT = CHEV.replace('%2310282b', '%23f4f1ea')

def root_vars():
    mask = svg_data(MOTIF)
    coupon = ("radial-gradient(14px at 46% 0, transparent 97%, #000 100%), radial-gradient(14px at 46% 100%, transparent 97%, #000 100%)")
    coupon_v = ("radial-gradient(14px at 0 46%, transparent 97%, #000 100%), radial-gradient(14px at 100% 46%, transparent 97%, #000 100%)")
    return (f":root{{--lake-mask:{mask};--chev:{CHEV};--chev-light:{CHEV_LIGHT};--coupon-mask:{coupon};--coupon-mask-v:{coupon_v};}}"
            ".coupon{-webkit-mask-composite:source-in;mask-composite:intersect;}")

def lake_defs():
    return (f'<svg width="0" height="0" aria-hidden="true" style="position:absolute"><defs>'
            f'<clipPath id="lake" clipPathUnits="objectBoundingBox"><path d="{MOTIF}"/></clipPath>'
            f'<clipPath id="lake-wide" clipPathUnits="objectBoundingBox"><path d="{MOTIF}" transform="translate(0 1) rotate(-90)"/></clipPath>'
            f'<symbol id="lk" viewBox="0 0 1 1" preserveAspectRatio="none"><path d="{MOTIF}"/></symbol>'
            f'</defs></svg>')

def schema():
    data = {"@context": "https://schema.org", "@type": "Dentist", "name": "Dental Solutions of Winter Haven",
            "url": "https://www.dentalsolutionsofwh.com/", "telephone": "+1-863-324-7121", "email": MAIL,
            "address": {"@type": "PostalAddress", "streetAddress": ADDR1, "addressLocality": "Winter Haven", "addressRegion": "FL", "postalCode": "33884", "addressCountry": "US"},
            "geo": {"@type": "GeoCoordinates", "latitude": 27.9825809, "longitude": -81.6782343},
            "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday"], "opens": "08:00", "closes": "17:00"}],
            "employee": [{"@type": "Person", "name": "Dr. Carlos A. Polo", "jobTitle": "Prosthodontist"}, {"@type": "Person", "name": "Dr. Jose G. Cruz", "jobTitle": "Dentist"}],
            "knowsLanguage": ["en", "es", "de"], "paymentAccepted": "Cash, Check, Visa, Mastercard, American Express, Discover, CareCredit"}
    return json.dumps(data, ensure_ascii=False)

FAVICON = "data:image/svg+xml," + urllib.parse.quote(f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'><rect width='64' height='64' fill='#f4f1ea'/><g transform='translate(14 6) scale(36 52)'><path d='{MOTIF}' fill='#146b73'/></g></svg>")

def head(title, desc):
    return f'''<!doctype html>
<html lang="en" data-lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#146b73">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:locale" content="en_US">
<meta property="og:locale:alternate" content="es_US">
<script type="application/ld+json">{schema()}</script>
<script>document.documentElement.classList.add('js');try{{var l=localStorage.getItem('dswh-lang');if(l==='es'||l==='en'){{document.documentElement.dataset.lang=l;document.documentElement.lang=l;}}}}catch(e){{}}</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Hanken+Grotesk:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="icon" href="{FAVICON}">
<link rel="stylesheet" href="styles.css">
<style>{root_vars()}</style>
</head>
<body>
{lake_defs()}
<a class="skip" href="#main">{t("Skip to content", "Ir al contenido")}</a>
'''

CUR = ' aria-current="page"'
LAZY = ' loading="lazy"'

def header(current):
    links = ''.join(f'<a href="{f}"{CUR if f == current else ""}>{t(en, es)}</a>' for f, en, es in PAGES[1:])
    return f'''<header class="top">
  <div class="wrap top-row">
    <a class="wordmark" href="index.html" aria-label="Dental Solutions of Winter Haven, home"><i aria-hidden="true"></i><span><b>Dental Solutions</b><small>of Winter Haven</small></span></a>
    <nav class="menu" id="menu" aria-label="Main">{links}
      <button class="lang" id="lang" type="button" aria-label="Cambiar idioma / Change language">{t("Español", "English")}</button>
    </nav>
    <a class="btn" href="contact.html">{t("Book a visit", "Reservar cita")}</a>
    <button class="burger" id="burger" type="button" aria-expanded="false" aria-controls="menu">{t("Menu", "Menú")}</button>
  </div>
</header>
<main id="main">'''

def credits_line():
    parts = []
    for c in CREDITS:
        title = c['title'] if len(c['title']) < 60 else c['title'][:57].rstrip() + '…'
        parts.append(f'<a href="{c["page"]}" rel="noopener">{title}</a> ({c["creator"]}, {c.get("license") or c.get("licence")})')
    return ' · '.join(parts)

def footer():
    colours = ['#146b73', '#3f7a4a', '#cfe3e2', '#146b73', '#d7e4cf', '#0f565d', '#146b73', '#cfe3e2', '#3f7a4a']
    heights = [78, 100, 62, 88, 70, 96, 58, 84, 92]
    chain = ''.join(f'<i style="background:{c};height:{h}%"></i>' for c, h in zip(colours, heights))
    links = ''.join(f'<a href="{f}">{t(en, es)}</a>' for f, en, es in PAGES)
    return f'''</main>
<footer class="foot">
  <div class="wrap">
    <div class="foot-chain" aria-hidden="true" data-reveal>{chain}</div>
    <div class="grid foot-grid" data-reveal>
      <div class="foot-links">
        <div><a href="index.html">Dental Solutions of Winter Haven</a>{links}</div>
        <div><a href="services.html">{t("Services", "Servicios")}</a><a href="services.html#general">{t("Family dentistry", "Odontología familiar")}</a><a href="services.html#prostho">{t("Prosthodontics", "Prostodoncia")}</a><a href="services.html#cosmetic">{t("Cosmetic", "Estética")}</a><a href="services.html#implants">{t("Implants and surgery", "Implantes y cirugía")}</a><a href="sleep-apnea.html">{t("Sleep apnea", "Apnea del sueño")}</a></div>
        <div><a href="doctors.html">{t("Doctors", "Doctores")}</a><a href="doctors.html#polo">Dr. Carlos A. Polo</a><a href="doctors.html#cruz">Dr. Jose G. Cruz</a><a href="reviews.html">{t("Reviews", "Opiniones")}</a></div>
        <div><a href="contact.html">{t("Visit", "Visita")}</a><a href="contact.html#hours">{t("Hours and directions", "Horario y cómo llegar")}</a><a href="contact.html#pay">{t("Insurance and payment", "Seguros y pagos")}</a><a href="contact.html#faq">{t("Questions", "Preguntas")}</a></div>
      </div>
      <div class="foot-contact">
        <p>{ADDR1}<br>{ADDR2}</p>
        <p><a href="{TEL}">{PHONE}</a><br><a href="mailto:{MAIL}">{MAIL}</a></p>
        <p>{t("Monday to Thursday, 8 a.m. to 5 p.m. Friday by appointment.", "Lunes a jueves, 8 a.m. a 5 p.m. Viernes con cita.")}</p>
        <p>English · Español · Deutsch</p>
      </div>
    </div>
    <div class="foot-bottom">
      <span>© 2026 Dental Solutions of Winter Haven, PLC</span>
      <a class="btn btn-paper" href="{TEL}">{t("Call", "Llamar")} {PHONE}</a>
    </div>
    <p class="credits">{t("Pictures of Winter Haven and Central Florida, used with thanks:", "Imágenes de Winter Haven y Florida Central, usadas con agradecimiento:")} {credits_line()}. {t("Map tiles", "Mapa")} © OpenStreetMap contributors (ODbL). {t("None of the pictures shows the office itself.", "Ninguna imagen muestra el consultorio en sí.")}</p>
  </div>
</footer>
<script src="main.js"></script>
</body>
</html>
'''

def pic(src, alt, w, h, cls='pic pic-tall lake', lazy=True, extra=''):
    return f'<figure class="{cls}"{extra}><img src="{src}" alt="{alt}" width="{w}" height="{h}"{LAZY if lazy else ""}></figure>'

def section_title(en, es, lead=None, light=False):
    out = f'<h2 class="h2">{t(en, es)}</h2>'
    if lead:
        out += f'<p class="lead{" muted" if not light else ""}">{t(*lead)}</p>'
    return out

def cta_band(en_h='Ready for a first visit?', es_h='¿Agendamos su primera visita?'):
    return f'''<section class="section section-tight field on-lake">
  <div class="wrap grid band" data-reveal>
    <div class="band-text">
      <h2 class="h2">{t(en_h, es_h)}</h2>
      <p>{t("Call during office hours, or send a message and the front desk will get back to you the next business day. Same‑day times are kept for emergencies.", "Llame en horario de oficina o envíe un mensaje y la recepción le responde el siguiente día hábil. Se reservan horas del mismo día para urgencias.")}</p>
    </div>
    <div class="band-actions btn-row">
      <a class="btn btn-citrus" href="contact.html">{t("Book a visit", "Reservar cita")}</a>
      <a class="btn btn-paper" href="{TEL}">{t("Call", "Llamar")} {PHONE}</a>
    </div>
  </div>
</section>'''

# --------------------------------------------------------------------------- drawings (one flat language)
INK, LAKE, PAPER, CYP = '#10282b', '#146b73', '#f4f1ea', '#3f7a4a'
ART = {
    'general': f'<svg viewBox="0 0 100 100" aria-hidden="true"><path d="M30 12c10-6 30-6 40 0 12 7 14 24 8 38-3 7-4 20-6 30-1 6-7 7-9 1-2-6-3-16-7-16s-5 10-7 16c-2 6-8 5-9-1-2-10-3-23-6-30-6-14-4-31 6-38z" fill="{INK}"/><path d="M38 24c6-4 18-4 24 0" fill="none" stroke="{PAPER}" stroke-width="5" stroke-linecap="round"/></svg>',
    'prostho': f'<svg viewBox="0 0 160 100" aria-hidden="true"><path d="M22 58h116v10c0 14-26 24-58 24S22 82 22 68z" fill="{INK}"/><path d="M34 56c4-22 18-36 46-36s42 14 46 36c-14 6-30 9-46 9s-32-3-46-9z" fill="{LAKE}"/><path d="M50 55c2-12 12-22 30-22s28 10 30 22" fill="none" stroke="{PAPER}" stroke-width="5" stroke-linecap="round"/><rect x="60" y="66" width="40" height="8" rx="4" fill="{PAPER}"/></svg>',
    'cosmetic': f'<svg viewBox="0 0 100 100" aria-hidden="true"><path d="M28 10h44c4 0 6 3 6 7l-6 54c-2 14-10 21-22 21S30 85 28 71L22 17c0-4 2-7 6-7z" fill="{INK}"/><path d="M34 16h20c2 0 3 2 3 4l-4 50c-1 9-4 13-9 13" fill="{LAKE}"/></svg>',
    'implants': f'<svg viewBox="0 0 100 100" aria-hidden="true"><path d="M26 10h48c4 0 6 3 5 7l-5 20H26l-5-20c-1-4 1-7 5-7z" fill="{INK}"/><path d="M38 40h24l-3 10H41zM40 54h20l-3 10H43zM42 68h16l-3 10H45zM44 82h12l-6 10z" fill="{LAKE}"/></svg>',
    'sleep': f'<svg viewBox="0 0 100 100" aria-hidden="true"><path d="M14 36c0-10 8-16 36-16s36 6 36 16-8 14-36 14-36-4-36-14z" fill="{INK}"/><path d="M14 64c0 10 8 16 36 16s36-6 36-16-8-14-36-14-36 4-36 14z" fill="{LAKE}"/><rect x="20" y="46" width="12" height="8" rx="2" fill="{INK}"/><rect x="68" y="46" width="12" height="8" rx="2" fill="{INK}"/></svg>',
    'emergency': f'<svg viewBox="0 0 100 100" aria-hidden="true"><path d="M30 12c10-6 30-6 40 0 12 7 14 24 8 38-3 7-4 20-6 30-1 6-7 7-9 1-2-6-3-16-7-16s-5 10-7 16c-2 6-8 5-9-1-2-10-3-23-6-30-6-14-4-31 6-38z" fill="{INK}"/><path d="M52 14l-10 30h12l-8 30 24-38H56l8-22z" fill="{PAPER}"/></svg>',
}

def flow_svg(horizontal=True):
    rnd = random.Random(1884)
    uses = []
    if horizontal:
        W, H, uw, uh = 1200, 260, 11, 16
        # left third: scattered, two pale tones
        for _ in range(58):
            x, y = rnd.uniform(0, 360), rnd.uniform(0, H - uh)
            uses.append((x, y, '#cfe3e2' if rnd.random() < 0.55 else '#dcd6c6'))
        # middle third: tight ribbon three high
        for i in range(22):
            for j in range(3):
                uses.append((420 + i * 15, H / 2 - 24 + j * 16, '#5e9a9c'))
        # right third: neat rows in the accent
        for i in range(14):
            for j in range(5):
                uses.append((790 + i * 28, 40 + j * 38, LAKE))
    else:
        W, H, uw, uh = 300, 420, 10, 14
        for _ in range(48):
            x, y = rnd.uniform(0, W - uw), rnd.uniform(0, 130)
            uses.append((x, y, '#cfe3e2' if rnd.random() < 0.55 else '#dcd6c6'))
        for i in range(3):
            for j in range(8):
                uses.append((W / 2 - 22 + i * 15, 160 + j * 15, '#5e9a9c'))
        for i in range(8):
            for j in range(5):
                uses.append((40 + i * 30, 300 + j * 24, LAKE))
    body = ''.join(f'<use href="#lk" x="{x:.0f}" y="{y:.0f}" width="{uw}" height="{uh}" fill="{c}"/>' for x, y, c in uses)
    return f'<svg class="{"horizontal" if horizontal else "vertical"}" viewBox="0 0 {W} {H}" width="{W}" height="{H}" aria-hidden="true">{body}</svg>'

def chain_map():
    paths = ''.join(f'<path d="{l["path"]}" data-name="{l["name"]}" class="{"is-near" if l["km"] < 3 else ""}"><title>{l["name"]}</title></path>' for l in LAKES['lakes'])
    ox, oy = LAKES['office']
    return (f'<svg id="chain-map" viewBox="0 0 {LAKES["W"]} {LAKES["H"]}" role="img" aria-label="Map of the lakes of Winter Haven with the office marked">'
            f'{paths}<circle class="office-ring" cx="{ox}" cy="{oy}" r="26"/><circle class="office" cx="{ox}" cy="{oy}" r="12"/>'
            f'<text x="{ox + 36}" y="{oy + 9}" data-l="en">The office</text><text x="{ox + 36}" y="{oy + 9}" data-l="es">El consultorio</text><text id="chain-label" text-anchor="middle" x="0" y="0"></text></svg>')

def lake_options():
    opts = ''.join(f'<option value="{l["name"]}" data-km="{l["km"]}" data-cx="{l["cx"]}" data-cy="{l["cy"]}">{l["name"]}</option>' for l in sorted(LAKES['lakes'], key=lambda l: l['name']))
    return f'<option value="" data-en="Choose a lake…" data-es="Elija un lago…">Choose a lake…</option>{opts}'

def tilemap():
    g = json.load(open(ROOT / 'assets/map/grid.json'))
    tiles = ''.join(f'<img src="assets/map/{g["z"]}-{x}-{y}.png" width="256" height="256" alt="" loading="lazy">' for y in g['rows'] for x in g['cols'])
    return (f'<div class="tilemap" role="img" aria-label="Map of 6390 Cypress Gardens Boulevard, Winter Haven"><div class="tilemap-grid">{tiles}</div>'
            f'<span class="tilemap-pin" style="left:{g["marker"][0]*100:.2f}%;top:{g["marker"][1]*100:.2f}%"></span></div>')

# --------------------------------------------------------------------------- content
SERVICES = [
    ('general', 'tile-b', ('Family and general dentistry', 'Odontología general y familiar'),
     ('Cleanings, checkups and digital X‑rays, for everyone in the family.', 'Limpiezas, revisiones y radiografías digitales, para toda la familia.'),
     ('The exams and cleanings that keep teeth and gums strong, and the small repairs that stop small problems from growing.', 'Los exámenes y limpiezas que mantienen dientes y encías fuertes, y las reparaciones pequeñas que evitan que un problema crezca.'),
     [('Cleanings and checkups', 'Limpiezas y revisiones'), ('Digital X‑rays', 'Radiografías digitales'), ('Tooth‑colored fillings', 'Empastes del color del diente'), ('Sealants', 'Sellantes'), ('Scaling and root planing', 'Raspado y alisado radicular'), ('Root canal therapy', 'Tratamiento de conducto'), ('Mouth guards', 'Protectores bucales'), ('Extractions', 'Extracciones')]),
    ('prostho', 'tile-a', ('Prosthodontics', 'Prostodoncia'),
     ('Crowns, bridges, dentures and full‑mouth reconstruction, by a specialist.', 'Coronas, puentes, prótesis y reconstrucción completa, con un especialista.'),
     ('Dr. Polo is a prosthodontist: a dentist with specialty training in replacing and rebuilding teeth. The cases that usually mean a referral somewhere else are done here.', 'El Dr. Polo es prostodoncista: un dentista con formación de especialidad en reemplazar y reconstruir dientes. Los casos que suelen significar una remisión a otro lugar se hacen aquí.'),
     [('Crowns and bridges', 'Coronas y puentes'), ('Complete and partial dentures', 'Prótesis completas y parciales'), ('Implant restorations', 'Restauración sobre implantes'), ('Full‑mouth reconstruction', 'Reconstrucción de boca completa'), ('Bite and wear problems', 'Problemas de mordida y desgaste')]),
    ('cosmetic', 'tile-c', ('Cosmetic dentistry', 'Odontología estética'),
     ('Porcelain veneers, ZOOM! whitening, Botox and Juvederm.', 'Carillas de porcelana, blanqueamiento ZOOM!, Botox y Juvederm.'),
     ('Treatments that change how a smile looks, planned so the result still looks like you.', 'Tratamientos que cambian cómo se ve una sonrisa, planeados para que el resultado siga pareciéndose a usted.'),
     [('Porcelain veneers', 'Carillas de porcelana'), ('ZOOM! teeth whitening', 'Blanqueamiento ZOOM!'), ('Cosmetic fillings', 'Empastes estéticos'), ('Botox and Juvederm', 'Botox y Juvederm')]),
    ('implants', 'tile-a', ('Implants and oral surgery', 'Implantes y cirugía oral'),
     ('From one missing tooth to a full arch on implants.', 'Desde un diente perdido hasta una arcada completa sobre implantes.'),
     ('Replacing one, several or all missing teeth, with the restoration designed by the prosthodontist who will finish it.', 'Reemplazo de uno, varios o todos los dientes perdidos, con la restauración diseñada por el prostodoncista que la terminará.'),
     [('Dental implant restorations', 'Restauraciones sobre implantes dentales'), ('Implant‑supported dentures', 'Prótesis sobre implantes'), ('Simple and surgical extractions', 'Extracciones simples y quirúrgicas'), ('Oral surgery', 'Cirugía oral')]),
    ('sleep', 'tile-b', ('Sleep apnea treatment', 'Tratamiento de apnea del sueño'),
     ('A custom oral appliance instead of a CPAP mask.', 'Un aparato bucal a medida en lugar de la máscara CPAP.'),
     ('A small custom device worn at night that keeps the airway open. Quieter than CPAP, nothing to plug in, fits in a pocket.', 'Un pequeño dispositivo a medida que se usa de noche y mantiene abierta la vía aérea. Más silencioso que el CPAP, sin enchufes, cabe en un bolsillo.'),
     [('Custom dental sleep devices', 'Dispositivos dentales para dormir, a medida'), ('Snoring', 'Ronquidos'), ('An alternative to CPAP or surgery', 'Una alternativa al CPAP o la cirugía'), ('Follow‑up adjustments', 'Ajustes de seguimiento')]),
    ('emergency', 'tile-c', ('Emergencies', 'Urgencias'),
     ('Seen the same day when a tooth can’t wait.', 'Atención el mismo día cuando un diente no puede esperar.'),
     ('A broken tooth, an abscess, pain that keeps you up. Call first thing and the front desk will find a time that day whenever it can.', 'Un diente roto, un absceso, un dolor que no deja dormir. Llame a primera hora y la recepción buscará una hora ese mismo día siempre que pueda.'),
     [('Toothache and swelling', 'Dolor de muela e hinchazón'), ('Broken or knocked‑out teeth', 'Dientes rotos o caídos'), ('Lost crowns and fillings', 'Coronas y empastes perdidos'), ('Same‑day times kept open', 'Horas del mismo día reservadas')]),
]

QUOTES = [
    (('“Dr. Polo explained everything he was doing and why. The staff was super wonderful, and I got a same‑day appointment for a painful tooth.”',
      '“El Dr. Polo me explicó todo lo que hacía y por qué. El personal fue maravilloso, y me dieron cita el mismo día por un diente que dolía.”'), 'Carol S.'),
    (('“I came in without an appointment with a dental abscess and was seen the same day. Very competent, professional and meticulous, and the clinic is very clean.”',
      '“Llegué sin cita con un absceso dental y me atendieron el mismo día. Muy competente, profesional y meticuloso, y la clínica está impecable.”'), t('A patient, 2019', 'Un paciente, 2019')),
    (('“Dr. Cruz did my implants. He is kind and compassionate, and the work is excellent.”',
      '“El Dr. Cruz hizo mis implantes. Es amable y compasivo, y el trabajo es excelente.”'), 'Judee C.'),
    (('“I was treated very well and felt very comfortable with the practice.”',
      '“Me trataron muy bien y me sentí muy cómoda en el consultorio.”'), 'Amity K.'),
]

FAQS = [
    (('Insurance', 'Seguros'), ('Do you take my insurance?', '¿Aceptan mi seguro?'),
     ('Most PPO plans are accepted, and the office files the claim for you. Call with the details on your card and the front desk will check your coverage before you come in. There is no Medicaid or Medicare dental at this time.', 'Se aceptan la mayoría de los planes PPO, y el consultorio presenta el reclamo por usted. Llame con los datos de su tarjeta y la recepción verifica su cobertura antes de su visita. Por ahora no se acepta Medicaid ni Medicare dental.')),
    (('Languages', 'Idiomas'), ('Can I be seen in Spanish or German?', '¿Me pueden atender en español o alemán?'),
     ('Yes. Both doctors speak Spanish, Dr. Polo also speaks German, and the whole visit, from the phone call to the treatment plan, can happen in your language.', 'Sí. Los dos doctores hablan español, el Dr. Polo también habla alemán, y toda la visita, desde la llamada hasta el plan de tratamiento, puede ser en su idioma.')),
    (('Emergencies', 'Urgencias'), ('What if I have a toothache today?', '¿Y si tengo dolor de muela hoy?'),
     (f'Call <a href="{TEL}">{PHONE}</a> as early as you can. Same‑day times are kept open for emergencies, Monday to Thursday, and patients have been seen the same day without an appointment.', f'Llame al <a href="{TEL}">{PHONE}</a> lo antes posible. Se reservan horas del mismo día para urgencias, de lunes a jueves, y hay pacientes que han sido atendidos el mismo día sin cita.')),
    (('Paying', 'Pagos'), ('How can I pay, and is there financing?', '¿Cómo puedo pagar, y hay financiamiento?'),
     ('Cash, check, Visa, Mastercard, American Express and Discover are accepted. CareCredit financing is available, with a prequalification that does not affect your credit score. Every plan comes with its cost written down before anything starts.', 'Se acepta efectivo, cheque, Visa, Mastercard, American Express y Discover. Hay financiamiento con CareCredit, con una precalificación que no afecta su puntaje de crédito. Cada plan viene con su costo por escrito antes de empezar.')),
    (('Sleep', 'Sueño'), ('Can a dentist really treat sleep apnea?', '¿Un dentista puede tratar la apnea del sueño?'),
     ('For many people with mild to moderate obstructive sleep apnea, yes. A custom oral appliance holds the lower jaw slightly forward so the airway stays open. It is fitted here after a sleep study, and adjusted until it is comfortable.', 'Para muchas personas con apnea obstructiva leve a moderada, sí. Un aparato bucal a medida sostiene la mandíbula un poco hacia adelante para que la vía aérea quede abierta. Se ajusta aquí después de un estudio del sueño, hasta que sea cómodo.')),
]

def faq_cards(items):
    out = ''
    for i, (tab, q, a) in enumerate(items):
        out += (f'<details class="card card-{i % 3 + 1}" name="faq" style="--tab:{min(i * 150, 600)}px"{" open" if i == 0 else ""}>'
                f'<summary><span class="tab">{t(*tab)}</span><span class="q">{t(*q)}</span></summary><div class="a"><p>{t(*a)}</p></div></details>')
    return out

def pay_tiles():
    names = ['Visa', 'Mastercard', 'American Express', 'Discover', 'CareCredit', t('Most PPO plans', 'La mayoría de planes PPO'), t('Cash and check', 'Efectivo y cheque'), 'CitiHealth']
    return '<div class="pay">' + ''.join(f'<div>{n}</div>' for n in names) + '</div>'

def coupon(mail=MAIL):
    reasons = [('Cleaning and checkup', 'Limpieza y revisión'), ('Toothache or emergency', 'Dolor o urgencia'), ('Crowns, dentures or implants', 'Coronas, prótesis o implantes'), ('Cosmetic: veneers, whitening', 'Estética: carillas, blanqueamiento'), ('Sleep apnea appliance', 'Aparato para apnea del sueño'), ('Something else', 'Otra cosa')]
    opts = ''.join(f'<option data-en="{en}" data-es="{es}">{en}</option>' for en, es in reasons)
    return f'''<section class="coupon-wrap">
  <div class="wrap grid">
    <form class="coupon" id="contact-form" data-mail="{mail}" data-reveal>
      <div class="coupon-left">
        <h2 class="h2">{t("Request a visit", "Solicite una cita")}</h2>
        <p>{t("Send this and the front desk replies by phone or email the next business day. For same‑day pain, call instead.", "Envíe esto y la recepción le responde por teléfono o correo el siguiente día hábil. Si tiene dolor hoy, mejor llame.")}</p>
      </div>
      <div class="coupon-right">
        <label class="sr" for="f-name">{t("Your name", "Su nombre")}</label>
        <input id="f-name" name="name" type="text" autocomplete="name" required placeholder="Your name" data-en="Your name" data-es="Su nombre">
        <label class="sr" for="f-phone">{t("Phone", "Teléfono")}</label>
        <input id="f-phone" name="phone" type="tel" autocomplete="tel" required placeholder="Phone" data-en="Phone" data-es="Teléfono">
        <label class="sr" for="f-reason">{t("Reason for the visit", "Motivo de la visita")}</label>
        <select id="f-reason" name="reason">{opts}</select>
        <label class="sr" for="f-msg">{t("Message", "Mensaje")}</label>
        <textarea id="f-msg" name="message" placeholder="Anything we should know (optional)" data-en="Anything we should know (optional)" data-es="Algo que debamos saber (opcional)"></textarea>
        <button class="coupon-submit" type="submit">{t("Send the request", "Enviar la solicitud")}</button>
      </div>
    </form>
    <p class="form-note">{t("The form opens your email app with the message written for you. No information is stored on this site.", "El formulario abre su aplicación de correo con el mensaje ya escrito. Este sitio no guarda ninguna información.")}</p>
  </div>
</section>'''

# =================================================================== HOME
def home():
    tiles = ''
    for i, (key, tone, name, fact, _, _) in enumerate(SERVICES):
        wide = ' tile-wide' if key == 'prostho' else ''
        href = 'sleep-apnea.html' if key == 'sleep' else f'services.html#{key}'
        tiles += f'<a class="tile{wide}" href="{href}"><div class="tile-art {tone}">{ART[key]}</div><h3>{t(*name)}</h3><p>{t(*fact)}</p></a>'
    quotes = ''.join(f'<blockquote class="mark"><p>{t(*q)}</p><footer>{name}</footer></blockquote>' for q, name in QUOTES)
    return f'''
<section class="hero wrap grid">
  <div class="hero-text">
    <h1 class="h1" data-rise style="--i:0">{t("Two dentists, one plan.", "Dos dentistas, un plan.")}</h1>
    <p class="lead" data-rise style="--i:1">{t("A prosthodontist and a general dentist at 6390 Cypress Gardens Boulevard, Winter Haven. From a cleaning to a full‑mouth reconstruction, in English, Spanish and German.", "Un prostodoncista y un dentista general en 6390 Cypress Gardens Boulevard, Winter Haven. De una limpieza a una reconstrucción completa, en español, inglés y alemán.")}</p>
    <div class="btn-row" data-rise style="--i:2">
      <a class="btn" href="contact.html">{t("Book a visit", "Reservar cita")}</a>
      <a class="textlink" href="{TEL}">{t("or call", "o llame al")} {PHONE}</a>
    </div>
    <p class="hero-note small muted" data-rise style="--i:3"><span class="open-now" data-open-now></span> · {t("Monday to Thursday, 8 to 5 · Same‑day emergencies", "Lunes a jueves, 8 a 5 · Urgencias el mismo día")}</p>
  </div>
  <div class="hero-pair lake" aria-hidden="true"></div>
  <figure class="hero-shape lake shutter">
    <img src="assets/winter-haven-legoland-florida-island-in-the.jpg" alt="Lake Eloise seen from above, with the far shore and summer clouds" width="1920" height="1402" fetchpriority="high">
  </figure>
</section>

<section class="wrap">
  <div class="statement-block" data-reveal>
    <p class="statement">{t("Between Lake Eloise and Lake Winterset, on the road to Cypress Gardens", "Entre Lake Eloise y Lake Winterset, camino a Cypress Gardens")} <span class="inl"><img src="assets/cypress-gardens-41115552574.jpg" alt="" width="640" height="409" loading="lazy"></span> {t("a prosthodontist and a general dentist look after Winter Haven’s families", "un prostodoncista y un dentista general cuidan a las familias de Winter Haven")} <span class="inl"><img src="assets/cypress-gardens-florida-26975314327.jpg" alt="" width="640" height="402" loading="lazy"></span> {t("in three languages.", "en tres idiomas.")}</p>
  </div>
</section>

<section class="section" id="services">
  <div class="wrap grid spec">
    <div class="spec-head" data-reveal>
      {section_title("Everything a smile needs", "Todo lo que una sonrisa necesita")}
      <p class="muted">{t("Six areas of care, one office. The prosthodontist plans the restorative work; the general dentist keeps everything else healthy.", "Seis áreas de atención, un solo consultorio. El prostodoncista planea el trabajo restaurador; el dentista general mantiene sano todo lo demás.")}</p>
      <div class="btn-row"><a class="btn" href="services.html">{t("All services", "Todos los servicios")}</a></div>
    </div>
    <div class="tiles" data-reveal>{tiles}</div>
  </div>
</section>

<section class="section">
  <div class="wrap grid" data-reveal>
    <div class="flow-head">
      {section_title("Your first visit", "Su primera visita")}
      <p class="muted">{t("About an hour. Everything you are worried about goes in; one plan, in steps you can afford, comes out.", "Alrededor de una hora. Entran todas sus preocupaciones; sale un solo plan, en pasos que pueda pagar.")}</p>
    </div>
    <div class="flow-diagram">{flow_svg(True)}{flow_svg(False)}</div>
    <div class="flow-steps">
      <div><h3>{t("Everything", "Todo")}</h3><p>{t("Tell us what hurts, what you avoid, what you have been told before. Photographs and digital X‑rays, at a fraction of the old dose.", "Cuéntenos qué duele, qué evita, qué le han dicho antes. Fotografías y radiografías digitales, con una fracción de la dosis de antes.")}</p></div>
      <div><h3>{t("One exam", "Un examen")}</h3><p>{t("Both doctors can look at the same case: the general dentist for the health of teeth and gums, the prosthodontist for what needs rebuilding.", "Los dos doctores pueden ver el mismo caso: el dentista general por la salud de dientes y encías, el prostodoncista por lo que hay que reconstruir.")}</p></div>
      <div><h3>{t("One plan", "Un plan")}</h3><p>{t("Options in order, with what each costs and what can wait. Nothing starts until you say so.", "Opciones en orden, con lo que cuesta cada una y lo que puede esperar. Nada empieza hasta que usted lo diga.")}</p></div>
    </div>
  </div>
</section>

<section class="section-tight">
  <div class="panel" data-reveal>
    <div class="panel-head">
      <h2 class="h2">{t("A specialist and a generalist, together", "Un especialista y un generalista, juntos")}</h2>
    </div>
    <div class="panel-text">
      <div><h3>Dr. Carlos A. Polo, DDS, MS</h3><p>{t("Prosthodontist. Graduated cum laude from the Universidad Francisco Marroquín School of Dentistry in Guatemala City in 2003, then specialty training in prosthodontics. Crowns, dentures, implants and full reconstructions. English, Spanish and German.", "Prostodoncista. Graduado cum laude de la Facultad de Odontología de la Universidad Francisco Marroquín, en la Ciudad de Guatemala, en 2003, y luego formación de especialidad en prostodoncia. Coronas, prótesis, implantes y reconstrucciones completas. Inglés, español y alemán.")}</p></div>
      <div><h3>Dr. Jose G. Cruz, DDS</h3><p>{t("General dentist and co‑founder of the practice. Checkups, fillings, root canals, extractions and implant work, for children and adults, in English and Spanish.", "Dentista general y cofundador del consultorio. Revisiones, empastes, conductos, extracciones e implantes, para niños y adultos, en español e inglés.")}</p></div>
      <div class="btn-row"><a class="btn btn-paper" href="doctors.html">{t("Meet the doctors", "Conozca a los doctores")}</a></div>
    </div>
    <figure class="panel-portrait lake pic drift">
      <img src="assets/hartman-litho-sales-co-ig4-e-8595.jpg" alt="Vintage postcard of Gardenia Lane in Idylwild Gardens, Winter Haven" width="1920" height="1209" loading="lazy">
    </figure>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="board" data-reveal>
      <div class="mark mark-head"><h2 class="h2">{t("4.9 stars on Google", "4,9 estrellas en Google")}</h2><p>{t("From more than 260 patient reviews. A few of them:", "De más de 260 opiniones de pacientes. Algunas:")}</p></div>
      {quotes}
      <div class="mark mark-fact"><p class="big">English · Español · Deutsch</p><p class="note">{t("Three languages at the front desk and in the chair", "Tres idiomas en la recepción y en el sillón")}</p></div>
      <div class="mark mark-pic lake"><img src="assets/jacaranda-apartments-winter-haven-florida.jpg" alt="Vintage postcard of the Jacaranda Apartments, Winter Haven" width="1024" height="646" loading="lazy"></div>
    </div>
    <div class="btn-row" style="margin-top:2rem"><a class="btn" href="reviews.html">{t("All reviews", "Todas las opiniones")}</a></div>
  </div>
</section>

<section class="section field on-lake chain">
  <div class="wrap grid">
    <div class="chain-text" data-reveal>
      <h2 class="h2">{t("How far is your lake?", "¿Qué tan lejos queda su lago?")}</h2>
      <p>{t("Winter Haven is a chain of lakes joined by canals. The office is on Cypress Gardens Boulevard, between Lake Eloise and Lake Winterset. Pick the lake you live near.", "Winter Haven es una cadena de lagos unidos por canales. El consultorio está en Cypress Gardens Boulevard, entre Lake Eloise y Lake Winterset. Elija el lago cerca del que vive.")}</p>
      <div class="chain-pick">
        <label for="lake-select">{t("Your lake", "Su lago")}</label>
        <select id="lake-select">{lake_options()}</select>
      </div>
      <div class="chain-result" id="chain-result" aria-live="polite"><strong>{t("Pick your lake", "Elija su lago")}</strong><span>{t("Distances are approximate, from the middle of the lake to the office.", "Las distancias son aproximadas, del centro del lago al consultorio.")}</span></div>
      <div class="btn-row"><a class="btn btn-citrus" href="{MAPS}" target="_blank" rel="noopener">{t("Directions", "Cómo llegar")}</a></div>
    </div>
    <div class="chain-map">{chain_map()}<p class="chain-note">{t("Lake outlines from OpenStreetMap. Tap a lake to pick it.", "Contornos de los lagos de OpenStreetMap. Toque un lago para elegirlo.")}</p></div>
  </div>
</section>

<section class="section">
  <div class="wrap grid" data-reveal-pic>
    <div class="strip-head" data-reveal>
      {section_title("The town the office belongs to", "El pueblo al que pertenece el consultorio")}
      <p>{t("Winter Haven grew on citrus and on its lakes, and the pictures its visitors sent home still look like the view from Cypress Gardens Boulevard. From the city’s archives:", "Winter Haven creció con los cítricos y con sus lagos, y las postales que sus visitantes mandaban a casa todavía se parecen a la vista desde Cypress Gardens Boulevard. De los archivos de la ciudad:")}</p>
    </div>
    <div class="strip">
      <figure>{pic("assets/sunset-lake-howard-winter-haven-fl.jpg", "Sunset over Lake Howard, Winter Haven, with a fisherman on a dock", 1024, 683, "pic lake")}<figcaption>{t("Lake Howard at sunset, eight miles up the chain.", "Lake Howard al atardecer, a ocho millas por la cadena.")}</figcaption></figure>
      <figure>{pic("assets/florida-citrus-queen-sally-ardrey-and-her.jpg", "The 1955 Florida Citrus Queen and her court on a stage of oranges, Winter Haven", 1200, 950, "pic lake")}<figcaption>{t("The Florida Citrus Exposition, Winter Haven, 1955.", "La Exposición de Cítricos de Florida, Winter Haven, 1955.")}</figcaption></figure>
      <figure>{pic("assets/the-orange-blossom-special-going-through-orange.jpg", "Vintage postcard of the Orange Blossom Special train passing orange groves", 1024, 648, "pic lake")}<figcaption>{t("The Orange Blossom Special through the groves, 1940s.", "El Orange Blossom Special entre los naranjales, años 40.")}</figcaption></figure>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap grid">
    <div class="faq-head" data-reveal>
      {section_title("Questions people ask first", "Lo que la gente pregunta primero")}
    </div>
    <div class="cards">{faq_cards(FAQS)}</div>
  </div>
</section>

{coupon()}
'''

# =================================================================== SERVICES
def services():
    rows = ''
    photos = ['assets/jacaranda-apartments-winter-haven-florida.jpg', 'assets/cypress-gardens-41115552574.jpg', 'assets/the-orange-blossom-special-going-through-orange.jpg']
    alts = ['Vintage postcard of the Jacaranda Apartments, Winter Haven', 'The gardens and gazebo at Cypress Gardens, Winter Haven', 'Vintage postcard of the Orange Blossom Special train passing orange groves']
    for i, (key, tone, name, fact, lead, items) in enumerate(SERVICES):
        li = ''.join(f'<li>{t(*x)}</li>' for x in items)
        more = f'<a class="btn btn-paper" href="sleep-apnea.html">{t("The sleep apnea page", "La página de apnea del sueño")}</a>' if key == 'sleep' else ''
        rows += f'''
<section class="row grid" id="{key}" data-reveal>
  <div class="row-text" data-reveal>
    <h2 class="h2">{t(*name)}</h2>
    <p class="lead muted">{t(*lead)}</p>
    <ul class="lakes">{li}</ul>
    <div class="btn-row"><a class="btn" href="contact.html">{t("Ask about this care", "Consultar sobre esto")}</a>{more}</div>
  </div>
  <div class="row-art"><div class="tile-art {tone} lake">{ART[key]}</div></div>
</section>'''
    return f'''
<section class="wrap grid page-head">
  <h1 class="h1" data-rise style="--i:0">{t("Everything a smile needs", "Todo lo que una sonrisa necesita")}</h1>
  <p class="lead muted" data-rise style="--i:1">{t("From routine cleanings to full‑mouth reconstruction, planned by a prosthodontist and a general dentist in the same office, so you are not sent somewhere else for the next step.", "De limpiezas de rutina a reconstrucción de boca completa, planeado por un prostodoncista y un dentista general en el mismo consultorio, para que no lo manden a otro lugar para el siguiente paso.")}</p>
  {pic(photos[0], alts[0], 1024, 646, 'pic pic-tall lake shutter drift', lazy=False)}
</section>
<div class="wrap section">
{rows}
</div>
<section class="section field-surface">
  <div class="wrap grid two" data-reveal>
    <div>
      {section_title("Pictures of the same town", "Imágenes del mismo pueblo")}
      <p class="lead muted">{t("Cypress Gardens opened on Lake Eloise in 1936 and made the chain of lakes famous. The boulevard that carried visitors there is the one the office is on today.", "Cypress Gardens abrió en Lake Eloise en 1936 e hizo famosa la cadena de lagos. El bulevar que llevaba a los visitantes es el mismo donde hoy está el consultorio.")}</p>
    </div>
    <div class="grid" style="grid-template-columns:1fr 1fr;gap:var(--gutter);align-items:end">
      {pic(photos[1], alts[1], 1920, 1228)}
      {pic(photos[2], alts[2], 1024, 648)}
      {pic('assets/sierra-court-motel-winter-haven-florida.jpg', 'Vintage night postcard of the Sierra Court Motel, Winter Haven', 1024, 652)}
    </div>
  </div>
</section>
{cta_band()}
'''

# =================================================================== SLEEP APNEA
def sleep():
    steps = [
        (('A sleep study', 'Un estudio del sueño'), ('Your physician or a sleep lab confirms obstructive sleep apnea and how severe it is. If you already have a diagnosis, bring it.', 'Su médico o un laboratorio del sueño confirma la apnea obstructiva y su gravedad. Si ya tiene un diagnóstico, tráigalo.')),
        (('Impressions', 'Impresiones'), ('Dr. Polo takes digital impressions of your teeth and records how far forward your jaw can comfortably sit.', 'El Dr. Polo toma impresiones digitales de sus dientes y registra qué tan adelante puede quedar cómodamente su mandíbula.')),
        (('Fitting', 'Ajuste'), ('The appliance is made for you and fitted in the office. Two thin trays, joined, that you wear only at night.', 'El aparato se fabrica para usted y se ajusta en el consultorio. Dos férulas delgadas, unidas, que usa solo de noche.')),
        (('Adjustments', 'Ajustes'), ('Small advances over a few weeks until snoring stops and sleep improves, then a check once a year.', 'Pequeños avances durante algunas semanas hasta que el ronquido pare y el sueño mejore, y luego una revisión al año.')),
    ]
    step_html = ''.join(f'<div><h3>{t(*h)}</h3><p>{t(*p)}</p></div>' for h, p in steps)
    faqs = [
        (('Who', 'Quién'), ('Who is it for?', '¿Para quién es?'), ('Adults with mild to moderate obstructive sleep apnea, people who snore, and CPAP users who cannot tolerate the mask. Severe apnea usually still needs CPAP; the appliance can sometimes be combined with it.', 'Adultos con apnea obstructiva leve a moderada, personas que roncan y usuarios de CPAP que no toleran la máscara. La apnea severa suele seguir necesitando CPAP; a veces el aparato se combina con él.')),
        (('Comfort', 'Comodidad'), ('Is it comfortable?', '¿Es cómodo?'), ('It is custom made from impressions of your own teeth, so it fits like a night guard. Most people stop noticing it within two weeks.', 'Se hace a medida con impresiones de sus propios dientes, así que se siente como un protector nocturno. La mayoría deja de notarlo en dos semanas.')),
        (('Cost', 'Costo'), ('Is it covered?', '¿Lo cubre el seguro?'), ('Oral appliances for diagnosed sleep apnea are often covered by medical insurance rather than dental. The front desk will check with your plan before anything is made.', 'Los aparatos bucales para apnea diagnosticada suelen estar cubiertos por el seguro médico y no el dental. La recepción lo verifica con su plan antes de fabricar nada.')),
    ]
    return f'''
<section class="wrap grid page-head">
  <h1 class="h1" data-rise style="--i:0">{t("Sleep without the mask", "Dormir sin la máscara")}</h1>
  <p class="lead muted" data-rise style="--i:1">{t("A custom dental sleep device, fitted by a prosthodontist, keeps your airway open at night. Far more comfortable than CPAP, no surgery, nothing to plug in.", "Un dispositivo dental a medida, ajustado por un prostodoncista, mantiene su vía aérea abierta de noche. Mucho más cómodo que el CPAP, sin cirugía, sin enchufes.")}</p>
  {pic('assets/sunset-lake-howard-winter-haven-fl.jpg', 'Sunset over Lake Howard, Winter Haven, with a fisherman on a dock', 1024, 683, 'pic pic-tall lake shutter drift', lazy=False)}
</section>

<section class="section night">
  <div class="wrap grid two" data-reveal>
    <div>
      {section_title("What the appliance does", "Qué hace el aparato")}
      <p class="lead muted">{t("Obstructive sleep apnea happens when the tongue and soft tissue fall back and close the airway. The appliance holds the lower jaw a few millimetres forward, so the airway stays open and the snoring stops.", "La apnea obstructiva ocurre cuando la lengua y el tejido blando caen hacia atrás y cierran la vía aérea. El aparato sostiene la mandíbula unos milímetros hacia adelante, así la vía aérea queda abierta y el ronquido para.")}</p>
      <ul class="lakes" style="margin-top:1.5rem">
        <li>{t("Two thin custom trays, joined, worn only at night", "Dos férulas delgadas a medida, unidas, solo de noche")}</li>
        <li>{t("Quiet: no pump, no hose, no mask", "Silencioso: sin bomba, sin manguera, sin máscara")}</li>
        <li>{t("Fits in a pocket for travel", "Cabe en un bolsillo para viajar")}</li>
        <li>{t("Adjustable in small steps until it works", "Ajustable en pasos pequeños hasta que funcione")}</li>
      </ul>
    </div>
    <div class="tile-art lake" style="background:var(--lake);aspect-ratio:0.7;padding:16%;width:72%;margin-inline:auto">{ART['sleep'].replace(INK, '#f4f1ea')}</div>
  </div>
</section>

<section class="section">
  <div class="wrap grid" data-reveal>
    <div class="flow-head">
      {section_title("How it goes", "Cómo es el proceso")}
      <p class="muted">{t("Four visits over a few weeks, then once a year.", "Cuatro visitas en unas semanas, luego una al año.")}</p>
    </div>
    <div class="flow-steps" style="grid-template-columns:repeat(4,minmax(0,1fr))">{step_html}</div>
  </div>
</section>

<section class="section field-surface">
  <div class="wrap grid">
    <div class="faq-head" data-reveal>{section_title("Before you ask", "Antes de que pregunte")}</div>
    <div class="cards">{faq_cards(faqs)}</div>
  </div>
</section>

<section class="section">
  <div class="wrap grid" data-reveal-pic>
    <div class="strip-head" data-reveal>
      {section_title("Night in Winter Haven", "La noche en Winter Haven")}
      <p>{t("A town built for sleeping well: quiet streets between the lakes, and a motel postcard that promised “a vacation in itself”.", "Un pueblo hecho para dormir bien: calles tranquilas entre los lagos, y una postal de motel que prometía “unas vacaciones en sí mismo”.")}</p>
      <div class="btn-row" style="margin-top:1.5rem"><a class="btn" href="contact.html">{t("Ask about the appliance", "Preguntar por el aparato")}</a></div>
    </div>
    <div class="strip">
      <figure>{pic('assets/sierra-court-motel-winter-haven-florida.jpg', 'Vintage night postcard of the Sierra Court Motel, Winter Haven, under a full moon', 1024, 652, 'pic lake')}<figcaption>{t("The Sierra Court Motel by moonlight, 1950s.", "El Sierra Court Motel a la luz de la luna, años 50.")}</figcaption></figure>
      <figure>{pic('assets/hartman-litho-sales-co-ig4-e-8595.jpg', 'Vintage postcard of Gardenia Lane in Idylwild Gardens, Winter Haven', 1920, 1209, 'pic lake')}<figcaption>{t("Gardenia Lane, Idylwild Gardens.", "Gardenia Lane, Idylwild Gardens.")}</figcaption></figure>
      <figure>{pic('assets/jacaranda-apartments-winter-haven-florida.jpg', 'Vintage postcard of the Jacaranda Apartments, Winter Haven', 1024, 646, 'pic lake')}<figcaption>{t("The Jacaranda Apartments, 1940s.", "Los Jacaranda Apartments, años 40.")}</figcaption></figure>
    </div>
  </div>
</section>
{cta_band('Tired of the mask?', '¿Cansado de la máscara?')}
'''

# =================================================================== DOCTORS
def doctors():
    return f'''
<section class="wrap grid page-head">
  <h1 class="h1" data-rise style="--i:0">{t("The two doctors", "Los dos doctores")}</h1>
  <p class="lead muted" data-rise style="--i:1">{t("A prosthodontist who rebuilds, and a general dentist who keeps everything healthy. Between them, every treatment the office offers, in English, Spanish and German.", "Un prostodoncista que reconstruye, y un dentista general que mantiene todo sano. Entre los dos, todos los tratamientos del consultorio, en español, inglés y alemán.")}</p>
  {pic('assets/cypress-gardens-florida-26975314327.jpg', 'A boat on the canal through the flower beds of Cypress Gardens', 1920, 1205, 'pic pic-tall lake shutter drift', lazy=False)}
</section>

<div class="wrap section">
<section class="doc grid" id="polo" data-reveal>
  <figure class="doc-portrait">
    <div class="pic lake"><img src="assets/florida-citrus-queen-sally-ardrey-and-her.jpg" alt="The 1955 Florida Citrus Queen and her court on a stage of oranges at the Florida Citrus Exposition, Winter Haven" width="1200" height="950" loading="lazy"></div>
    <figcaption>{t("Portrait to be supplied by the office. Shown: the Florida Citrus Exposition, Winter Haven, 1955.", "Retrato a entregar por el consultorio. En la imagen: la Exposición de Cítricos de Florida, Winter Haven, 1955.")}</figcaption>
  </figure>
  <div class="doc-text" data-reveal>
    <h2 class="h2">Dr. Carlos A. Polo, DDS, MS</h2>
    <p class="role">{t("Prosthodontist", "Prostodoncista")}</p>
    <div class="body">
      <p>{t("Dr. Polo trained at the Universidad Francisco Marroquín School of Dentistry in Guatemala City and received his D.D.S. with cum laude honors in 2003. He went on to specialty training in prosthodontics, the branch of dentistry that replaces and rebuilds teeth: crowns and bridges, complete and partial dentures, implant restorations and full‑mouth reconstruction.", "El Dr. Polo se formó en la Facultad de Odontología de la Universidad Francisco Marroquín, en la Ciudad de Guatemala, y recibió su D.D.S. con honores cum laude en 2003. Continuó con la especialidad en prostodoncia, la rama de la odontología que reemplaza y reconstruye dientes: coronas y puentes, prótesis completas y parciales, restauraciones sobre implantes y reconstrucción de boca completa.")}</p>
      <p>{t("Patients describe him the same way in review after review: he explains everything he is doing and why, before he does it. He also fits custom oral appliances for sleep apnea.", "Los pacientes lo describen igual, opinión tras opinión: explica todo lo que hace y por qué, antes de hacerlo. También ajusta aparatos bucales a medida para la apnea del sueño.")}</p>
    </div>
    <ul class="lakes">
      <li>{t("D.D.S., cum laude, Universidad Francisco Marroquín, 2003", "D.D.S., cum laude, Universidad Francisco Marroquín, 2003")}</li>
      <li>{t("M.S. and specialty training in prosthodontics", "M.S. y especialidad en prostodoncia")}</li>
      <li>{t("Languages: English, Spanish, German", "Idiomas: inglés, español, alemán")}</li>
    </ul>
  </div>
</section>

<section class="doc grid" id="cruz" data-reveal>
  <figure class="doc-portrait">
    <div class="pic lake"><img src="assets/the-orange-blossom-special-going-through-orange.jpg" alt="Vintage postcard of the Orange Blossom Special train passing orange groves in Florida" width="1024" height="648" loading="lazy"></div>
    <figcaption>{t("Portrait to be supplied by the office. Shown: a 1940s postcard of the Orange Blossom Special.", "Retrato a entregar por el consultorio. En la imagen: una postal de los años 40 del Orange Blossom Special.")}</figcaption>
  </figure>
  <div class="doc-text" data-reveal>
    <h2 class="h2">Dr. Jose G. Cruz, DDS</h2>
    <p class="role">{t("General dentist, co‑founder", "Dentista general, cofundador")}</p>
    <div class="body">
      <p>{t("Dr. Cruz co‑founded Dental Solutions of Winter Haven. He practices the whole of general dentistry, checkups, fillings, root canals, extractions, and places and restores implants, for children and adults, in English and Spanish.", "El Dr. Cruz cofundó Dental Solutions of Winter Haven. Ejerce toda la odontología general, revisiones, empastes, conductos, extracciones, y coloca y restaura implantes, para niños y adultos, en español e inglés.")}</p>
      <p>{t("Patients call him kind and compassionate, which is the part of dentistry no school teaches.", "Los pacientes lo llaman amable y compasivo, que es la parte de la odontología que ninguna escuela enseña.")}</p>
    </div>
    <ul class="lakes">
      <li>{t("D.D.S., general dentistry", "D.D.S., odontología general")}</li>
      <li>{t("Implant placement and restoration", "Colocación y restauración de implantes")}</li>
      <li>{t("Languages: English, Spanish", "Idiomas: inglés, español")}</li>
    </ul>
  </div>
</section>
</div>

<section class="section field-surface">
  <div class="wrap grid two" data-reveal>
    <div>
      {section_title("Why two doctors matter", "Por qué importan dos doctores")}
      <p class="lead muted">{t("Most offices refer crowns, dentures and implant work out to a specialist across town. Here the specialist is down the hall, so one plan covers everything and nobody repeats your X‑rays.", "La mayoría de los consultorios remiten coronas, prótesis e implantes a un especialista al otro lado del pueblo. Aquí el especialista está en el pasillo, así que un solo plan lo cubre todo y nadie repite sus radiografías.")}</p>
      {pic('assets/winter-haven-legoland-florida-island-in-the.jpg', 'Lake Eloise seen from above, with the far shore and summer clouds', 1920, 1402, 'pic lake pic-inline')}
    </div>
    <div>
      <dl class="facts">
        <div><dt>{t("Prosthodontist", "Prostodoncista")}</dt><dd>{t("A dentist with two to three extra years of specialty training in replacing and rebuilding teeth. There are fewer than 4,000 in the United States.", "Un dentista con dos a tres años extra de especialidad en reemplazar y reconstruir dientes. Hay menos de 4.000 en Estados Unidos.")}</dd></div>
        <div><dt>{t("General dentist", "Dentista general")}</dt><dd>{t("Your first stop for everything: prevention, diagnosis, fillings, root canals, extractions and children.", "Su primera parada para todo: prevención, diagnóstico, empastes, conductos, extracciones y niños.")}</dd></div>
        <div><dt>{t("Together", "Juntos")}</dt><dd>{t("One record, one plan, one bill, in your language.", "Un expediente, un plan, una cuenta, en su idioma.")}</dd></div>
      </dl>
    </div>
  </div>
</section>
{cta_band()}
'''

# =================================================================== REVIEWS
def reviews():
    quotes = ''.join(f'<blockquote class="mark"><p>{t(*q)}</p><footer>{name}</footer></blockquote>' for q, name in QUOTES)
    return f'''
<section class="wrap grid page-head">
  <h1 class="h1" data-rise style="--i:0">{t("What patients say", "Lo que dicen los pacientes")}</h1>
  <p class="lead muted" data-rise style="--i:1">{t("Dental Solutions of Winter Haven holds 4.9 stars on Google from more than 260 reviews. These are a few, shortened, from public review sites.", "Dental Solutions of Winter Haven tiene 4,9 estrellas en Google con más de 260 opiniones. Estas son algunas, acortadas, de sitios públicos de opiniones.")}</p>
  {pic('assets/jacaranda-apartments-winter-haven-florida.jpg', 'Vintage postcard of the Jacaranda Apartments, Winter Haven', 1024, 646, 'pic pic-tall lake shutter drift', lazy=False)}
</section>
<section class="section">
  <div class="wrap">
    <div class="board" data-reveal>
      <div class="mark mark-head"><h2 class="h2">{t("4.9 stars on Google", "4,9 estrellas en Google")}</h2><p>{t("More than 260 reviews", "Más de 260 opiniones")}</p></div>
      {quotes}
      <div class="mark mark-pic lake"><img src="assets/hartman-litho-sales-co-ig4-e-8595.jpg" alt="Vintage postcard of Gardenia Lane in Idylwild Gardens, Winter Haven" width="1920" height="1209" loading="lazy"></div>
      <div class="mark mark-pic lake"><img src="assets/florida-citrus-queen-sally-ardrey-and-her.jpg" alt="The 1955 Florida Citrus Queen and her court on a stage of oranges, Winter Haven" width="1200" height="950" loading="lazy"></div>
    </div>
  </div>
</section>
<section class="section field-surface">
  <div class="wrap grid two" data-reveal>
    <div>
      {section_title("Been a patient?", "¿Ha sido paciente?")}
      <p class="lead muted">{t("A short review helps the next family find the office. It takes a minute on Google.", "Una opinión corta ayuda a la siguiente familia a encontrar el consultorio. Toma un minuto en Google.")}</p>
      <div class="btn-row"><a class="btn" href="{REVIEW}" target="_blank" rel="noopener">{t("Leave a Google review", "Dejar una opinión en Google")}</a></div>
    </div>
    <div>
      {section_title("New here?", "¿Nuevo aquí?")}
      <p class="lead muted">{t("Your first visit is an exam and a conversation about options and cost, nothing more. Nobody will lecture you, however long it has been.", "Su primera visita es un examen y una conversación sobre opciones y costo, nada más. Nadie lo va a regañar, por mucho tiempo que haya pasado.")}</p>
      <div class="btn-row"><a class="btn btn-ink" href="contact.html">{t("Book a first visit", "Reservar primera visita")}</a></div>
      {pic('assets/cypress-gardens-florida-26975314327.jpg', 'A boat on the canal through the flower beds of Cypress Gardens', 1920, 1205, 'pic lake pic-inline')}
    </div>
  </div>
</section>
{cta_band()}
'''

# =================================================================== CONTACT
def contact():
    return f'''
<section class="wrap grid page-head">
  <h1 class="h1" data-rise style="--i:0">{t("Book a visit or ask a question", "Reserve una cita o pregunte")}</h1>
  <p class="lead muted" data-rise style="--i:1">{t("Call during office hours, or send the request below and the front desk replies the next business day. Hablamos español. Wir sprechen Deutsch.", "Llame en horario de oficina o envíe la solicitud de abajo y la recepción responde el siguiente día hábil. We speak English. Wir sprechen Deutsch.")}</p>
  <div class="pic pic-tall lake shutter drift" style="grid-column:9/13;grid-row:1/3"><img src="assets/sunset-lake-howard-winter-haven-fl.jpg" alt="Sunset over Lake Howard, Winter Haven" width="1024" height="683"></div>
</section>

<section class="section-tight" id="hours">
  <div class="wrap grid two" data-reveal>
    <div>
      {section_title("Hours and address", "Horario y dirección")}
      <dl class="facts" style="margin-top:1.5rem">
        <div><dt>{t("Today", "Hoy")}</dt><dd><span class="open-now" data-open-now></span></dd></div>
        <div><dt>{t("Hours", "Horario")}</dt><dd>{t("Monday to Thursday, 8 a.m. to 5 p.m.", "Lunes a jueves, 8 a.m. a 5 p.m.")}<br>{t("Friday by appointment. Closed Saturday and Sunday.", "Viernes con cita. Cerrado sábado y domingo.")}</dd></div>
        <div><dt>{t("Address", "Dirección")}</dt><dd>{ADDR1}<br>{ADDR2}</dd></div>
        <div><dt>{t("Phone", "Teléfono")}</dt><dd><a href="{TEL}">{PHONE}</a></dd></div>
        <div><dt>Email</dt><dd><a href="mailto:{MAIL}">{MAIL}</a></dd></div>
        <div><dt>{t("Languages", "Idiomas")}</dt><dd>English · Español · Deutsch</dd></div>
      </dl>
      <div class="btn-row">
        <a class="btn" href="{MAPS}" target="_blank" rel="noopener">{t("Directions", "Cómo llegar")}</a>
        <a class="btn btn-paper" href="{TEL}">{t("Call", "Llamar")} {PHONE}</a>
      </div>
    </div>
    <div class="lake">{tilemap()}</div>
  </div>
</section>

{coupon()}

<section class="section field-surface" id="pay">
  <div class="wrap grid two" data-reveal>
    <div>
      {section_title("Insurance and payment", "Seguros y pagos")}
      <p class="lead muted">{t("Most PPO plans are accepted and filed for you. CareCredit financing is available for larger plans, with a prequalification that does not affect your credit score.", "Se aceptan la mayoría de los planes PPO y el consultorio presenta el reclamo. Hay financiamiento CareCredit para planes grandes, con una precalificación que no afecta su puntaje de crédito.")}</p>
    </div>
    <div>{pay_tiles()}</div>
  </div>
</section>

<section class="section" id="faq">
  <div class="wrap grid">
    <div class="faq-head" data-reveal>{section_title("Questions people ask first", "Lo que la gente pregunta primero")}</div>
    <div class="cards">{faq_cards(FAQS)}</div>
  </div>
</section>
'''

# --------------------------------------------------------------------------- build
TITLES = {
    'index.html': ('Dental Solutions of Winter Haven · Dentists on Cypress Gardens Blvd', 'A prosthodontist and a general dentist in Winter Haven, FL. Family dentistry, crowns, dentures, implants, veneers, sleep apnea appliances and same‑day emergencies. English, Spanish, German.'),
    'services.html': ('Services · Dental Solutions of Winter Haven', 'Family and general dentistry, prosthodontics, cosmetic dentistry, implants and oral surgery, sleep apnea treatment and emergencies in Winter Haven, FL.'),
    'sleep-apnea.html': ('Sleep apnea treatment · Dental Solutions of Winter Haven', 'Custom dental sleep devices fitted by a prosthodontist in Winter Haven, FL. A comfortable alternative to CPAP.'),
    'doctors.html': ('Dr. Carlos A. Polo and Dr. Jose G. Cruz · Dental Solutions of Winter Haven', 'Meet the prosthodontist and the general dentist of Dental Solutions of Winter Haven, FL.'),
    'reviews.html': ('Reviews · Dental Solutions of Winter Haven', 'What patients say about Dental Solutions of Winter Haven: 4.9 stars on Google.'),
    'contact.html': ('Contact and hours · Dental Solutions of Winter Haven', 'Book a visit at 6390 Cypress Gardens Blvd, Winter Haven, FL 33884. Call (863) 324‑7121. Monday to Thursday 8 to 5.'),
}
BODIES = {'index.html': home, 'services.html': services, 'sleep-apnea.html': sleep, 'doctors.html': doctors, 'reviews.html': reviews, 'contact.html': contact}

if __name__ == '__main__':
    for f, _, _ in PAGES:
        title, desc = TITLES[f]
        html = head(title, desc) + header(f) + BODIES[f]() + footer()
        (ROOT / f).write_text(html, encoding='utf-8')
        print('wrote', f, len(html), 'bytes')
