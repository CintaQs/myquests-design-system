# Richtlinie 02 Vollständiges Verbot von Inline-Styles

## Status & Verbindlichkeit
- **Gültigkeit:** Strikt für alle Komponenten, Templates (Astro, React, Svelte, Vue), HTML-Elemente und Markdown.
- **Priorität:** Hoch / Codequalität, Wartbarkeit & Design-System-Konsistenz.

---

## 1. Verbotstatbestand
Die Verwendung von Inline-Styles über Attribute wie `style="..."` (HTML/Astro) oder `style={{ ... }}` (React/JSX) ist **vollständig untersagt**.

- Statische Abstände, Farben, Schriftgrößen, Breiten, Flexbox-Definitionen oder Versteck-Mechanismen (z. B. Honeypots mit `style="display:none"`) im `style`-Attribut sind **ausnahmslos verboten**.
- Einzige eng begrenzte Ausnahme: Rein mathematisch zur Laufzeit berechnete Koordinaten bei dynamischen Canvas-/Chart-Visualisierungen, sofern diese technisch nicht über Tailwind-Klassen oder CSS-Variablen im Design-System abbildbar sind.

---

## 2. Erlaubte Architektur im Globalen Design-System (`myquests-design-system`)
Maßgeblicher Agentur-Leitfaden für alle Projekte ist das zentrale Repository **`https://github.com/CintaQs/myquests-design-system`** sowie die lokale Implementierung in `Website/src/styles/global.css`.

Jegliches Styling muss über dieses zentrale Design-System erfolgen:

1. **Verbot von Utility-Klassen-Bloat (Smell-Code):**
   Sich ständig wiederholende lange Utility-Klassen-Ketten in `.astro`- oder `.tsx`-Dateien sind ebenso verboten wie Inline-Styles. Komponenten nutzen die zentralen semantischen Systemklassen aus `global.css` (`.section-white`, `.section-muted`, `.container-layout`, `.grid-intrinsic-2`, `.grid-intrinsic-3`, `.grid-asymmetric-split`, `.card-surface`, `.card-muted`, `.card-highlight`, `.card-header-aligned`, `.btn-primary`, `.btn-secondary`, `.btn-tertiary`, `.form-input`, `.data-table`, `.faq-editorial-grid`).
2. **Zwei-Schichten-Token-System (`@theme` in `global.css`):**
   - **Schicht 1 (`Core Palette`):** Rohe Farbwerte mit gedämpfter Sättigung (`< 80 %`, 0 Zirkusfarben).
   - **Schicht 2 (`Semantische Color-System-Tokens`):** Komponenten und Systemklassen binden ausschließlich an semantische Rollen (`--color-surface-*`, `--color-border-*`, `--color-brand*`, `--color-ink-*`, `--color-icon-*`) und niemals an rohe Hex-Werte.
   - **Schicht 3 (`Spacing, Radius, Z-Index & Typografie`):** Mathematische 4px-/8px-Skala (`--space-0` bis `--space-900`), konzentrische Eckenradien (`--radius-card: 4px`, `--radius-sm: 2px` nach der Formel $\text{inner radius} = \max(2\text{px}, \text{outer radius} - \text{gap})$), zentrale Z-Index-Tokens (`--z-header: 20`, `--z-skip-link: 50`) und intrinsische `clamp()`-Skalen.

---

## 3. Umsetzung technischer Spezialfälle ohne Inline-Styles & ohne Utility-Bloat

### A. Komponenten-Styling über semantische Systemklassen
```astro
<!-- Richtig (Sauberes zentrales Design-System aus global.css, 0 Inline-Styles, 0 Utility-Bloat) -->
<article class="card-surface">
  <div class="card-header-aligned">
    <h3 class="title-card">Kennzahlenübersicht</h3>
    <p class="price-figure">ab CHF 6'580.–</p>
  </div>
  <a href="/kontakt" class="btn-primary">Projekt anfragen</a>
</article>

<!-- Falsch (Strikt verboten: Inline-Styles oder aufgeblähte Utility-Ketten mit Schatten) -->
<div style="display:flex; flex-direction:column; gap:16px; padding:24px; background:#fff;">
  <h3 style="font-size:18px; font-weight:bold; color:#111827;">Kennzahlenübersicht</h3>
</div>
```

### B. Unsichtbare Hilfselemente (z. B. Bot-Honeypots)
Honeypots oder Screenreader-Hilfselemente werden ausschließlich über globale Utility-Klassen (`global.css` oder Tailwind `sr-only`) gesteuert:
```astro
<!-- Richtig -->
<input
  type="text"
  name="b_company_url"
  tabindex="-1"
  autocomplete="off"
  aria-hidden="true"
  class="honeypot-trap"
/>

<!-- Falsch (Strikt verboten) -->
<input
  type="text"
  style="display:none !important; position:absolute; left:-9999px;"
/>
```
