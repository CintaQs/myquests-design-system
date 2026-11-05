# Richtlinie 07 Barrierefreiheit (WCAG 2.2 AA / BFSG) & Design-System

## Status & Verbindlichkeit
- **Gültigkeit:** Strikt für alle Frontend-Komponenten, Astro-Seiten, HTML-Strukturen und Styles.
- **Priorität:** Hoch / Gesetzliche & ethische Vorgabe (BFSG & BITV 2.0).

---

## 1. Gesetzliche Vorgaben & Normen
Die Plattform unterliegt dem **Barrierefreiheitsstärkungsgesetz (BFSG)** und der **BITV 2.0** (bzw. bei Schweizer Portalen `eCH-0059`).
Alle Seiten müssen die Kriterien der **WCAG 2.2 Level AA** vollständig erfüllen:

1. **Farbkontraste & 2-Schichten-Token-System (`https://github.com/CintaQs/myquests-design-system`):**
   - Normaler Text (`--color-ink-body: #334155` auf `#FFFFFF`/`#F8FAFC`): Mindestkontrast von **4.5:1** gegen den Hintergrund (in unserem System $> 10:1$).
   - Großer Text / Überschriften (`--color-ink-heading: #0F172A`): Mindestkontrast von **3:1** (in unserem System $> 15:1$).
   - UI-Komponenten, Formularrahmen & grafische Objekte: Mindestkontrast von **3:1** nach WCAG 2.2 AA (1.4.11 Non-text Contrast). Formular-Eingabefelder (`.form-input`, `.form-select`, `.form-textarea`) nutzen hierfür verbindlich `--color-border-control` (`#64748B`), da helles `#E2E8F0` nur für dekorative Oberflächengrenzen (`--color-surface-border`) zulässig ist.
   - Farbcodierungen für Statusanzeigen (`Error`, `Warning`, `Success`) müssen immer durch Text, Symbole oder Muster redundant begleitet werden (keine reine Farbinformation).
2. **Lückenlose Tastaturbedienbarkeit, Navigation & Vollständige Zustands-Matrix:**
   - Jedes interaktive Element (Links, Buttons, Formularfelder, Filter) muss über die `Tab`-Taste erreichbar sein.
   - Alle 3 Button-Hierarchien (`.btn-primary`, `.btn-secondary`, `.btn-tertiary`) müssen alle **5 interaktiven Zustände** vollständig abbilden: `Default`, `Hover`, `Active/Pressed` (`translateY(1px)`), `Focus-Visible` (`2px solid var(--color-brand)` mit `2px` Offset) und `Disabled` (`opacity: 0.55; cursor: not-allowed`).
   - Formular-Eingabefelder bilden neben `Default`, `Hover`, `Focus-Visible` und `Disabled` auch den ausgefüllten Zustand (`:not(:placeholder-shown)`) sowie Inline-Validierungszustände (`[aria-invalid="true"]`, `.form-status-error`, `.form-status-warning`, `.form-status-success` mit `role="status"` und `aria-live="polite"`) ab.
   - Der aktive Navigationspunkt im Header wird semantisch und visuell über `aria-current="page"` gekennzeichnet.
   - Modale Dialoge müssen über eine barrierefreie Focus-Trap verfügen und sich mit der `Escape`-Taste schließen lassen.
   - Ein sichtbarer Skip-Link (`.skip-link` mit `z-index: var(--z-skip-link)`) am Dokumentanfang muss direkt zum Hauptinhalt (`#main-content`) springen.
3. **Screenreader-Semantik (ARIA & HTML5):**
   - Lückenlose Überschriftenhierarchie (`h1` $\rightarrow$ `h2` $\rightarrow$ `h3` ohne Auslassungen; genau eine `h1` pro Seite; eine direkt auf `h1` folgende `h2` bleibt für SEO ein `<h2>`, wird aber über `h1 + h2` automatisch als ruhige Lead-Subheadline gestylt).
   - Formularfelder besitzen immer explizite `<label for="...">`-Zuordnungen sowie `aria-invalid` und `aria-describedby` für Fehlermeldungen.
   - Datentabellen nutzen semantische `<table>`-Strukturen mit `<th scope="col">` und tabellarischen Ziffern (`font-variant-numeric: tabular-nums`).
4. **Touch-Targets & Bewegungsreduktion:**
   - Alle Klick- und Touch-Flächen müssen mindestens **44 x 44 px** (`min-height: 2.75rem`) groß sein (WCAG 2.5.5 / 2.5.8).
   - Interaktive Übergänge reagieren verzögerungsfrei (`--duration-interactive: 160ms cubic-bezier(0.22, 1, 0.36, 1)`) bei vollständiger Unterstützung von `@media (prefers-reduced-motion: reduce)`.

---

## 2. Verpflichtende Barrierefreiheitserklärung (§ 12 BFSG)
- Jede öffentliche Website stellt eine im Footer verlinkte **Barrierefreiheitserklärung (`/barrierefreiheit`)** bereit.
- Diese dokumentiert den Stand der Vereinbarkeit mit den Anforderungen der BITV 2.0 / EN 301 549, bietet einen barrierefreien Feedback-Kanal zur Meldung von Barrieren und nennt die zuständige Marktüberwachungsbehörde der Länder für die Barrierefreiheit von Produkten und Dienstleistungen (MLBF).
