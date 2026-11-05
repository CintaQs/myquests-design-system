---
name: myquests-design-system
description: Offizieller MyQuests Digital Design-Leitfaden (https://github.com/CintaQs/myquests-design-system). Aktivieren bei Konzeption, UI/UX-Design, Astro/React-Komponenten, CSS-Architektur, Typografie und Qualitätsprüfung für alle Web-Plattformen der Agentur.
---

# MyQuests Digital Design System (`myquests-design-system`)

Dieser Skill definiert die verbindlichen Design-, Typografie-, Farb-, Abstands- und Komponenten-Regeln für alle Web-Plattformen von **MyQuests Digital (Olivier Jacob)**.

## 1. Unverhandelbare Grundregeln

1. **Sauber, edel, minimalistisch & intrinsisch (`0 %` Glasmorphismus):**
   - Alle Oberflächen sind zu `100 %` opak (`#FFFFFF`, `#F8FAFC`, `#F1F5F9`).
   - `backdrop-filter: blur(...)` und `backdrop-blur-*` sind in Navigation, Karten, Formularen und Bannern ausnahmslos verboten.
2. **Kein Inline-CSS & kein Utility-Bloat (Smell-Code):**
   - `style="..."` und `style={{ ... }}` sind verboten (für Honeypot-Felder `.honeypot-trap` nutzen).
   - Wiederkehrende Komponenten nutzen die semantischen Klassen aus `styles/global.css` (`.container-layout`, `.section-white`, `.section-muted`, `.card-surface`, `.card-highlight`, `.card-header-aligned`, `.btn-primary`, `.btn-secondary`, `.btn-tertiary`, `.data-table`, `.faq-editorial-grid`).
3. **2-Schichten-Farb-Tokens & WCAG 2.2 AA:**
   - Schicht 1 (`--palette-*`): Gedämpfte Rohwerte (`< 80 %` Sättigung, `0` Zirkusfarben, kein `#CCFF00`).
   - Schicht 2 (`--color-*`): Semantische Rollen für Surface, Border, Action, Ink und Icon.
   - Textkontrast $\ge 4.5:1$ (in der Praxis `> 10:1`), Formular-Rahmenkontrast $\ge 3:1$ (`--color-border-control: #64748B`).
4. **Mathematische Spacing-Skala & Konzentrische Eckenradien:**
   - 4px-/8px-Skala (`--space-0` bis `--space-900`).
   - Sektionen nutzen optische Boden-Balance (`padding-block-end: calc(var(--space-section) * 1.1)`).
   - Äußere Karten/Tabellen: `--radius-card: 4px`; innere Buttons/Inputs/Badges: `--radius-sm: 2px`.
   - Zentrale Z-Index-Tokens: `--z-header: 20`, `--z-skip-link: 50`.
5. **Funktionale 5-Gruppen-Typografie & Zeilenlängen (`ch`):**
   - Lokal gehostete Variable-Schrift `Inter` (`/fonts/inter-var-latin.woff2`, `font-display: swap`).
   - Erlaubte Schriftstärken: `400`, `500`, `600`, `700` (Bold). Verbot von `800` (ExtraBold), `900` (Black) und Kursivschrift (`font-style: normal`).
   - Zeilenbreiten: `32ch` für `h1`, `48ch` für Sektions-`h2`, `65ch` für `h1 + h2` und `.prose-measure`.
   - Zahlen & Preise: `font-variant-numeric: tabular-nums`.
   - `H1`-Vertrag: Kein `:`, kein `?`, kein Schlusspunkt `.`, keine Jahreszahl-Klammern `[2026]`.
6. **Komponenten-Harmonie & Anti-Monotonie:**
   - **Karten-Ausrichtung:** `.card-header-aligned` synchronisiert die Y-Startlinie von Leistungslisten; kein `transform: scale()` auf hervorgehobenen Karten (*No Three Towers*).
   - **Offenes FAQ-Raster:** `.faq-editorial-grid` (2 Spalten, offen scannbar mit `1px`-Oberkante `.faq-item`) statt versteckter Chevron-Akkordeons.
   - **Dachzeilen-Disziplin:** `.context-kicker` ausschließlich 1x im Seiten-Hero über `H1`, niemals repetitiv über jedem Sektions-`H2`.
   - **Asymmetrischer Rhythmus:** Abwechslung zwischen `.grid-asymmetric-split`, `.data-table`, `.grid-intrinsic-2` und `.grid-intrinsic-3`.
7. **Visuelle & Sprachliche Sperrliste:**
   - `0 %` Emojis, `0 %` Geviertstriche (`U+2014`), keine `Sparkles`/`Wand2`-Icons, kein `bg-clip-text`, keine einseitigen Karten-Seitenbalken (`border-left`), kein US-Beraterjargon (`C-Level`, `Cutover`, `Quick-Wins`, `Staging`).
