"""Comprobaciones del CV antes de subir cambios.

Uso (desde la carpeta del repositorio):
    uv run --with playwright --with pypdfium2 --with axe-playwright-python python scripts/check.py
Opciones:
    --offline   no comprueba los enlaces externos

Qué comprueba:
  1. Textos: todo texto en castellano (.t-es) tiene su versión en inglés (.t-en) y en catalán (.t-ca), y la
     terminal tiene las mismas frases en los tres idiomas.
  2. Archivos: todo lo que enlazan las páginas (imágenes, PDF, iconos...) existe en el repositorio.
  3. Enlaces externos (aviso, no error: algunas webs bloquean a los robots).
  4. Accesibilidad (axe) en los tres idiomas, en claro y oscuro, en escritorio y móvil.
  5. Iconos: archivos reales (Google no admite data URIs) y declarados en todas las páginas.
  6. PDF: existen, no pasan de 2 páginas y (solo en local) no están desactualizados respecto a la web.
  7. Carrusel infinito: dar la vuelta con la flecha vuelve al primer proyecto.
Sale con código 1 si hay algún error.
"""
import os
import pathlib
import re
import sys
import tempfile
import urllib.request

from playwright.sync_api import sync_playwright

from _site import ROOT, serve
from build_pdfs import LANGS, MAX_PAGES, build, pages_and_text

PAGES = ['index.html', '404.html', 'recomendaciones/real-madrid-official-store/index.html']
errors, warnings = [], []


def ok(msg):
    print('OK     ' + msg)


def err(msg):
    errors.append(msg)
    print('ERROR  ' + msg)


def warn(msg):
    warnings.append(msg)
    print('AVISO  ' + msg)


# ---------- 1. textos en tres idiomas ----------
I18N_JS = """() => {
  const out = [];
  document.querySelectorAll('.t-es,.t-en,.t-ca').forEach(el => {
    const p = el.parentElement;
    for (const c of ['t-es', 't-en', 't-ca']) {
      if (!p.querySelector(':scope > .' + c)) {
        out.push((el.textContent || el.getAttribute('alt') || '').trim().slice(0, 50) + '  (falta ' + c + ')');
        break;
      }
    }
  });
  return [...new Set(out)];
}"""


def terminal_keys(page, html):
    """Claves del objeto S de la terminal (frases en cada idioma), evaluándolo en el navegador."""
    start = html.index('const S = ') + len('const S = ')
    depth = 0
    for i, ch in enumerate(html[start:], start):
        depth += (ch == '{') - (ch == '}')
        if depth == 0:
            literal = html[start:i + 1]
            break
    return page.evaluate("src => { const S = new Function('return (' + src + ')')(); "
                         "return { es: Object.keys(S.es), en: Object.keys(S.en), ca: Object.keys(S.ca) }; }", literal)


def check_texts(page, base):
    bad = False
    for path in PAGES:
        page.goto('%s/cv/%s' % (base, path.replace('index.html', '')))
        missing = page.evaluate(I18N_JS)
        if missing:
            bad = True
            for t in missing[:10]:
                err('texto sin las tres versiones en %s: %s' % (path, t))
    html = (ROOT / 'index.html').read_text(encoding='utf-8')
    keys = terminal_keys(page, html)
    for lang in ('en', 'ca'):
        diff = set(keys['es']) ^ set(keys[lang])
        if diff:
            bad = True
            err('la terminal tiene claves distintas en es y %s: %s' % (lang, sorted(diff)))
    if not bad:
        ok('todos los textos están en castellano, inglés y catalán (CV, carta, 404 y terminal)')


# ---------- 2 y 3. archivos y enlaces ----------
REF = re.compile(r'''(?:href|src|poster)="([^"]+)"|srcset="([^"]+)"|url\(["']?([^)"']+)["']?\)|<meta (?:property|name)="(?:og|twitter):image" content="([^"]+)"''')


def refs(html):
    for m in REF.finditer(html):
        if m.group(2):
            for part in m.group(2).split(','):
                yield part.strip().split(' ')[0]
        else:
            yield m.group(1) or m.group(3) or m.group(4)


def check_files(offline):
    external, missing = set(), []
    for path in PAGES:
        base = (ROOT / path).parent
        html = (ROOT / path).read_text(encoding='utf-8')
        for r in refs(html):
            if not r or r.startswith(('data:', 'mailto:', 'tel:', '#', '%23', 'javascript:')):
                continue
            r = r.replace('https://dasuarezang.github.io/cv/', '/cv/')
            if r.startswith(('http://', 'https://')):
                if r.startswith('https://dasuarezang.github.io'):
                    continue
                external.add(r)
                continue
            r = r.split('#')[0].split('?')[0]
            if not r or r in ('/cv/', '/cv'):
                continue
            target = (ROOT / r[len('/cv/'):]) if r.startswith('/cv/') else (base / r)
            if r.startswith('/') and not r.startswith('/cv/'):
                continue
            if not target.exists():
                missing.append('%s -> %s' % (path, r))
    for m in sorted(set(missing)):
        err('archivo enlazado que no existe: ' + m)
    if not missing:
        ok('todos los archivos enlazados existen')
    if offline:
        return
    bad = 0
    for url in sorted(external):
        if any(h in url for h in ('fonts.googleapis', 'shields.io', 'www.w3.org')):
            continue
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=20) as r:
                if r.status >= 400:
                    raise ValueError(r.status)
        except Exception as e:
            code = getattr(e, 'code', e)
            if code in (999, 403, 429):
                warn('enlace externo que bloquea a los robots (%s): %s' % (code, url))
            else:
                bad += 1
                warn('enlace externo que no responde (%s): %s' % (code, url))
    if not bad:
        ok('los %d enlaces externos responden' % len(external))


# ---------- 4. accesibilidad ----------
def check_axe(browser, base):
    from axe_playwright_python.sync_playwright import Axe
    axe = Axe()
    found = 0
    combos = [(loc, scheme, vp) for loc in ('es-ES', 'en-US', 'ca-ES') for scheme in ('light', 'dark')
              for vp in ((1366, 768), (390, 844))]
    for loc, scheme, vp in combos:
        ctx = browser.new_context(locale=loc, color_scheme=scheme, viewport={'width': vp[0], 'height': vp[1]}, reduced_motion='reduce')
        page = ctx.new_page()
        for path in PAGES:
            page.goto('%s/cv/%s' % (base, path.replace('index.html', '')))
            page.wait_for_timeout(500)
            if path == 'index.html':
                page.evaluate("document.querySelectorAll('.reveal').forEach(e => e.classList.add('in-view'))")
                page.evaluate("document.getElementById('proyectos').scrollIntoView()")
                page.wait_for_timeout(700)
            for v in axe.run(page).response['violations']:
                found += 1
                err('accesibilidad (%s, %s, %dpx, %s): %s en %s' % (loc, scheme, vp[0], path, v['id'], v['nodes'][0]['target']))
        ctx.close()
    if not found:
        ok('axe: 0 problemas de accesibilidad (%d combinaciones x %d páginas)' % (len(combos), len(PAGES)))


# ---------- 5. iconos ----------
def check_icons():
    from PIL import Image
    bad = False
    for f in ('favicon.ico', 'icon.svg', 'icon-48.png', 'icon-192.png', 'apple-touch-icon.png', 'og-image.jpg'):
        if not (ROOT / f).exists():
            bad = True
            err('falta el icono ' + f)
    ico = Image.open(ROOT / 'favicon.ico')
    if (48, 48) not in ico.info.get('sizes', set()):
        bad = True
        err('favicon.ico no incluye la medida 48x48 que recomienda Google')
    for path in PAGES:
        html = (ROOT / path).read_text(encoding='utf-8')
        if re.search(r'<link rel="icon"[^>]*href="data:', html):
            bad = True
            err('%s declara un icono como data URI (Google no lo lee)' % path)
        if 'favicon.ico' not in html:
            bad = True
            err('%s no declara favicon.ico' % path)
    if not bad:
        ok('iconos: archivos reales, con 48 px y declarados en todas las páginas')


# ---------- 6. PDF ----------
def check_pdfs():
    bad = False
    for lang in LANGS:
        path = ROOT / ('cv-daniel-suarez-%s.pdf' % lang)
        if not path.exists():
            bad = True
            err('falta %s (ejecuta scripts/build_pdfs.py)' % path.name)
            continue
        n, _ = pages_and_text(path)
        if n > MAX_PAGES:
            bad = True
            err('%s tiene %d páginas (máximo %d)' % (path.name, n, MAX_PAGES))
    if os.environ.get('CI'):
        # El diseño de impresión depende de las fuentes del sistema (p. ej. Verdana), así que en GitHub
        # (Linux) saldría distinto que en tu ordenador: la comparación con la web solo se hace en local
        warn('PDF actualizados y páginas al imprimir: solo se comprueban en local (en GitHub el sistema tiene otras fuentes)')
        if not bad:
            ok('los 3 PDF existen y caben en %d páginas' % MAX_PAGES)
        return
    with tempfile.TemporaryDirectory() as tmp:
        fresh = build(tmp)
        for lang in LANGS:
            n2, fresh_text = pages_and_text(fresh[lang])
            _, text = pages_and_text(ROOT / ('cv-daniel-suarez-%s.pdf' % lang))
            if n2 > MAX_PAGES:
                bad = True
                err('la web pasa de %d páginas al imprimir en %s' % (MAX_PAGES, lang))
            if text != fresh_text:
                bad = True
                err('cv-daniel-suarez-%s.pdf está desactualizado: ejecuta scripts/build_pdfs.py y súbelo' % lang)
    if not bad:
        ok('los 3 PDF existen, caben en %d páginas y están al día con la web' % MAX_PAGES)


# ---------- 7. carrusel ----------
def check_carousel(browser, base):
    ctx = browser.new_context(locale='ca-ES', viewport={'width': 1280, 'height': 900})
    page = ctx.new_page()
    page.goto(base + '/cv/')
    page.wait_for_timeout(500)
    page.evaluate("document.getElementById('proyectos').scrollIntoView()")
    page.wait_for_timeout(900)
    n = page.evaluate("document.querySelectorAll('#projTrack .proj-card:not(.is-clone)').length")
    seq = []
    for _ in range(n + 1):
        page.click('.car-btn[data-dir="1"]')
        page.wait_for_timeout(1100)
        seq.append(page.evaluate("[...document.querySelectorAll('.car-dot')].findIndex(d => d.getAttribute('aria-current') === 'true')"))
    ctx.close()
    expected = [(i + 1) % n for i in range(n + 1)]
    if seq == expected:
        ok('carrusel infinito: da la vuelta del último al primero (%s)' % seq)
    else:
        err('el carrusel no da la vuelta bien: %s en vez de %s' % (seq, expected))


def main():
    offline = '--offline' in sys.argv
    srv, base = serve()
    with sync_playwright() as p:
        browser = p.chromium.launch()
        ctx = browser.new_context(viewport={'width': 1280, 'height': 900})
        page = ctx.new_page()
        check_texts(page, base)
        ctx.close()
        check_files(offline)
        check_icons()
        check_axe(browser, base)
        check_carousel(browser, base)
        browser.close()
    check_pdfs()
    srv.shutdown()
    print()
    print('%d errores, %d avisos' % (len(errors), len(warnings)))
    sys.exit(1 if errors else 0)


if __name__ == '__main__':
    main()
