// Dental Solutions of Winter Haven · shared script for every page.
// 1. Language switch (English / Spanish), remembered across pages.
// 2. "Open now" from Winter Haven time (Mon–Thu 8–5, Friday by appointment).
// 3. The phone menu.
// 4. Reveals: the hero shutter, section entrances, the pair of lakes.
// 5. The chain of lakes: pick your lake, read the distance to the office.
// 6. The coupon form opens an email with the message filled in.
// 7. FAQ cards: one open at a time.

(() => {
  const root = document.documentElement;
  const button = document.getElementById('lang');
  const apply = (lang) => {
    root.dataset.lang = lang;
    root.lang = lang;
    try { localStorage.setItem('dswh-lang', lang); } catch (e) { /* private window */ }
    document.querySelectorAll('[data-en]').forEach((o) => {
      const v = o.dataset[lang] || o.dataset.en;
      if (o.tagName === 'OPTION' || o.tagName === 'SPAN' || o.tagName === 'LABEL') o.textContent = v;
      else if ('placeholder' in o) o.placeholder = v;
    });
    updateOpenNow();
    updateChain();
  };
  if (button) button.addEventListener('click', () => apply(root.dataset.lang === 'es' ? 'en' : 'es'));
  const q = new URLSearchParams(location.search).get('lang');
  if (q === 'es' || q === 'en') apply(q); else apply(root.dataset.lang || 'en');
})();

// Hours: Monday to Thursday, 8 to 5, Winter Haven time (America/New_York). Friday by appointment.
function updateOpenNow() {
  const els = document.querySelectorAll('[data-open-now]');
  if (!els.length) return;
  let parts;
  try {
    parts = new Intl.DateTimeFormat('en-US', { timeZone: 'America/New_York', weekday: 'short', hour: 'numeric', minute: 'numeric', hour12: false }).formatToParts(new Date());
  } catch (e) { return; }
  const get = (type) => (parts.find((p) => p.type === type) || {}).value;
  const day = get('weekday');
  const minutes = (Number(get('hour')) % 24) * 60 + Number(get('minute'));
  const weekday = ['Mon', 'Tue', 'Wed', 'Thu'].includes(day);
  const open = weekday && minutes >= 8 * 60 && minutes < 17 * 60;
  const es = document.documentElement.dataset.lang === 'es';
  let text;
  if (open) {
    text = (17 * 60 - minutes <= 60) ? (es ? 'Abierto, cierra pronto' : 'Open now, closes soon') : (es ? 'Abierto ahora' : 'Open now');
  } else if (weekday && minutes < 8 * 60) {
    text = es ? 'Cerrado, abre a las 8' : 'Closed, opens at 8 a.m.';
  } else if (day === 'Fri') {
    text = es ? 'Viernes: solo con cita' : 'Friday: by appointment';
  } else if (day === 'Sat' || day === 'Sun') {
    text = es ? 'Cerrado, abre el lunes a las 8' : 'Closed, opens Monday at 8 a.m.';
  } else {
    text = es ? 'Cerrado, abre mañana a las 8' : 'Closed, opens tomorrow at 8 a.m.';
  }
  els.forEach((el) => { el.textContent = text; el.classList.toggle('is-closed', !open); });
}
updateOpenNow();
setInterval(updateOpenNow, 60000);

// Phone menu
(() => {
  const burger = document.getElementById('burger');
  const menu = document.getElementById('menu');
  if (!burger || !menu) return;
  burger.addEventListener('click', () => {
    const open = menu.classList.toggle('is-open');
    burger.setAttribute('aria-expanded', String(open));
  });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && menu.classList.contains('is-open')) burger.click(); });
})();

// Reveals, once, as sections enter. After 2.5 s the hero is shown whatever happened to the animations.
setTimeout(() => document.documentElement.classList.add('settled'), 2500);
(() => {
  const hero = document.querySelector('.shutter');
  const pair = document.querySelector('.hero-pair');
  requestAnimationFrame(() => { if (hero) hero.classList.add('is-in'); if (pair) pair.classList.add('is-in'); });
  if (!('IntersectionObserver' in window)) {
    document.querySelectorAll('[data-reveal], [data-reveal-pic]').forEach((el) => el.classList.add('is-in'));
    return;
  }
  document.querySelectorAll('[data-reveal]').forEach((el) => {
    Array.from(el.children).forEach((c, i) => c.style.setProperty('--n', String(i)));
  });
  const io = new IntersectionObserver((entries) => {
    for (const e of entries) if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); }
  }, { rootMargin: '0px 0px -12% 0px', threshold: 0.1 });
  document.querySelectorAll('[data-reveal], [data-reveal-pic]').forEach((el) => io.observe(el));
})();

// The chain of lakes: pick a lake, read how far it is from the office.
function updateChain() {
  const select = document.getElementById('lake-select');
  const map = document.getElementById('chain-map');
  const result = document.getElementById('chain-result');
  if (!select || !map || !result) return;
  const es = document.documentElement.dataset.lang === 'es';
  const picked = select.value;
  map.querySelectorAll('path[data-name]').forEach((p) => p.classList.toggle('is-picked', p.dataset.name === picked));
  const label = map.querySelector('#chain-label');
  const opt = select.selectedOptions[0];
  if (!opt || !picked) {
    result.innerHTML = `<strong>${es ? 'Elija su lago' : 'Pick your lake'}</strong><span>${es ? 'Las distancias son aproximadas, desde el centro del lago hasta el consultorio.' : 'Distances are approximate, from the middle of the lake to the office.'}</span>`;
    if (label) label.textContent = '';
    return;
  }
  const km = Number(opt.dataset.km);
  const miles = km * 0.621371;
  const minutes = Math.max(3, Math.round((km * 1.3) / 40 * 60 + 2));
  const mi = miles < 10 ? miles.toFixed(1) : Math.round(miles);
  result.innerHTML = es
    ? `<strong>Unos ${minutes} minutos</strong><span>${picked} queda a unas ${mi} millas del consultorio, en 6390 Cypress Gardens Blvd.</span>`
    : `<strong>About ${minutes} minutes</strong><span>${picked} is about ${mi} miles from the office at 6390 Cypress Gardens Blvd.</span>`;
  if (label) {
    label.textContent = picked;
    label.setAttribute('x', opt.dataset.cx);
    label.setAttribute('y', String(Number(opt.dataset.cy) - 18));
  }
}
(() => {
  const select = document.getElementById('lake-select');
  const map = document.getElementById('chain-map');
  if (!select) return;
  select.addEventListener('change', updateChain);
  if (map) {
    map.querySelectorAll('path[data-name]').forEach((p) => {
      p.addEventListener('click', () => { select.value = p.dataset.name; updateChain(); select.focus({ preventScroll: true }); });
    });
  }
  updateChain();
})();

// Contact form: opens an email with everything filled in (no backend yet).
(() => {
  const form = document.getElementById('contact-form');
  if (!form) return;
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const d = new FormData(form);
    const es = document.documentElement.dataset.lang === 'es';
    const subject = es ? `Solicitud de cita: ${d.get('name') || ''}` : `Appointment request: ${d.get('name') || ''}`;
    const body = [
      (es ? 'Nombre: ' : 'Name: ') + (d.get('name') || ''),
      (es ? 'Teléfono: ' : 'Phone: ') + (d.get('phone') || ''),
      (es ? 'Motivo: ' : 'Reason: ') + (d.get('reason') || ''),
      '',
      d.get('message') || '',
    ].join('\n');
    location.href = `mailto:${form.dataset.mail}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
  });
})();

// FAQ cards: one open at a time (for browsers without the `name` attribute on details).
(() => {
  const cards = document.querySelectorAll('details.card');
  cards.forEach((c) => c.addEventListener('toggle', () => {
    if (c.open) cards.forEach((o) => { if (o !== c && o.open) o.open = false; });
  }));
})();
