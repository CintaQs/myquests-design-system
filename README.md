# MyQuests Digital Design System

Offizieller, verbindlicher Design-, Typografie-, Layout- und Komponenten-Leitfaden für alle Web-Plattformen von **MyQuests Digital (Olivier Jacob)**.

- **Repository:** `https://github.com/CintaQs/myquests-design-system`
- **Master-Template im Workspace:** `00_dummy` (`Website/src/styles/global.css` & `.agents/rules/`)
- **Grundprinzip:** Sauber, edel, minimalistisch, intrinsisch – `0 %` Glasmorphismus, `0` HTML-Inline-Styles, `0` Utility-Bloat (Smell-Code), `100 %` WCAG 2.2 AA & Privacy by Design.

---

## 1. Design-Philosophie & Visuelle Identität

Unsere Websites richten sich an kaufmännische und technische Entscheider im DACH-Raum (Deutschland & Schweiz). Das Design folgt einer ruhigen, präzisen Schweizer Editorial-Disziplin:

1. **100 % Opake Oberflächen (`0 %` Glasmorphismus):**
   - Keine halbtransparenten Karten, kein Milchglas-Header (`backdrop-filter: blur(...)` und `backdrop-blur-*` sind ausnahmslos verboten).
   - Alle Sektionen, Karten, Tabellen und Formulare stehen auf klaren, opaken Flächen (`#FFFFFF`, `#F8FAFC`, `#F1F5F9`), getrennt durch präzise `1px`-Haarlinien (`#E2E8F0`).
2. **Alternierender Sektions-Rhythmus mit optischer Boden-Balance:**
   - Vertikale Sektionen wechseln konsequent zwischen `.section-white` (`#FFFFFF`) und `.section-muted` (`#F8FAFC`).
   - Damit Inhalte am Sektionsende nicht optisch nach unten durchhängen, ist der untere Innenabstand jeder Sektion exakt `10 %` größer als der obere (`padding-block-start: var(--space-section)`, `padding-block-end: calc(var(--space-section) * 1.1)`).
3. **Semantische Komponenten-Klassen statt Smell-Code:**
   - HTML- und Astro-Templates bleiben schlank und lesbar. Wiederholte Styling-Ketten werden über die semantischen Klassen in `styles/global.css` (`.container-layout`, `.card-surface`, `.btn-primary`, `.data-table`, `.faq-editorial-grid`) abgebildet.
   - `style="..."` und `style={{ ... }}` sind im gesamten UI-Code verboten.

---

## 2. 2-Schichten-Farb-Architektur (`Core Palette` & `Color System`)

Kein Komponenten-CSS verwendet rohe Hex-Werte. Alle Farben laufen über zwei klar getrennte Token-Schichten in `@theme`:

### Schicht 1 – `Core Palette` (Gedämpfte Rohwerte, `< 80 %` Sättigung)
| Token | Hex-Wert | Beschreibung |
| :--- | :--- | :--- |
| `--palette-navy-800` | `#1E3A8A` | Primäre Marken- und Interaktionsfarbe (Sättigung `64 %`) |
| `--palette-navy-900` | `#172554` | Abgedunkelter Hover-Zustand |
| `--palette-navy-700` | `#1D4ED8` | Aktiver Klick-Zustand (`:active`) |
| `--palette-navy-50` | `#EFF6FF` | Ruhige Marken-Akzentfläche |
| `--palette-navy-200` | `#BFDBFE` | Rahmenfarbe für hervorgehobene Karten (`.card-highlight`) |
| `--palette-slate-00` | `#FFFFFF` | Primäre Hintergrundfläche |
| `--palette-slate-50` | `#F8FAFC` | Sekundäre Hintergrundfläche (`.section-muted`, `.card-muted`) |
| `--palette-slate-100` | `#F1F5F9` | Subtile Hervorhebungsfläche (Tabellenkopf, passive Badges) |
| `--palette-slate-200` | `#E2E8F0` | Standard-Haarlinie (`1px`) für Sektionen und Karten |
| `--palette-slate-300` | `#CBD5E1` | Verstärkte Trennlinie unter Tabellenköpfen |
| `--palette-slate-500` | `#64748B` | Kontraststarker Rahmen für Formularfelder ($\ge 3:1$ gegen `#FFFFFF`) |
| `--palette-slate-600` | `#475569` | Gedämpfter Sekundär- und Metatext ($\ge 7:1$ Kontrast) |
| `--palette-slate-700` | `#334155` | Primärer Fließtext (`> 10:1` Kontrast) |
| `--palette-slate-900` | `#0F172A` | Überschriften- und Primär-Icon-Farbe (`> 15:1` Kontrast) |

### Schicht 2 – Semantische `Color System`-Rollen
- **Surface:** `--color-surface-white`, `--color-surface-muted`, `--color-surface-subtle`, `--color-surface-error`, `--color-surface-warning`, `--color-surface-success`
- **Border:** `--color-surface-border`, `--color-surface-border-strong`, `--color-border-control`, `--color-brand-border`, `--color-border-error`, `--color-border-warning`, `--color-border-success`
- **Action / Brand:** `--color-brand`, `--color-brand-dark`, `--color-brand-active`, `--color-brand-light`
- **Text / Ink:** `--color-ink-heading`, `--color-ink-body`, `--color-ink-muted`, `--color-ink-inverted`, `--color-ink-error`, `--color-ink-warning`, `--color-ink-success`
- **Icon:** `--color-icon-default`, `--color-icon-secondary`, `--color-icon-brand`

---

## 3. Mathematische Spacing-Skala, Konzentrische Radien & Z-Index-Tokens

### 4px-/8px-Spacing-Skala
| Token | Wert (`rem`) | Pixel-Äquivalent | Typischer Einsatzbereich |
| :--- | :--- | :--- | :--- |
| `--space-0` | `0px` | `0px` | Reset |
| `--space-25` | `0.125rem` | `2px` | Mikro-Abstand in passiven Badges |
| `--space-50` | `0.25rem` | `4px` | Abstand zwischen Label und Input / Kicker und H1 |
| `--space-75` | `0.5rem` | `8px` | Vertikales Button- und Input-Padding |
| `--space-100` | `0.75rem` | `12px` | Kompakter Innenabstand, Tabellen-Zellen vertikal |
| `--space-200` | `1rem` | `16px` | Standard-Elementabstand, Header-Padding |
| `--space-300` | `1.5rem` | `24px` | Abstand zwischen Formulargruppen (`.form-stack`) |
| `--space-400` | `2rem` | `32px` | Abstand im offenen 2-Spalten-FAQ-Raster |
| `--space-500` bis `--space-900` | `2.5rem` bis `6rem` | `40px` bis `96px` | Große Layout- und Sektionsabstände |

### Konzentrische Eckenradien (Nested Radius Formula)
- **Äußere Container (`.card-surface`, `.card-muted`, `.card-highlight`, `.data-table-wrap`):** `--radius-card: 4px`
- **Innere Elemente (`.btn-primary`, `.btn-secondary`, `.form-input`, `.badge-passive`):** `--radius-sm: 2px`
- Keine großen Pill-Radien (`rounded-full`) auf Karten, Buttons oder Badges.

### Zentrale Z-Index-Tokens
- `--z-header: 20` (Kopfleiste)
- `--z-skip-link: 50` (Barrierefreier Skip-Link bei Tastaturfokus)

---

## 4. Funktionale 5-Gruppen-Typografie & Zeilenlängen (`ch`-Measure)

Wir nutzen ausschließlich die lokal vom eigenen Server ausgelieferte Variable-Schrift `Inter` (`/fonts/inter-var-latin.woff2`, `font-display: swap`).

1. **Schriftstärken- & Stil-Disziplin:**
   - Erlaubt sind ausschließlich `400` (Regular), `500` (Medium), `600` (SemiBold) und `700` (Bold).
   - **Verbot von `800` (ExtraBold) und `900` (Black):** Wirkt plakativ und unruhig.
   - **Verbot von Kursivschrift (`0 %` Italic):** `font-style: normal` gilt global für alle Elemente.
2. **Die 5 funktionalen Textgruppen:**
   - **Heading (`h1`, `h2`, `h3`):** `font-weight: 700` (bzw. `600` bei `h3`), `line-height: 1.22`, `letter-spacing: -0.015em`, `text-wrap: balance`.
   - **Title (`.title-card`, `.footer-heading`, `.brand-link`):** `font-weight: 600`–`700` für Karten- und Modultitel.
   - **Body (`body`, `.body-lead`, `h1 + h2`):** `font-size: clamp(1rem, 0.96rem + 0.18vw, 1.0625rem)`, `line-height: 1.65`, `text-wrap: pretty`. Die direkt auf `h1` folgende `h2` (`h1 + h2`) bleibt für Suchmaschinen ein echtes `<h2>`, wird aber optisch als ruhiger Lead-Vorspann (`font-weight: 400`, `--font-size-lead`) dargestellt.
   - **Button (`.btn-primary`, `.btn-secondary`, `.btn-tertiary`):** `0.9375rem`, `font-weight: 600`, Mindesthöhe `2.75rem` (`44px` Touch-Target).
   - **Caption (`.text-meta`, `.context-kicker`, `.badge-passive`):** `0.75rem`–`0.8125rem`.
3. **Verbindliche Zeilenlängen (`ch`-Measure) & Tabular Numerals:**
   - `h1`: `max-width: 32ch` (verhindert einzeilige Textwände und Umbrüche über 3–4 Zeilen bei deutschen Komposita).
   - Sektions-`h2`: `max-width: 48ch`.
   - `h1 + h2` & `.prose-measure`: `max-width: 65ch`.
   - Preise (`.price-figure`) und Datentabellen (`.data-table`): `font-variant-numeric: tabular-nums`.
4. **H1-Formatierungs-Vertrag:**
   - Kein Doppelpunkt (`:`), kein Fragezeichen (`?`), kein Schlusspunkt (`.`) und keine Jahreszahl-Klammern (`[2026]`) in `<h1>`.

---

## 5. Komponenten-Standards & Anti-Monotonie-Regeln

1. **Asymmetrischer Rhythmus statt 3-Karten-Monotonie:**
   - Niemals zwei identische 3-Spalten-Karten-Raster direkt untereinander platzieren.
   - Abwechslung zwischen `.grid-asymmetric-split` (`1fr 1.35fr`), `.data-table`, `.grid-intrinsic-2` und `.grid-intrinsic-3`.
2. **Y-Achsen-Synchronisation in Preis- und Vergleichskarten (`.card-header-aligned`):**
   - In nebeneinanderstehenden Karten sorgt `.card-header-aligned` (`min-height: 7.5rem`) dafür, dass die Aufzählungslisten (`<ul>`) und Fuß-Buttons auf exakt derselben horizontalen Y-Linie starten.
   - Hervorgehobene Karten (`.card-highlight`) nutzen ausschließlich `--color-surface-muted` und `--color-brand-border` – niemals `transform: scale(...)` oder künstliche Höhenunterschiede (*No Three Towers*).
3. **Offenes 2-Spalten-Editorial-FAQ-Raster (`.faq-editorial-grid`):**
   - Häufige Fragen werden nicht hinter klickpflichtigen Chevron-Akkordeons versteckt, sondern als offenes, sofort scannbares 2-Spalten-Editorial-Raster mit `1px`-Oberkante (`.faq-item`) gerendert.
4. **Sparsamkeit bei Dachzeilen (`.context-kicker`) & Nummerierungen:**
   - `.context-kicker` wird maximal **einmalig im Seiten-Hero** über der `H1` eingesetzt, niemals repetitiv über jedem Sektions-`H2`.
   - Vorangestellte Nummern (`01`, `02`, `03`) sind ausschließlich für echte chronologische Abläufe und Prüflisten erlaubt, niemals für ungeordnete Vorteile.

---

## 6. Visuelle & Sprachliche Sperrliste (Zero-Tolerance)

- **0 % Emojis** in Code, UI, Markdown und Commits.
- **0 % Geviertstriche (`U+2014`)** oder doppelte Bindestriche (`--`) im Fließtext; ausschließlich deutsche Halbgeviertstriche (`–`, `U+2013`) mit Leerzeichen.
- **0 % Zirkusfarben & Glitzer-Icons:** Kein `#CCFF00`, keine `Sparkles`-, `Wand2`- oder `Bot`-Icons, kein `bg-clip-text`, kein `.bg-mesh` oder `.noise-overlay`.
- **0 % US-Beraterjargon & KI-Floskeln:** Kein `C-Level`, `Cutover`, `Quick-Wins`, `Staging`, `Gamechanger`, `Revolution` oder `State-of-the-Art`.
