"""Genera los PDF del CV (español, inglés y catalán) a partir de la propia web.

Uso (desde la carpeta del repositorio):
    uv run --with playwright --with pypdfium2 python scripts/build_pdfs.py
(la primera vez: uv run --with playwright python -m playwright install chromium)

Cada PDF es lo que sale de Imprimir -> Guardar como PDF con la web en ese idioma, con los proyectos
desplegados. Se guardan como cv-daniel-suarez-es.pdf, -en.pdf y -ca.pdf junto a index.html, y el botón
"Descargar CV" de la web enlaza a ellos. Hay que volver a ejecutarlo cada vez que cambie el contenido del CV
(scripts/check.py avisa si los PDF han quedado desactualizados).
"""
import pathlib
import sys

from playwright.sync_api import sync_playwright

from _site import ROOT, serve

LANGS = {'es': 'es-ES', 'en': 'en-US', 'ca': 'ca-ES'}
MAX_PAGES = 2


def build(out_dir=ROOT):
    """Genera los tres PDF en out_dir y devuelve {idioma: ruta}."""
    srv, base = serve()
    result = {}
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for lang, locale in LANGS.items():
            ctx = browser.new_context(locale=locale, viewport={'width': 1280, 'height': 900}, reduced_motion='reduce')
            page = ctx.new_page()
            page.goto(base + '/index.html')
            page.wait_for_timeout(400)
            page.evaluate("l => document.getElementById('lang-' + l).click()", lang)
            page.evaluate("document.querySelectorAll('.proj-card:not(.is-clone)').forEach(d => { d.open = true; })")
            page.evaluate("l => { document.title = 'CV - Daniel Suárez Angosto (' + l.toUpperCase() + ')'; }", lang)
            page.emulate_media(media='print')
            path = pathlib.Path(out_dir) / ('cv-daniel-suarez-%s.pdf' % lang)
            path.write_bytes(page.pdf(format='A4', print_background=True))
            result[lang] = path
            ctx.close()
        browser.close()
    srv.shutdown()
    return result


def pages_and_text(path):
    import pypdfium2 as pdfium
    pdf = pdfium.PdfDocument(pathlib.Path(path).read_bytes())
    try:
        text = ' '.join(pdf[i].get_textpage().get_text_range() for i in range(len(pdf)))
        return len(pdf), ' '.join(text.split())
    finally:
        pdf.close()


if __name__ == '__main__':
    ok = True
    for lang, path in build().items():
        n, _ = pages_and_text(path)
        print('%s: %s (%d páginas, %d KB)' % (lang, path.name, n, path.stat().st_size // 1024))
        if n > MAX_PAGES:
            ok = False
            print('  AVISO: pasa de %d páginas; hay que acortar contenido o ajustar el CSS de impresión' % MAX_PAGES)
    sys.exit(0 if ok else 1)
