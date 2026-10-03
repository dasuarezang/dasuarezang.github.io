# >_ DSA · Daniel Suárez Angosto

CV web personal: estudiante de último año de **Ingeniería de Tecnologías y Servicios de Telecomunicación** (especialidad Telemática) en la ETSETB UPC y futuro **Network Engineer**.

🌐 **Ver online:** https://dasuarezang.github.io/cv/

---

## ✨ Características

- **Sin dependencias externas.** Estilos, scripts, iconos y logos pequeños van dentro de `index.html`. Las fotos y las fuentes principales están en la carpeta `assets/`, para que la página cargue antes. No se carga nada de otros servidores.
- **Trilingüe ES / EN / CA.** Cambio de idioma al instante, también en la frase animada y en la terminal. La primera visita se abre en castellano o en catalán según el idioma del navegador (y en inglés si no es ninguno de los dos), y la elección manual se recuerda entre visitas.
- **Funciona sin JavaScript.** El cambio de idioma, el menú móvil (que se cierra solo al elegir un apartado), la frase animada y el carrusel están hechos con HTML y CSS, así que funcionan también en visores de archivos del móvil que bloquean JavaScript. El JavaScript solo añade extras.
- **Diseño adaptable.** Probado de 280 px (móvil plegable) a 1920 px, en vertical y en horizontal, con los motores de Chrome, Safari y Firefox y sin scroll horizontal. Con el móvil en horizontal, el menú se reparte en dos columnas.
- **Modo oscuro automático** según el ajuste del sistema.
- **Listo para imprimir.** El botón *Descargar CV* (o *Imprimir → Guardar como PDF*) genera un CV limpio en blanco de 3 páginas A4, con todas las secciones y los proyectos desplegados.
- **Accesible.** Enlace "Saltar al contenido", navegación por teclado, textos alternativos, zonas táctiles de tamaño adecuado y respeto a *reducir movimiento*.
- **Ligero y rápido.** `index.html` pesa ~190 KB. Las imágenes van en WebP y las fotos de los proyectos se cargan solo al llegar a ellas. Las fuentes están reducidas a los caracteres y pesos que se usan y se precargan. En Lighthouse: 100 en accesibilidad, buenas prácticas y SEO, y 99–100 de rendimiento en móvil y escritorio.
- **Listo para compartir.** Metadatos Open Graph con imagen de vista previa para LinkedIn, WhatsApp o X, datos estructurados de schema.org para buscadores, favicon propio e icono para la pantalla de inicio del móvil.

### Detalles de la interfaz

- Navegación flotante con el apartado activo resaltado y una barra de progreso de lectura.
- Menú móvil a pantalla completa, con el icono de hamburguesa que se transforma en una X.
- Tarjetas con doble borde, animaciones de entrada al hacer scroll y transiciones con curvas tipo muelle.
- Botón de correo que además copia la dirección y lo confirma con un aviso.
- Botón para volver arriba.

## 🧩 Secciones

| Sección | Detalle |
|---|---|
| **Portada** | Nombre, frase animada tipo terminal en ES / EN / CA y contacto (correo, LinkedIn, GitHub) |
| **Sobre mí** | Perfil profesional |
| **Educación** | Grado en la ETSETB · UPC |
| **Experiencia** | Timeline de tarjetas con logos: Fòrum Telecos UPC y Real Madrid Official Store |
| **Proyectos** | Carrusel deslizable con tarjetas desplegables y las tecnologías de cada proyecto: red P2P para LLMs (con enlace a su código en GitHub), VitalLink (monitorización remota de salud con LoRaWAN), medidor de distancia por ultrasonidos y ROUV (vehículo subacuático) |
| **Habilidades** | Lenguajes, web y bases de datos, infraestructura y sistemas operativos, e idiomas |
| **Certificados** | Harvard (CS50), IBM y Cisco, con enlace a la validación de cada uno |

## 📁 Archivos

| Archivo | Uso |
|---|---|
| `index.html` | El CV completo |
| `og-image.png` | Imagen de vista previa al compartir el enlace (1200 × 630) |
| `apple-touch-icon.png` | Icono al guardar la web en la pantalla de inicio del móvil |
| `assets/` | Foto de perfil, logo de la ETSETB, fotos de los 4 proyectos, logo de VitalLink y fuentes Geist y Geist Mono |

## 🛠️ Tecnologías

HTML5 · CSS3 (Grid, Flexbox, scroll-snap, `<details>`, `:has()`, `:target`, animaciones ligadas al scroll, `prefers-color-scheme`, `@media print`) · JavaScript vanilla, solo como mejora progresiva (IntersectionObserver, Clipboard API)

## 📄 Créditos

- Iconos: [Phosphor Icons](https://phosphoricons.com) (MIT)
- Fuentes: [Geist y Geist Mono](https://vercel.com/font) y [Press Start 2P](https://fonts.google.com/specimen/Press+Start+2P) (SIL Open Font License)
- Insignias: [shields.io](https://shields.io)
- Los logotipos de UPC · ETSETB, Fòrum Telecos UPC, Real Madrid, Harvard, IBM y Cisco pertenecen a sus respectivos propietarios y se usan solo para identificar la institución o empresa.

---

© 2026 Daniel Suárez Angosto — Todos los derechos reservados.
