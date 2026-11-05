# Richtlinie 16 Intrinsisches Design, Responsivität & Core Web Vitals

## Status & Verbindlichkeit
- **Gültigkeit:** Strikt für alle Komponenten, Layouts, Typografie, Medien-Assets und CSS/Tailwind-Tokens.
- **Priorität:** Kritisch / Visueller Standard, Mobile-First-Nutzbarkeit & Ladezeit-Exzellenz.

---

## 1. Das Paradigma des intrinsischen Designs (Intrinsic Web Design)
Die Website setzt nicht auf starre, rein gerätebezogene Viewport-Breakpoints, sondern auf **intrinsisches Design**: Das Layout orientiert sich am Inhalt und dem tatsächlich verfügbaren Platz.

1. **Fluidität statt starrer Stufen:**
   - Verwendung moderner mathematischer CSS-Funktionen: `clamp()`, `min()`, `max()`.
   - Fluid Typography: Schriftgrößen und Zeilenabstände skalieren stufenlos zwischen mobilen Displays und Desktop-Monitoren, ohne harte Sprünge.
   - Fluid Spacing: Abstände (`padding`, `gap`, `margin`) passen sich harmonisch dem Viewport an.
2. **CSS Grid mit inhaltsgetriebener Flexibilität:**
   - Tabellen und Inhaltskacheln nutzen `grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr))`.
   - Flexbox-Layouts müssen bei Platzmangel sauber umbrechen (`flex-wrap`) und dürfen niemals Inhalte abschneiden oder horizontales Scrollen erzwingen.
3. **Container Queries (`@container`) & Moderne CSS-Architektur (`https://github.com/CintaQs/myquests-design-system`):**
   - Wiederverwendbare Komponenten passen ihre Darstellung an die Breite ihres Eltern-Containers an (`container-type: inline-size`), nicht an den gesamten Viewport.
   - Verwendung moderner CSS-Standards (Stand 2027): `min-height: 100dvh` statt veraltetem `100vh`, logische CSS-Eigenschaften (`margin-inline`, `padding-block`, `inset-inline-start`, `border-block-end`), `overflow-x: clip` auf `html`/`body`, `text-wrap: balance` auf Überschriften (`h1`–`h6`) und `text-wrap: pretty` auf Fließtext (`p`, `li`, `td`, `dd`).
   - Dadurch funktioniert dieselbe Komponente nahtlos als Vollbild am Smartphone, als zweispaltiger Block auf der Detailseite und als kompaktes Widget in einer Seitenleiste.

---

## 2. Mobile Responsivität, Null-Overflow-Garantie & Automatisierte Playwright-DOM-Prüfung
- **Schmale Viewports (320px–380px):**
  - Die einhändige mobile Nutzung auf kompakten Smartphones muss uneingeschränkt komfortabel möglich sein.
  - Tabellen, Karten und Formulare dürfen auf 320px-Bildschirmen keinen horizontalen Überlauf erzeugen (`0.00px` Toleranz, siehe Regel 09; Touch-Targets $\ge 44 \times 44\text{px}$ / `2.75rem`, siehe Regel 07).
- **Automatisierte Playwright-Verifikation nach `networkidle`:**
  - Vor jedem Release prüft Playwright das live gerenderte DOM nach `page.waitForLoadState('networkidle')` bei `320px`, `768px` und `1440px` auf `0.00px` horizontalen Überlauf sowie auf identische Y-Startkoordinaten (`boundingBox().y`) nebeneinanderliegender Preiskarten.

---

## 3. Core Web Vitals, Bild- & Font-Performance (`LCP`, `CLS`, `INP`)
1. **Null Layout-Shifts (`CLS = 0.00`):**
   - Jedes `<img>`-, `<svg>`- und Video-Element besitzt zwingend explizite `width`- und `height`-Attribute oder ein festes CSS-`aspect-ratio`, damit der Browser den Platz vor dem Laden exakt reserviert.
2. **Moderne Bildformate & Lade-Priorisierung (`LCP < 1,8 s`):**
   - Rasterbilder werden ausnahmslos als komprimiertes **`WebP`** oder **`AVIF`** ausgeliefert (keine unkomprimierten Megabyte-PNGs/JPEGs).
   - Das primäre Above-the-Fold-Element (Hero-Bild) erhält `loading="eager"` und `fetchpriority="high"`.
   - Alle Bilder unterhalb des sichtbaren Erstbereichs (Below the Fold) erhalten zwingend `loading="lazy"` und `decoding="async"`.
3. **Lokale Font-Performance:**
   - Selbst gehostete `.woff2`-Schriften nutzen `font-display: swap` sowie ein `<link rel="preload" as="font" type="font/woff2" crossorigin>` für den primären Schriftschnitt im `<head>`.
