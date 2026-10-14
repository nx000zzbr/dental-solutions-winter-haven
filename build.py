#!/usr/bin/env python3
"""Generates the six pages of the Dental Solutions of Winter Haven site (version 2, the conventional layout)
from one set of shared parts. Run `python3 build.py` after editing; the .html files are the output."""
import json, pathlib

ROOT = pathlib.Path(__file__).parent
LAKES = json.load(open(ROOT / 'assets/data/lakes.json'))
CREDITS = json.load(open(ROOT / 'assets/credits.json'))

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
CUR = ' aria-current="page"'

PAGES = [
    ('index.html', 'Home', 'Inicio'),
    ('services.html', 'Services', 'Servicios'),
    ('sleep-apnea.html', 'Sleep apnea', 'Apnea del sueño'),
    ('doctors.html', 'Doctors', 'Doctores'),
    ('reviews.html', 'Reviews', 'Opiniones'),
    ('contact.html', 'Contact', 'Contacto'),
]

# --------------------------------------------------------------------------- small icons
I = {
    'phone': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.9 2.1z"/></svg>',
    'clock': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>',
    'pin': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 10c0 7-9 13-9 13S3 17 3 10a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
    'globe': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 0 1 4 10 15 15 0 0 1-4 10 15 15 0 0 1-4-10 15 15 0 0 1 4-10z"/></svg>',
    'check': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>',
    'star': '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z"/></svg>',
    'mail': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>',
    'tooth': '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M7.5 3C9 3 10 4 12 4s3-1 4.5-1C19.5 3 21 5.5 21 8c0 2-1 3.5-1.5 5-.6 2-1 6-2.5 8-1 1.3-2 .3-2.3-1-.4-1.8-.7-4-2.7-4s-2.3 2.2-2.7 4c-.3 1.3-1.3 2.3-2.3 1C5.5 19 5.1 15 4.5 13 4 11.5 3 10 3 8c0-2.5 1.5-5 4.5-5z"/></svg>',
    'moon': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>',
    'alert': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 9v4M12 17h.01M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z"/></svg>',
}
def check(): return f'<span class="check">{I["check"]}</span>'
def stars(): return '<span class="stars" aria-label="5 stars">' + I['star'] * 5 + '</span>'
def checklist(items, cols=False):
    return f'<ul class="checks{" checks-2" if cols else ""}">' + ''.join(f'<li>{check()}<span>{t(*x) if isinstance(x, tuple) else x}</span></li>' for x in items) + '</ul>'

INK, LAKE, PAPER, CYP = '#10282b', '#146b73', '#f4f1ea', '#3f7a4a'
ART = {
    'general': f'<svg viewBox="0 0 100 100" aria-hidden="true"><path d="M30 12c10-6 30-6 40 0 12 7 14 24 8 38-3 7-4 20-6 30-1 6-7 7-9 1-2-6-3-16-7-16s-5 10-7 16c-2 6-8 5-9-1-2-10-3-23-6-30-6-14-4-31 6-38z" fill="{INK}"/><path d="M38 24c6-4 18-4 24 0" fill="none" stroke="{PAPER}" stroke-width="5" stroke-linecap="round"/></svg>',
    'prostho': f'<svg viewBox="0 0 160 100" aria-hidden="true"><path d="M22 58h116v10c0 14-26 24-58 24S22 82 22 68z" fill="{INK}"/><path d="M34 56c4-22 18-36 46-36s42 14 46 36c-14 6-30 9-46 9s-32-3-46-9z" fill="{LAKE}"/><path d="M50 55c2-12 12-22 30-22s28 10 30 22" fill="none" stroke="{PAPER}" stroke-width="5" stroke-linecap="round"/><rect x="60" y="66" width="40" height="8" rx="4" fill="{PAPER}"/></svg>',
    'cosmetic': f'<svg viewBox="0 0 100 100" aria-hidden="true"><path d="M28 10h44c4 0 6 3 6 7l-6 54c-2 14-10 21-22 21S30 85 28 71L22 17c0-4 2-7 6-7z" fill="{INK}"/><path d="M34 16h20c2 0 3 2 3 4l-4 50c-1 9-4 13-9 13" fill="{LAKE}"/></svg>',
    'implants': f'<svg viewBox="0 0 100 100" aria-hidden="true"><path d="M26 10h48c4 0 6 3 5 7l-5 20H26l-5-20c-1-4 1-7 5-7z" fill="{INK}"/><path d="M38 40h24l-3 10H41zM40 54h20l-3 10H43zM42 68h16l-3 10H45zM44 82h12l-6 10z" fill="{LAKE}"/></svg>',
    'sleep': f'<svg viewBox="0 0 100 100" aria-hidden="true"><path d="M14 36c0-10 8-16 36-16s36 6 36 16-8 14-36 14-36-4-36-14z" fill="{INK}"/><path d="M14 64c0 10 8 16 36 16s36-6 36-16-8-14-36-14-36 4-36 14z" fill="{LAKE}"/><rect x="20" y="46" width="12" height="8" rx="2" fill="{INK}"/><rect x="68" y="46" width="12" height="8" rx="2" fill="{INK}"/></svg>',
    'emergency': f'<svg viewBox="0 0 100 100" aria-hidden="true"><path d="M30 12c10-6 30-6 40 0 12 7 14 24 8 38-3 7-4 20-6 30-1 6-7 7-9 1-2-6-3-16-7-16s-5 10-7 16c-2 6-8 5-9-1-2-10-3-23-6-30-6-14-4-31 6-38z" fill="{INK}"/><path d="M52 14l-10 30h12l-8 30 24-38H56l8-22z" fill="{PAPER}"/></svg>',
}


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



def schema():
    data = {"@context": "https://schema.org", "@type": "Dentist", "name": "Dental Solutions of Winter Haven",
            "url": "https://www.dentalsolutionsofwh.com/", "telephone": "+1-863-324-7121", "email": MAIL,
            "address": {"@type": "PostalAddress", "streetAddress": ADDR1, "addressLocality": "Winter Haven", "addressRegion": "FL", "postalCode": "33884", "addressCountry": "US"},
            "geo": {"@type": "GeoCoordinates", "latitude": 27.9825809, "longitude": -81.6782343},
            "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday"], "opens": "08:00", "closes": "17:00"}],
            "employee": [{"@type": "Person", "name": "Dr. Carlos A. Polo", "jobTitle": "Prosthodontist"}, {"@type": "Person", "name": "Dr. Jose G. Cruz", "jobTitle": "Dentist"}],
            "knowsLanguage": ["en", "es", "de"], "paymentAccepted": "Cash, Check, Visa, Mastercard, American Express, Discover, CareCredit"}
    return json.dumps(data, ensure_ascii=False)

FAVICON = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%23146b73'/%3E%3Cpath d='M22 14c4 0 7 3 10 3s6-3 10-3c7 0 11 6 11 12 0 5-2.5 8.5-4 12-1.5 5-2.5 14-6 18-2.5 3-5 1-5.7-2.5-1-4.5-1.8-9.5-5.3-9.5s-4.3 5-5.3 9.5C26 57 23.5 59 21 56c-3.5-4-4.5-13-6-18-1.5-3.5-4-7-4-12 0-6 4-12 11-12z' fill='%23fff'/%3E%3C/svg%3E"

def head(title, desc):
    return f'''<!doctype html>
<html lang="en" data-lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#15282b">
<meta name="color-scheme" content="light">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:locale" content="en_US">
<meta property="og:locale:alternate" content="es_US">
<script type="application/ld+json">{schema()}</script>
<script>document.documentElement.classList.add('js');try{{var l=localStorage.getItem('dswh-lang');if(l==='es'||l==='en'){{document.documentElement.dataset.lang=l;document.documentElement.lang=l;}}}}catch(e){{}}</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="icon" href="{FAVICON}">
<link rel="stylesheet" href="styles.css">
</head>
<body>
<a class="skip" href="#main">{t("Skip to content", "Ir al contenido")}</a>
'''

def logo(cls=''):
    return f'<a class="logo {cls}" href="index.html" aria-label="Dental Solutions of Winter Haven, home"><span class="logo-mark">{I["tooth"]}</span><span><b>Dental Solutions</b><small>of Winter Haven</small></span></a>'

def header(current):
    links = ''.join(f'<a href="{f}"{CUR if f == current else ""}>{t(en, es)}</a>' for f, en, es in PAGES)
    return f'''<div class="topbar">
  <div class="wrap topbar-row">
    <span><span class="open-now" data-open-now></span><span class="hide-sm"> · {t("Mon–Thu 8 a.m.–5 p.m. · Fri by appointment", "Lun–jue 8 a.m.–5 p.m. · Vie con cita")}</span></span>
    <span class="hide-sm">{ADDR1}, {ADDR2}</span>
    <span class="spacer hide-md">English · Español · Deutsch</span>
    <button class="lang" id="lang" type="button" aria-label="Cambiar idioma / Change language">{t("Español", "English")}</button>
  </div>
</div>
<header class="header">
  <div class="wrap header-row">
    {logo()}
    <nav class="nav" id="menu" aria-label="Main">{links}</nav>
    <div class="header-actions">
      <a class="header-phone" href="{TEL}">{PHONE}</a>
      <a class="btn" href="contact.html#request">{t("Book a visit", "Reservar cita")}</a>
      <button class="burger" id="burger" type="button" aria-expanded="false" aria-controls="menu">{t("Menu", "Menú")}</button>
    </div>
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
    pages = ''.join(f'<li><a href="{f}">{t(en, es)}</a></li>' for f, en, es in PAGES)
    return f'''</main>
<footer class="footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        {logo()}
        <p>{t("A prosthodontist and a general dentist on Cypress Gardens Boulevard, Winter Haven. Family, cosmetic and restorative dentistry, implants, sleep apnea appliances and same‑day emergencies.", "Un prostodoncista y un dentista general en Cypress Gardens Boulevard, Winter Haven. Odontología familiar, estética y restauradora, implantes, aparatos para apnea del sueño y urgencias el mismo día.")}</p>
        <p style="margin-top:0.75rem">English · Español · Deutsch</p>
      </div>
      <div><h4>{t("Pages", "Páginas")}</h4><ul>{pages}</ul></div>
      <div><h4>{t("Services", "Servicios")}</h4><ul>
        <li><a href="services.html#general">{t("Family dentistry", "Odontología familiar")}</a></li>
        <li><a href="services.html#prostho">{t("Crowns, bridges and dentures", "Coronas, puentes y prótesis")}</a></li>
        <li><a href="services.html#cosmetic">{t("Cosmetic dentistry", "Odontología estética")}</a></li>
        <li><a href="services.html#implants">{t("Implants and oral surgery", "Implantes y cirugía oral")}</a></li>
        <li><a href="sleep-apnea.html">{t("Sleep apnea treatment", "Tratamiento de apnea del sueño")}</a></li>
        <li><a href="services.html#emergency">{t("Emergencies", "Urgencias")}</a></li>
      </ul></div>
      <div><h4>{t("Contact", "Contacto")}</h4><ul>
        <li>{ADDR1}<br>{ADDR2}</li>
        <li><a href="{TEL}">{PHONE}</a></li>
        <li><a href="mailto:{MAIL}">{MAIL}</a></li>
        <li>{t("Monday to Thursday, 8 a.m. to 5 p.m.", "Lunes a jueves, 8 a.m. a 5 p.m.")}<br>{t("Friday by appointment", "Viernes con cita")}</li>
        <li><a href="{MAPS}" target="_blank" rel="noopener">{t("Get directions", "Cómo llegar")} →</a></li>
      </ul></div>
    </div>
    <p class="credits">{t("Pictures of Winter Haven and Central Florida, used with thanks:", "Imágenes de Winter Haven y Florida Central, usadas con agradecimiento:")} {credits_line()}. {t("Map", "Mapa")} © OpenStreetMap contributors (ODbL). {t("None of the pictures shows the office itself.", "Ninguna imagen muestra el consultorio en sí.")}</p>
    <div class="footer-bottom">
      <span>© 2026 Dental Solutions of Winter Haven, PLC</span>
      <span>{t("Website proposal", "Propuesta de sitio web")} · <a href="v1/index.html">{t("See version 1", "Ver versión 1")}</a></span>
    </div>
  </div>
</footer>
<script src="main.js"></script>
</body>
</html>
'''

def page_head(crumb, h1, lead, extra=''):
    return f'''<section class="page-head">
  <div class="wrap">
    <p class="crumbs"><a href="index.html">{t("Home", "Inicio")}</a> › {t(*crumb)}</p>
    <h1 class="h1">{t(*h1)}</h1>
    <p class="lead">{t(*lead)}</p>
    {extra}
  </div>
</section>'''

def cta_band(en_h='Ready to book a visit?', es_h='¿Listo para reservar una cita?'):
    return f'''<section class="section band">
  <div class="wrap band-row">
    <div>
      <h2 class="h2">{t(en_h, es_h)}</h2>
      <p>{t("Call during office hours, or send a request and the front desk will get back to you the next business day. Same‑day times are kept for emergencies.", "Llame en horario de oficina o envíe una solicitud y la recepción le responde el siguiente día hábil. Se reservan horas del mismo día para urgencias.")}</p>
    </div>
    <div class="btn-row">
      <a class="btn btn-white btn-lg" href="contact.html#request">{t("Request an appointment", "Solicitar una cita")}</a>
      <a class="btn btn-ghost-white btn-lg" href="{TEL}">{I["phone"]} {PHONE}</a>
    </div>
  </div>
</section>'''

def faq_list(items, open_first=True):
    out = ''
    for i, (tab, q, a) in enumerate(items):
        out += f'<details class="faq" name="faq"{" open" if (i == 0 and open_first) else ""}><summary>{t(*q)}</summary><div class="answer"><p>{t(*a)}</p></div></details>'
    return out

def tilemap():
    g = json.load(open(ROOT / 'assets/map/grid.json'))
    tiles = ''.join(f'<img src="assets/map/{g["z"]}-{x}-{y}.png" width="256" height="256" alt="" loading="lazy">' for y in g['rows'] for x in g['cols'])
    return (f'<div class="tilemap" role="img" aria-label="Map of 6390 Cypress Gardens Boulevard, Winter Haven"><div class="tilemap-grid">{tiles}</div>'
            f'<span class="tilemap-pin" style="left:{g["marker"][0]*100:.2f}%;top:{g["marker"][1]*100:.2f}%"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 0a8.5 8.5 0 0 0-8.5 8.5C3.5 15 12 24 12 24s8.5-9 8.5-15.5A8.5 8.5 0 0 0 12 0zm0 12a3.5 3.5 0 1 1 0-7 3.5 3.5 0 0 1 0 7z"/></svg></span></div>')

def lake_options():
    opts = ''.join(f'<option value="{l["name"]}" data-km="{l["km"]}">{l["name"]}</option>' for l in sorted(LAKES['lakes'], key=lambda l: l['name']))
    return f'<option value="" data-en="Choose your lake…" data-es="Elija su lago…">Choose your lake…</option>{opts}'

def lake_tool():
    return f'''<div class="card lake-tool">
  <h3 class="h3">{t("How far are you from the office?", "¿Qué tan lejos está del consultorio?")}</h3>
  <p class="muted" style="margin:0.4rem 0 1rem">{t("Winter Haven is a chain of lakes. Pick the lake you live near and see the approximate drive.", "Winter Haven es una cadena de lagos. Elija el lago cerca del que vive y vea el trayecto aproximado.")}</p>
  <label class="sr" for="lake-select">{t("Your lake", "Su lago")}</label>
  <select id="lake-select">{lake_options()}</select>
  <div class="lake-result" id="chain-result" aria-live="polite"><strong>{t("Pick your lake", "Elija su lago")}</strong><span>{t("Distances are approximate, from the middle of the lake to the office.", "Las distancias son aproximadas, del centro del lago al consultorio.")}</span></div>
</div>'''

def request_form(mail=MAIL):
    reasons = [('Cleaning and checkup', 'Limpieza y revisión'), ('Toothache or emergency', 'Dolor o urgencia'), ('Crowns, dentures or implants', 'Coronas, prótesis o implantes'), ('Cosmetic: veneers, whitening', 'Estética: carillas, blanqueamiento'), ('Sleep apnea appliance', 'Aparato para apnea del sueño'), ('Something else', 'Otra cosa')]
    opts = ''.join(f'<option data-en="{en}" data-es="{es}">{en}</option>' for en, es in reasons)
    return f'''<form class="card card-pad-lg" id="contact-form" data-mail="{mail}">
  <h2 class="h2" style="margin-bottom:0.5rem">{t("Request an appointment", "Solicite una cita")}</h2>
  <p class="muted" style="margin-bottom:1.5rem">{t("The front desk replies by phone or email the next business day. For pain today, please call.", "La recepción responde por teléfono o correo el siguiente día hábil. Si tiene dolor hoy, mejor llame.")}</p>
  <div class="form-grid">
    <div class="row-2">
      <div><label for="f-name">{t("Full name", "Nombre completo")}</label><input id="f-name" name="name" type="text" autocomplete="name" required></div>
      <div><label for="f-phone">{t("Phone", "Teléfono")}</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" required></div>
    </div>
    <div><label for="f-reason">{t("Reason for the visit", "Motivo de la visita")}</label><select id="f-reason" name="reason">{opts}</select></div>
    <div><label for="f-msg">{t("Message (optional)", "Mensaje (opcional)")}</label><textarea id="f-msg" name="message"></textarea></div>
    <button class="btn btn-lg btn-block" type="submit">{t("Send the request", "Enviar la solicitud")}</button>
  </div>
  <p class="form-note">{t("The form opens your email app with the message written for you. Nothing is stored on this site.", "El formulario abre su aplicación de correo con el mensaje ya escrito. Este sitio no guarda nada.")}</p>
</form>'''

def service_cards(short=False):
    out = ''
    for key, tone, name, fact, lead, items in SERVICES:
        href = 'sleep-apnea.html' if key == 'sleep' else f'services.html#{key}'
        out += f'<a class="card card-link" href="{href}"><span class="icon">{ART[key]}</span><h3 class="h3">{t(*name)}</h3><p>{t(*fact)}</p><span class="link link-arrow">{t("Learn more", "Más información")}</span></a>'
    return out

def doctor_cards():
    return f'''
<div class="card doctor">
  <div class="doctor-photo"><div><b>CP</b><span>{t("Photo to be supplied", "Foto a entregar")}</span></div></div>
  <div>
    <h3>Dr. Carlos A. Polo, DDS, MS</h3>
    <p class="role">{t("Prosthodontist", "Prostodoncista")}</p>
    <p>{t("Specialist in replacing and rebuilding teeth: crowns, bridges, dentures, implant restorations and full‑mouth reconstruction. Graduated cum laude in 2003. Also fits custom sleep apnea appliances.", "Especialista en reemplazar y reconstruir dientes: coronas, puentes, prótesis, restauraciones sobre implantes y reconstrucción completa. Graduado cum laude en 2003. También ajusta aparatos a medida para apnea del sueño.")}</p>
    <ul class="tags"><li class="tag">English</li><li class="tag">Español</li><li class="tag">Deutsch</li></ul>
    <a class="link link-arrow" href="doctors.html#polo" style="display:inline-block;margin-top:1rem">{t("About Dr. Polo", "Sobre el Dr. Polo")}</a>
  </div>
</div>
<div class="card doctor">
  <div class="doctor-photo"><div><b>JC</b><span>{t("Photo to be supplied", "Foto a entregar")}</span></div></div>
  <div>
    <h3>Dr. Jose G. Cruz, DDS</h3>
    <p class="role">{t("General dentist · Co‑founder", "Dentista general · Cofundador")}</p>
    <p>{t("Checkups, fillings, root canals, extractions and implant placement, for children and adults. Patients describe him as kind and compassionate.", "Revisiones, empastes, conductos, extracciones y colocación de implantes, para niños y adultos. Los pacientes lo describen como amable y compasivo.")}</p>
    <ul class="tags"><li class="tag">English</li><li class="tag">Español</li></ul>
    <a class="link link-arrow" href="doctors.html#cruz" style="display:inline-block;margin-top:1rem">{t("About Dr. Cruz", "Sobre el Dr. Cruz")}</a>
  </div>
</div>'''

def review_cards(n=4):
    return ''.join(f'<blockquote class="card review">{stars()}<p>{t(*q)}</p><footer>{name}<span>{t("Google review", "Opinión en Google")}</span></footer></blockquote>' for q, name in QUOTES[:n])

# =================================================================== HOME
def home():
    return f'''
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <span class="eyebrow">{t("Family dentistry · Winter Haven, FL", "Odontología familiar · Winter Haven, FL")}</span>
      <h1 class="h1">{t("Complete dental care for the whole family, in one office", "Atención dental completa para toda la familia, en un solo consultorio")}</h1>
      <p class="lead">{t("A prosthodontist and a general dentist on Cypress Gardens Boulevard. From cleanings and checkups to crowns, implants and full‑mouth reconstruction, in English, Spanish and German.", "Un prostodoncista y un dentista general en Cypress Gardens Boulevard. De limpiezas y revisiones a coronas, implantes y reconstrucción completa, en español, inglés y alemán.")}</p>
      <div class="btn-row">
        <a class="btn btn-lg" href="contact.html#request">{t("Request an appointment", "Solicitar una cita")}</a>
        <a class="btn btn-outline btn-lg" href="{TEL}">{I["phone"]} {PHONE}</a>
      </div>
      <ul class="hero-badges">
        <li>{check()} {t("4.9 stars on Google", "4,9 estrellas en Google")}</li>
        <li>{check()} {t("Same‑day emergencies", "Urgencias el mismo día")}</li>
        <li>{check()} {t("Most PPO plans accepted", "Mayoría de planes PPO")}</li>
      </ul>
    </div>
    <figure class="hero-pic"><img src="assets/winter-haven-legoland-florida-island-in-the.jpg" alt="Lake Eloise, Winter Haven, seen from above on a summer day" width="1920" height="1402" fetchpriority="high"></figure>
  </div>
</section>

<section class="wrap strip">
  <div class="strip-grid">
    <div class="info"><span class="icon">{I["clock"]}</span><div><strong>{t("Hours", "Horario")}</strong><span class="open-now" data-open-now></span><span>{t("Mon–Thu 8 a.m.–5 p.m. · Fri by appointment", "Lun–jue 8 a.m.–5 p.m. · Vie con cita")}</span></div></div>
    <div class="info"><span class="icon">{I["phone"]}</span><div><strong>{t("Call us", "Llámenos")}</strong><a href="{TEL}">{PHONE}</a><span>{t("Emergencies: call first thing", "Urgencias: llame a primera hora")}</span></div></div>
    <div class="info"><span class="icon">{I["pin"]}</span><div><strong>{t("Address", "Dirección")}</strong><span>{ADDR1}<br>{ADDR2}</span><a href="{MAPS}" target="_blank" rel="noopener">{t("Directions", "Cómo llegar")} →</a></div></div>
    <div class="info"><span class="icon">{I["globe"]}</span><div><strong>{t("Languages", "Idiomas")}</strong><span>English · Español · Deutsch</span><span>{t("From the phone call to the chair", "De la llamada al sillón")}</span></div></div>
  </div>
</section>

<section class="section" id="services">
  <div class="wrap">
    <div class="section-head split">
      <div><span class="eyebrow">{t("Services", "Servicios")}</span><h2 class="h2">{t("Everything a smile needs", "Todo lo que una sonrisa necesita")}</h2><p class="lead">{t("Six areas of care, one office. The prosthodontist plans the restorative work; the general dentist keeps everything else healthy.", "Seis áreas de atención, un solo consultorio. El prostodoncista planea el trabajo restaurador; el dentista general mantiene sano todo lo demás.")}</p></div>
      <a class="btn btn-outline" href="services.html">{t("All services", "Todos los servicios")}</a>
    </div>
    <div class="grid-3">{service_cards()}</div>
  </div>
</section>

<section class="section section-alt">
  <div class="wrap two-col">
    <div>
      <span class="eyebrow">{t("Why patients choose us", "Por qué nos eligen")}</span>
      <h2 class="h2">{t("A specialist and a general dentist, under one roof", "Un especialista y un dentista general, bajo un mismo techo")}</h2>
      <p class="lead" style="margin-top:0.75rem">{t("Most offices refer crowns, dentures and implants to a specialist across town. Here the specialist is down the hall, so one plan covers everything and nobody repeats your X‑rays.", "La mayoría de los consultorios remiten coronas, prótesis e implantes a un especialista al otro lado del pueblo. Aquí el especialista está en el pasillo: un solo plan lo cubre todo y nadie repite sus radiografías.")}</p>
      <div class="btn-row" style="margin-top:1.5rem"><a class="btn" href="doctors.html">{t("Meet the doctors", "Conozca a los doctores")}</a></div>
    </div>
    <div class="grid-2" style="gap:1.25rem">
      <div class="feature"><span class="icon">{I["tooth"]}</span><div><h3>{t("Prosthodontist on staff", "Prostodoncista en el equipo")}</h3><p>{t("Crowns, dentures and implants planned by a specialist with extra years of training.", "Coronas, prótesis e implantes planeados por un especialista con años extra de formación.")}</p></div></div>
      <div class="feature"><span class="icon">{I["globe"]}</span><div><h3>{t("Three languages", "Tres idiomas")}</h3><p>{t("English, Spanish and German, from the front desk to the treatment plan.", "Inglés, español y alemán, de la recepción al plan de tratamiento.")}</p></div></div>
      <div class="feature"><span class="icon">{I["alert"]}</span><div><h3>{t("Same‑day emergencies", "Urgencias el mismo día")}</h3><p>{t("Times are kept open Monday to Thursday for pain that can’t wait.", "Se reservan horas de lunes a jueves para el dolor que no puede esperar.")}</p></div></div>
      <div class="feature"><span class="icon">{I["clock"]}</span><div><h3>{t("Plans with the cost written down", "Planes con el costo por escrito")}</h3><p>{t("Options in order, with what each costs. Nothing starts until you say so.", "Opciones en orden, con lo que cuesta cada una. Nada empieza hasta que usted lo diga.")}</p></div></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head center"><span class="eyebrow">{t("New patients", "Nuevos pacientes")}</span><h2 class="h2">{t("Your first visit, step by step", "Su primera visita, paso a paso")}</h2><p class="lead">{t("About an hour. You leave with a plan you understand and can afford.", "Alrededor de una hora. Sale con un plan que entiende y puede pagar.")}</p></div>
    <div class="steps">
      <div class="step"><h3>{t("Tell us everything", "Cuéntenos todo")}</h3><p>{t("What hurts, what you avoid, what you have been told before. Photographs and digital X‑rays at a fraction of the old dose.", "Qué duele, qué evita, qué le han dicho antes. Fotografías y radiografías digitales con una fracción de la dosis de antes.")}</p></div>
      <div class="step"><h3>{t("One exam, two doctors", "Un examen, dos doctores")}</h3><p>{t("The general dentist checks teeth and gums; the prosthodontist looks at what needs rebuilding.", "El dentista general revisa dientes y encías; el prostodoncista ve lo que hay que reconstruir.")}</p></div>
      <div class="step"><h3>{t("One plan, your decision", "Un plan, su decisión")}</h3><p>{t("Options in order, with costs and what can wait. We check your insurance and financing before anything starts.", "Opciones en orden, con costos y lo que puede esperar. Verificamos su seguro y financiamiento antes de empezar.")}</p></div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="wrap">
    <div class="section-head split">
      <div><span class="eyebrow">{t("Our doctors", "Nuestros doctores")}</span><h2 class="h2">{t("Two doctors, one plan", "Dos doctores, un plan")}</h2></div>
      <a class="btn btn-outline" href="doctors.html">{t("About the doctors", "Sobre los doctores")}</a>
    </div>
    <div class="grid-2">{doctor_cards()}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head split">
      <div><span class="eyebrow">{t("Reviews", "Opiniones")}</span><h2 class="h2">{t("What patients say", "Lo que dicen los pacientes")}</h2><p class="lead">{t("4.9 stars on Google from more than 260 reviews.", "4,9 estrellas en Google con más de 260 opiniones.")}</p></div>
      <a class="btn btn-outline" href="reviews.html">{t("All reviews", "Todas las opiniones")}</a>
    </div>
    <div class="grid-3">{review_cards(3)}</div>
  </div>
</section>

<section class="section section-alt">
  <div class="wrap two-col two-col-start">
    <div>
      <span class="eyebrow">{t("Visit us", "Visítenos")}</span>
      <h2 class="h2">{t("On Cypress Gardens Boulevard", "En Cypress Gardens Boulevard")}</h2>
      <dl class="facts" style="margin-top:1.25rem">
        <div><dt>{t("Address", "Dirección")}</dt><dd>{ADDR1}<br>{ADDR2}</dd></div>
        <div><dt>{t("Hours", "Horario")}</dt><dd>{t("Monday to Thursday, 8 a.m. to 5 p.m.", "Lunes a jueves, 8 a.m. a 5 p.m.")}<br>{t("Friday by appointment · Closed weekends", "Viernes con cita · Cerrado fines de semana")}</dd></div>
        <div><dt>{t("Phone", "Teléfono")}</dt><dd><a href="{TEL}">{PHONE}</a></dd></div>
        <div><dt>Email</dt><dd><a href="mailto:{MAIL}">{MAIL}</a></dd></div>
      </dl>
      <div class="btn-row" style="margin-top:1.5rem">
        <a class="btn" href="{MAPS}" target="_blank" rel="noopener">{t("Get directions", "Cómo llegar")}</a>
        <a class="btn btn-outline" href="contact.html">{t("Contact page", "Página de contacto")}</a>
      </div>
    </div>
    {tilemap()}
  </div>
</section>
{cta_band()}
'''

# =================================================================== SERVICES
def services():
    jump = ''.join(f'<a href="#{key}">{t(*name)}</a>' for key, _, name, _, _, _ in SERVICES)
    rows = ''
    for i, (key, tone, name, fact, lead, items) in enumerate(SERVICES):
        more = f'<a class="btn btn-outline" href="sleep-apnea.html">{t("Sleep apnea page", "Página de apnea del sueño")}</a>' if key == 'sleep' else ''
        art = f'<div class="service-art">{ART[key]}</div>'
        text = f'''<div>
      <h2 class="h2">{t(*name)}</h2>
      <p class="lead" style="margin-top:0.75rem">{t(*lead)}</p>
      {checklist(items, cols=True)}
      <div class="btn-row"><a class="btn" href="contact.html#request">{t("Request an appointment", "Solicitar una cita")}</a>{more}</div>
    </div>'''
        inner = f'{text}{art}' if i % 2 == 0 else f'{art}{text}'
        rows += f'<section class="section{" section-alt" if i % 2 else ""}" id="{key}"><div class="wrap service">{inner}</div></section>'
    return page_head(('Services', 'Servicios'), ('Dental services in Winter Haven', 'Servicios dentales en Winter Haven'),
                     ('From routine cleanings to full‑mouth reconstruction, planned by a prosthodontist and a general dentist in the same office, so you are not sent somewhere else for the next step.', 'De limpiezas de rutina a reconstrucción de boca completa, planeado por un prostodoncista y un dentista general en el mismo consultorio, para que no lo manden a otro lugar para el siguiente paso.'),
                     f'<nav class="jump" aria-label="Service areas">{jump}</nav>') + rows + cta_band()

# =================================================================== SLEEP APNEA
def sleep():
    steps = [
        (('A sleep study', 'Un estudio del sueño'), ('Your physician or a sleep lab confirms obstructive sleep apnea and how severe it is. If you already have a diagnosis, bring it.', 'Su médico o un laboratorio del sueño confirma la apnea obstructiva y su gravedad. Si ya tiene un diagnóstico, tráigalo.')),
        (('Impressions', 'Impresiones'), ('Dr. Polo takes digital impressions of your teeth and records how far forward your jaw can comfortably sit.', 'El Dr. Polo toma impresiones digitales de sus dientes y registra qué tan adelante puede quedar cómodamente su mandíbula.')),
        (('Fitting', 'Ajuste'), ('The appliance is made for you and fitted in the office: two thin trays, joined, worn only at night.', 'El aparato se fabrica para usted y se ajusta en el consultorio: dos férulas delgadas, unidas, solo de noche.')),
        (('Adjustments', 'Ajustes'), ('Small advances over a few weeks until snoring stops and sleep improves, then a check once a year.', 'Pequeños avances durante algunas semanas hasta que el ronquido pare y el sueño mejore, y luego una revisión al año.')),
    ]
    step_html = ''.join(f'<div class="step"><h3>{t(*h)}</h3><p>{t(*p)}</p></div>' for h, p in steps)
    faqs = [
        (('Who', 'Quién'), ('Who is it for?', '¿Para quién es?'), ('Adults with mild to moderate obstructive sleep apnea, people who snore, and CPAP users who cannot tolerate the mask. Severe apnea usually still needs CPAP; the appliance can sometimes be combined with it.', 'Adultos con apnea obstructiva leve a moderada, personas que roncan y usuarios de CPAP que no toleran la máscara. La apnea severa suele seguir necesitando CPAP; a veces el aparato se combina con él.')),
        (('Comfort', 'Comodidad'), ('Is it comfortable?', '¿Es cómodo?'), ('It is custom made from impressions of your own teeth, so it fits like a night guard. Most people stop noticing it within two weeks.', 'Se hace a medida con impresiones de sus propios dientes, así que se siente como un protector nocturno. La mayoría deja de notarlo en dos semanas.')),
        (('Cost', 'Costo'), ('Is it covered by insurance?', '¿Lo cubre el seguro?'), ('Oral appliances for diagnosed sleep apnea are often covered by medical insurance rather than dental. The front desk will check with your plan before anything is made.', 'Los aparatos bucales para apnea diagnosticada suelen estar cubiertos por el seguro médico y no el dental. La recepción lo verifica con su plan antes de fabricar nada.')),
    ]
    return page_head(('Sleep apnea', 'Apnea del sueño'), ('Sleep apnea treatment without the mask', 'Tratamiento de apnea del sueño sin la máscara'),
                     ('A custom dental sleep device, fitted by a prosthodontist, keeps your airway open at night. Far more comfortable than CPAP, no surgery, nothing to plug in.', 'Un dispositivo dental a medida, ajustado por un prostodoncista, mantiene su vía aérea abierta de noche. Mucho más cómodo que el CPAP, sin cirugía, sin enchufes.')) + f'''
<section class="section">
  <div class="wrap service">
    <div>
      <span class="eyebrow">{t("How it works", "Cómo funciona")}</span>
      <h2 class="h2">{t("What the appliance does", "Qué hace el aparato")}</h2>
      <p class="lead" style="margin-top:0.75rem">{t("Obstructive sleep apnea happens when the tongue and soft tissue fall back and close the airway. The appliance holds the lower jaw a few millimetres forward, so the airway stays open and the snoring stops.", "La apnea obstructiva ocurre cuando la lengua y el tejido blando caen hacia atrás y cierran la vía aérea. El aparato sostiene la mandíbula unos milímetros hacia adelante, así la vía aérea queda abierta y el ronquido para.")}</p>
      {checklist([("Two thin custom trays, joined, worn only at night", "Dos férulas delgadas a medida, unidas, solo de noche"), ("Quiet: no pump, no hose, no mask", "Silencioso: sin bomba, sin manguera, sin máscara"), ("Fits in a pocket for travel", "Cabe en un bolsillo para viajar"), ("Adjustable in small steps until it works", "Ajustable en pasos pequeños hasta que funcione")])}
      <div class="btn-row"><a class="btn" href="contact.html#request">{t("Ask about the appliance", "Preguntar por el aparato")}</a></div>
    </div>
    <div class="service-art">{ART["sleep"]}</div>
  </div>
</section>
<section class="section section-alt">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">{t("The process", "El proceso")}</span><h2 class="h2">{t("Four visits, then once a year", "Cuatro visitas, luego una al año")}</h2></div>
    <div class="steps steps-4">{step_html}</div>
  </div>
</section>
<section class="section">
  <div class="wrap two-col two-col-start">
    <div class="section-head" style="margin-bottom:0"><span class="eyebrow">{t("Questions", "Preguntas")}</span><h2 class="h2">{t("Before you ask", "Antes de que pregunte")}</h2><p class="lead">{t("The three questions every sleep apnea patient asks first.", "Las tres preguntas que todo paciente con apnea hace primero.")}</p></div>
    <div>{faq_list(faqs)}</div>
  </div>
</section>
{cta_band('Tired of the mask?', '¿Cansado de la máscara?')}
'''

# =================================================================== DOCTORS
def doctors():
    return page_head(('Doctors', 'Doctores'), ('Meet the doctors', 'Conozca a los doctores'),
                     ('A prosthodontist who rebuilds, and a general dentist who keeps everything healthy. Between them, every treatment the office offers, in English, Spanish and German.', 'Un prostodoncista que reconstruye, y un dentista general que mantiene todo sano. Entre los dos, todos los tratamientos del consultorio, en español, inglés y alemán.')) + f'''
<section class="section" id="polo">
  <div class="wrap doctor doctor-page">
    <div class="doctor-photo"><div><b>CP</b><span>{t("Portrait to be supplied by the office", "Retrato a entregar por el consultorio")}</span></div></div>
    <div>
      <h2 class="h2">Dr. Carlos A. Polo, DDS, MS</h2>
      <p class="role">{t("Prosthodontist", "Prostodoncista")}</p>
      <p>{t("Dr. Polo trained at the Universidad Francisco Marroquín School of Dentistry in Guatemala City and received his D.D.S. with cum laude honors in 2003. He went on to specialty training in prosthodontics, the branch of dentistry that replaces and rebuilds teeth: crowns and bridges, complete and partial dentures, implant restorations and full‑mouth reconstruction.", "El Dr. Polo se formó en la Facultad de Odontología de la Universidad Francisco Marroquín, en la Ciudad de Guatemala, y recibió su D.D.S. con honores cum laude en 2003. Continuó con la especialidad en prostodoncia, la rama de la odontología que reemplaza y reconstruye dientes: coronas y puentes, prótesis completas y parciales, restauraciones sobre implantes y reconstrucción de boca completa.")}</p>
      <p>{t("Patients describe him the same way in review after review: he explains everything he is doing and why, before he does it. He also fits custom oral appliances for sleep apnea.", "Los pacientes lo describen igual, opinión tras opinión: explica todo lo que hace y por qué, antes de hacerlo. También ajusta aparatos bucales a medida para la apnea del sueño.")}</p>
      {checklist([("D.D.S., cum laude, Universidad Francisco Marroquín, 2003", "D.D.S., cum laude, Universidad Francisco Marroquín, 2003"), ("M.S. and specialty training in prosthodontics", "M.S. y especialidad en prostodoncia"), ("Languages: English, Spanish, German", "Idiomas: inglés, español, alemán")])}
    </div>
  </div>
</section>
<section class="section section-alt" id="cruz">
  <div class="wrap doctor doctor-page">
    <div class="doctor-photo"><div><b>JC</b><span>{t("Portrait to be supplied by the office", "Retrato a entregar por el consultorio")}</span></div></div>
    <div>
      <h2 class="h2">Dr. Jose G. Cruz, DDS</h2>
      <p class="role">{t("General dentist · Co‑founder", "Dentista general · Cofundador")}</p>
      <p>{t("Dr. Cruz co‑founded Dental Solutions of Winter Haven. He practices the whole of general dentistry, checkups, fillings, root canals and extractions, and places and restores implants, for children and adults, in English and Spanish.", "El Dr. Cruz cofundó Dental Solutions of Winter Haven. Ejerce toda la odontología general, revisiones, empastes, conductos y extracciones, y coloca y restaura implantes, para niños y adultos, en español e inglés.")}</p>
      <p>{t("Patients call him kind and compassionate, which is the part of dentistry no school teaches.", "Los pacientes lo llaman amable y compasivo, que es la parte de la odontología que ninguna escuela enseña.")}</p>
      {checklist([("D.D.S., general dentistry", "D.D.S., odontología general"), ("Implant placement and restoration", "Colocación y restauración de implantes"), ("Languages: English, Spanish", "Idiomas: inglés, español")])}
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="section-head center"><span class="eyebrow">{t("Why it matters", "Por qué importa")}</span><h2 class="h2">{t("Why two doctors matter", "Por qué importan dos doctores")}</h2></div>
    <div class="grid-3">
      <div class="card"><span class="icon">{I["tooth"]}</span><h3 class="h3">{t("Prosthodontist", "Prostodoncista")}</h3><p>{t("A dentist with two to three extra years of specialty training in replacing and rebuilding teeth. There are fewer than 4,000 in the United States.", "Un dentista con dos a tres años extra de especialidad en reemplazar y reconstruir dientes. Hay menos de 4.000 en Estados Unidos.")}</p></div>
      <div class="card"><span class="icon">{I["check"]}</span><h3 class="h3">{t("General dentist", "Dentista general")}</h3><p>{t("Your first stop for everything: prevention, diagnosis, fillings, root canals, extractions and children.", "Su primera parada para todo: prevención, diagnóstico, empastes, conductos, extracciones y niños.")}</p></div>
      <div class="card"><span class="icon">{I["globe"]}</span><h3 class="h3">{t("Together", "Juntos")}</h3><p>{t("One record, one plan, one bill, in your language. Nobody repeats your X‑rays or sends you across town.", "Un expediente, un plan, una cuenta, en su idioma. Nadie repite sus radiografías ni lo manda al otro lado del pueblo.")}</p></div>
    </div>
  </div>
</section>
{cta_band()}
'''

# =================================================================== REVIEWS
def reviews():
    return page_head(('Reviews', 'Opiniones'), ('What patients say', 'Lo que dicen los pacientes'),
                     ('A few public reviews, shortened. The practice holds 4.9 stars on Google from more than 260 reviews.', 'Algunas opiniones públicas, acortadas. El consultorio tiene 4,9 estrellas en Google con más de 260 opiniones.')) + f'''
<section class="section">
  <div class="wrap">
    <div class="card card-pad-lg rating" style="margin-bottom:1.5rem">
      <span class="big">4.9</span>
      <div><div class="stars" aria-label="4.9 out of 5">{I["star"] * 5}</div><strong style="display:block;color:var(--ink);margin-top:0.25rem">{t("More than 260 Google reviews", "Más de 260 opiniones en Google")}</strong><span class="muted small">{t("Figure from public directories; confirm the current count.", "Cifra de directorios públicos; confirmar el número actual.")}</span></div>
      <a class="btn btn-outline" style="margin-left:auto" href="{REVIEW}" target="_blank" rel="noopener">{t("Read them on Google", "Leerlas en Google")}</a>
    </div>
    <div class="grid-2">{review_cards(4)}</div>
  </div>
</section>
<section class="section section-alt">
  <div class="wrap grid-2">
    <div class="card card-pad-lg"><h3 class="h3">{t("Been a patient?", "¿Ha sido paciente?")}</h3><p>{t("A short review helps the next family find the office. It takes a minute on Google.", "Una opinión corta ayuda a la siguiente familia a encontrar el consultorio. Toma un minuto en Google.")}</p><div class="btn-row" style="margin-top:1.25rem"><a class="btn" href="{REVIEW}" target="_blank" rel="noopener">{t("Leave a Google review", "Dejar una opinión en Google")}</a></div></div>
    <div class="card card-pad-lg"><h3 class="h3">{t("New here?", "¿Nuevo aquí?")}</h3><p>{t("Your first visit is an exam and a conversation about options and cost, nothing more. Nobody will lecture you, however long it has been.", "Su primera visita es un examen y una conversación sobre opciones y costo, nada más. Nadie lo va a regañar, por mucho tiempo que haya pasado.")}</p><div class="btn-row" style="margin-top:1.25rem"><a class="btn btn-outline" href="contact.html#request">{t("Request a first visit", "Solicitar primera visita")}</a></div></div>
  </div>
</section>
{cta_band()}
'''

# =================================================================== CONTACT
def contact():
    pay = ['Visa', 'Mastercard', 'American Express', 'Discover', 'CareCredit', 'CitiHealth', t('Cash and check', 'Efectivo y cheque'), t('Most PPO plans', 'La mayoría de planes PPO')]
    return page_head(('Contact', 'Contacto'), ('Contact and hours', 'Contacto y horario'),
                     ('Call during office hours, or send the request below and the front desk replies the next business day. Hablamos español. Wir sprechen Deutsch.', 'Llame en horario de oficina o envíe la solicitud de abajo y la recepción responde el siguiente día hábil. We speak English. Wir sprechen Deutsch.')) + f'''
<section class="section" id="hours">
  <div class="wrap two-col two-col-start">
    <div class="card card-pad-lg">
      <h2 class="h2" style="margin-bottom:1rem">{t("Hours and address", "Horario y dirección")}</h2>
      <p style="margin-bottom:1rem"><span class="open-now" data-open-now></span></p>
      <table class="hours">
        <tr><td>{t("Monday", "Lunes")}</td><td>8:00 a.m. – 5:00 p.m.</td></tr>
        <tr><td>{t("Tuesday", "Martes")}</td><td>8:00 a.m. – 5:00 p.m.</td></tr>
        <tr><td>{t("Wednesday", "Miércoles")}</td><td>8:00 a.m. – 5:00 p.m.</td></tr>
        <tr><td>{t("Thursday", "Jueves")}</td><td>8:00 a.m. – 5:00 p.m.</td></tr>
        <tr><td>{t("Friday", "Viernes")}</td><td>{t("By appointment", "Con cita")}</td></tr>
        <tr><td>{t("Saturday and Sunday", "Sábado y domingo")}</td><td>{t("Closed", "Cerrado")}</td></tr>
      </table>
      <dl class="facts" style="margin-top:1.5rem">
        <div><dt>{t("Address", "Dirección")}</dt><dd>{ADDR1}<br>{ADDR2}</dd></div>
        <div><dt>{t("Phone", "Teléfono")}</dt><dd><a href="{TEL}">{PHONE}</a></dd></div>
        <div><dt>Email</dt><dd><a href="mailto:{MAIL}">{MAIL}</a></dd></div>
        <div><dt>{t("Languages", "Idiomas")}</dt><dd>English · Español · Deutsch</dd></div>
      </dl>
      <div class="btn-row" style="margin-top:1.5rem">
        <a class="btn" href="{MAPS}" target="_blank" rel="noopener">{t("Get directions", "Cómo llegar")}</a>
        <a class="btn btn-outline" href="{TEL}">{I["phone"]} {t("Call", "Llamar")}</a>
      </div>
    </div>
    <div>
      {tilemap()}
      <p class="caption">{t("6390 Cypress Gardens Blvd, Suite B, between Lake Eloise and Lake Winterset. Free parking at the door.", "6390 Cypress Gardens Blvd, Suite B, entre Lake Eloise y Lake Winterset. Estacionamiento gratis en la puerta.")}</p>
      <div style="margin-top:1.5rem">{lake_tool()}</div>
    </div>
  </div>
</section>
<section class="section section-alt" id="request">
  <div class="wrap two-col two-col-start">
    {request_form()}
    <div>
      <div class="card" style="margin-bottom:1.5rem"><span class="icon">{I["alert"]}</span><h3 class="h3">{t("Pain today?", "¿Dolor hoy?")}</h3><p>{t("Don’t use the form. Call as early as you can: same‑day times are kept open Monday to Thursday.", "No use el formulario. Llame lo antes posible: se reservan horas del mismo día de lunes a jueves.")}</p><div class="btn-row" style="margin-top:1rem"><a class="btn btn-accent" href="{TEL}">{I["phone"]} {PHONE}</a></div></div>
      <div class="card" id="pay"><span class="icon">{I["check"]}</span><h3 class="h3">{t("Insurance and payment", "Seguros y pagos")}</h3><p>{t("Most PPO plans are accepted and filed for you. CareCredit financing is available for larger plans, with a prequalification that does not affect your credit score.", "Se aceptan la mayoría de los planes PPO y el consultorio presenta el reclamo. Hay financiamiento CareCredit para planes grandes, con una precalificación que no afecta su puntaje de crédito.")}</p><ul class="chips">{''.join(f'<li>{p}</li>' for p in pay)}</ul></div>
    </div>
  </div>
</section>
<section class="section" id="faq">
  <div class="wrap two-col two-col-start">
    <div class="section-head" style="margin-bottom:0"><span class="eyebrow">FAQ</span><h2 class="h2">{t("Questions people ask first", "Lo que la gente pregunta primero")}</h2><p class="lead">{t("If yours is not here, call or send the form.", "Si la suya no está aquí, llame o envíe el formulario.")}</p></div>
    <div>{faq_list(FAQS)}</div>
  </div>
</section>
'''

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
