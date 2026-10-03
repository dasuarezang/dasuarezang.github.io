# >_ DSA · Daniel Suárez Angosto

CV web personal: estudiante de último año de **Ingeniería de Tecnologías y Servicios de Telecomunicación** (especialidad Telemática) en la ETSETB UPC y futuro **Network Engineer**.

Ver online: https://dasuarezang.github.io/cv/

---

## Características

- **Sin dependencias externas.** Estilos, scripts, iconos y logos pequeños van dentro de `index.html`. Las fotos y las fuentes principales están en `assets/`. No se carga nada de otros servidores.
- **Trilingüe ES / EN / CA.** El cambio de idioma es instantáneo y afecta a todo: textos, frase animada, insignias de idiomas, terminal, carta de recomendación y página 404. La primera visita se abre en castellano o en catalán según el idioma del navegador (y en inglés si no es ninguno de los dos). La elección manual se recuerda entre visitas y se comparte entre las páginas.
- **Funciona sin JavaScript.** El cambio de idioma, el menú móvil, la frase animada y el carrusel están hechos con HTML y CSS, así que funcionan también en visores de archivos del móvil que bloquean JavaScript. El JavaScript solo añade extras.
- **Estética de terminal.** Etiquetas `$ cd ~/sección`, esquinas tipo plano técnico en las tarjetas, navegación en fuente monoespaciada y logo `>_ DSA`.
- **Portada con red animada.** Un diagrama del proyecto VitalLink (Raspberry Pi, Arduino, TTN, Node-RED, PostgreSQL, Next.js) rodea la foto, con paquetes y pulsos animados. La animación se pausa cuando no se ve y se desactiva con *reducir movimiento*.
- **Experiencia como `traceroute`.** La línea de tiempo se rellena al hacer scroll y cada salto (*hop*) se enciende al llegar a él. El salto 01 es el puesto más antiguo.
- **Terminal escondida.** Se abre con la tecla `º` (o `` ` ``) o con el botón del pie. Responde con el propio contenido del CV: `whoami`, `about`, `education`, `experience`, `traceroute`, `projects`, `skills`, `certs`, `contact`, `email`, `cv`, `ping`, `lang es|en|ca`, entre otros. En pantallas táctiles se usa con botones, sin abrir el teclado.
- **Diseño adaptable.** Probado de 280 px (móvil plegable) a 4K, en vertical y en horizontal, con los motores de Chrome, Safari y Firefox y sin scroll horizontal. Con el móvil en horizontal, el menú se reparte en dos columnas.
- **Modo oscuro automático** según el ajuste del sistema.
- **PDF descargable.** El botón *Descargar CV* baja un PDF ya generado en el idioma activo (`cv-daniel-suarez-es.pdf`, `-en.pdf` y `-ca.pdf`): un CV limpio en blanco de 2 páginas A4 con todas las secciones y los proyectos desplegados. También se puede usar *Imprimir → Guardar como PDF*.
- **Accesible.** Enlace "Saltar al contenido", navegación por teclado, textos alternativos, zonas táctiles de tamaño adecuado y respeto a *reducir movimiento*. Sin errores de accesibilidad según axe en los tres idiomas, en claro y oscuro, en escritorio y móvil.
- **Ligero y rápido.** `index.html` pesa unos 285 KB (88 KB comprimido). Las imágenes van en WebP y las fotos de los proyectos se cargan solo al llegar a ellas. Las fuentes están reducidas a los caracteres y pesos que se usan y se precargan. Medido en Chromium sin limitar la red: LCP de 1,7 a 1,9 s, CLS por debajo de 0,01 y sin errores en la consola.
- **Listo para compartir.** Metadatos Open Graph con imagen de vista previa para LinkedIn, WhatsApp o X, datos estructurados de schema.org, sitemap, favicon propio e icono para la pantalla de inicio del móvil.

### Detalles de la interfaz

- Navegación flotante con el apartado activo resaltado y una barra de progreso de lectura.
- Menú móvil a pantalla completa, con el icono de hamburguesa que se transforma en una X.
- Animaciones de entrada al hacer scroll y transiciones con curvas tipo muelle.
- Botón de correo que además copia la dirección y lo confirma con un aviso.
- Botón para volver arriba.

## Secciones

| Sección | Detalle |
|---|---|
| **Portada** | Nombre, frase animada tipo terminal en ES / EN / CA, red animada alrededor de la foto y contacto (correo, LinkedIn, GitHub) |
| **Sobre mí** | Perfil profesional |
| **Educación** | Grado en la ETSETB · UPC |
| **Experiencia** | Traceroute con tarjetas y logos: Fòrum Telecos UPC y Real Madrid Official Store, con un extracto de la carta de recomendación |
| **Proyectos** | Carrusel infinito (da la vuelta del último al primero con flechas, puntos o deslizando; sin JavaScript es un carrusel normal) con tarjetas desplegables y las tecnologías de cada proyecto: red P2P para LLMs (con enlace a su código en GitHub), VitalLink (monitorización remota de salud con LoRaWAN, con enlace a su código), medidor de distancia por ultrasonidos y ROUV (vehículo subacuático) |
| **Habilidades** | Redes, lenguajes, web y bases de datos, infraestructura y sistemas operativos, e idiomas |
| **Certificados** | Una tarjeta por entidad (Harvard, IBM, Cisco), con enlace a la validación de cada certificado. Cada tarjeta enseña los 3 más recientes y despliega el resto con "ver más", así que la sección escala sin alargarse. En el PDF salen todos |

## Archivos

| Archivo | Uso |
|---|---|
| `index.html` | El CV completo |
| `recomendaciones/real-madrid-official-store/` | Página de la carta de recomendación (imagen en tres tamaños y PDF descargable), con el teléfono de contacto omitido y traducción al inglés |
| `recomendacion/` | Redirección de la dirección antigua de la carta |
| `404.html` | Página de error con un traceroute que se pierde en el tercer salto |
| `sitemap.xml` | Solo la página principal; la carta, la redirección y la 404 llevan `noindex` |
| `cv-daniel-suarez-es.pdf`, `-en.pdf`, `-ca.pdf` | PDF del CV en cada idioma, generados con `scripts/build_pdfs.py` |
| `og-image.jpg` | Imagen de vista previa al compartir el enlace (1200 × 630) |
| `favicon.ico`, `icon.svg`, `icon-*.png` | Icono del sitio como archivos reales (Google no lee los iconos incrustados en el HTML) |
| `scripts/` | `build_pdfs.py` genera los PDF y `check.py` comprueba la web antes de subir cambios |
| `apple-touch-icon.png` | Icono al guardar la web en la pantalla de inicio del móvil |
| `google27aa19f9bf52eea7.html` | Verificación de Google Search Console (no borrar) |
| `assets/` | Foto de perfil, logo de la ETSETB, fotos de los 4 proyectos, logo de VitalLink y fuentes Geist y Geist Mono |

## Mantenimiento

Cada vez que cambie el contenido del CV hay que regenerar los PDF y pasar las comprobaciones. Hace falta [uv](https://docs.astral.sh/uv/) (la primera vez, `uv run --with playwright python -m playwright install chromium`).

```
uv run --with playwright --with pypdfium2 python scripts/build_pdfs.py
uv run --with playwright --with pypdfium2 --with axe-playwright-python --with pillow python scripts/check.py
```

`check.py` comprueba, sobre la web servida en local: que todo texto está en castellano, inglés y catalán (también en la terminal); que todos los archivos enlazados existen; que los enlaces externos responden (solo avisa); accesibilidad con axe en los tres idiomas, en claro y oscuro, en escritorio y móvil; que los iconos son archivos reales; que los tres PDF existen, caben en 2 páginas y no están desactualizados; y que el carrusel de proyectos da la vuelta. Sale con error si algo falla. Con `--offline` salta los enlaces externos. Se ejecuta también solo en GitHub (en cada subida, en cada pull request y una vez a la semana); allí no compara los PDF con la web porque el diseño de impresión depende de las fuentes del sistema, así que esa comprobación hay que pasarla en local.

Todo texto nuevo del CV se escribe en las tres versiones (`t-es`, `t-en`, `t-ca`).

## Tecnologías

HTML5 · CSS3 (Grid, Flexbox, scroll-snap, `<details>`, `:has()`, `:target`, animaciones ligadas al scroll, `prefers-color-scheme`, `@media print`) · JavaScript vanilla, solo como mejora progresiva (IntersectionObserver, ResizeObserver, Clipboard API)

## Créditos

- Iconos: [Phosphor Icons](https://phosphoricons.com) (MIT)
- Fuentes: [Geist y Geist Mono](https://vercel.com/font) y [Press Start 2P](https://fonts.google.com/specimen/Press+Start+2P) (SIL Open Font License)
- Insignias: [shields.io](https://shields.io)
- Los logotipos de UPC · ETSETB, Fòrum Telecos UPC, Real Madrid, Harvard, IBM y Cisco pertenecen a sus respectivos propietarios y se usan solo para identificar la institución o empresa.

---

© 2026 Daniel Suárez Angosto — Todos los derechos reservados.
