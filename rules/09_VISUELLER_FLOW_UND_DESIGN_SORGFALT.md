# Richtlinie 09 Visueller Flow, Ästhetik & Design-Sorgfalt

## Status & Verbindlichkeit
- **Gültigkeit:** Strikt für alle Benutzeroberflächen, Layouts, Typografie und Interaktionen.
- **Priorität:** Hoch / Nutzererlebnis & Seriosität.

---

## 1. Grundsatz (`https://github.com/CintaQs/myquests-design-system`)
Das Visuelle, der **Visual Flow** (Blickführung, Weißräume, typografischer Rhythmus) und das Design sind von elementarer Bedeutung und folgen verbindlich unserem zentralen Agentur-Leitfaden **`https://github.com/CintaQs/myquests-design-system`**. Es reicht niemals aus, dass eine Seite nur technisch funktioniert; sie muss sauber, edel und minimalistisch wirken (`0 %` Glasmorphismus), Ruhe und Autorität ausstrahlen und eine intuitive Nutzerführung bieten.

---

## 2. Kernkriterien für den visuellen Flow & Edel-Minimalismus

1. **Alternierender Sektions-Rhythmus (Cadence) & Optische Vertikal-Balance:**
   - Um visuelle Ermüdung zu vermeiden und maximale Übersichtlichkeit zu gewährleisten, folgen Seiten einem harmonisch wechselnden Kontrast-Rhythmus zwischen reinem Weiß (`.section-white`, `#FFFFFF`) und subtilem Schiefer-Canvas (`.section-muted`, `#F8FAFC`) mit klar abgegrenzten Karten (`#FFFFFF`).
   - Für ein optisch ausgewogenes Ruhen der Sektionsinhalte vor der unteren `1px`-Haarlinie ist der untere Innenabstand leicht größer als der obere (`padding-block-start: var(--space-section); padding-block-end: calc(var(--space-section) * 1.1);`).

2. **Funktionale 5-Gruppen-Typografie, Intrinsische `ch`-Zeilenbreiten & `tabular-nums`:**
   - **Maximale Schriftstärke `700` (Bold) & `0 %` Kursivschrift:** Keine klobigen `800`/`900` Ultra-Bold-Schnitte und kein `italic` (`font-style: normal`).
   - **Intrinsische Zeichenbreiten (`ch`) statt starrer Pixelwerte:** `max-width: 32ch` für `h1` (damit deutsche Komposita in 1 bis 2 Zeilen harmonisch umbrechen), `max-width: 48ch` für Sektions-`h2` und `max-width: 65ch` für die erklärende Hero-Subheadline (`h1 + h2`) sowie `.prose-measure` (Fließtext).
   - **Textausgleich & Tabellarische Ziffern:** `text-wrap: balance` bei Überschriften, `text-wrap: pretty` bei Fließtext sowie `font-variant-numeric: tabular-nums` auf allen Preisangaben (`.price-figure`) und Datentabellen (`.data-table`).

3. **Konzentrische Eckenradien, Umlaufende `1px`-Haarlinien & Y-Achsen-Synchronisation:**
   - **Konzentrische Radien-Formel ($\text{inner radius} = \max(2\text{px}, \text{outer radius} - \text{gap})$):** Äußere Karten und Tabellen nutzen `--radius-card: 4px`, innere Buttons, Badges und Eingabefelder nutzen `--radius-sm: 2px`.
   - **Synchronisierte Y-Startlinie in Karten (`.card-header-aligned`) & Verbot künstlicher Preistürme (`no three towers`):** Nebeneinanderliegende Karten richten Titel, Preise, den ersten Punkt der Leistungsliste (`<ul>`) und den unteren Handlungsbutton exakt auf derselben horizontalen Y-Achse aus. Empfohlene Preiskarten nutzen `.card-highlight` (`1px`-Rahmen in `--color-brand-border`) ohne künstliche Höhenskalierung (`transform: scale(...)` ist verboten).
   - **Asymmetrische Splits & Offenes 2-Spalten-Editorial-FAQ-Raster:** Neben 2er-/3er-Rastern sorgen `.grid-asymmetric-split` (`1fr 1.35fr`), `.divider-hairline` (`1px`-Trennlinie) und das offene 2-Spalten-FAQ-Raster (`.faq-editorial-grid` & `.faq-item` ohne zugeklappten Akkordeon-Klickzwang) für einen ruhigen, buchtypografischen Lesefluss.

4. **Farbdisziplin (`< 80 %` Sättigung) & Kontrast-Harmonie:**
   - Eine einzige primäre Marken-Akzentfarbe mit gedämpfter Sättigung (`< 80 %`, z. B. Marineblau `#1E3A8A`) sorgt für seriöse Ruhe (**striktes Verbot greller Zirkusfarben** wie `#CCFF00` oder eines bunten **„Kirmes-Effekts“**).
   - Pro Ansicht bzw. Sektion gibt es immer nur **einen einzigen dominanten Haupt-CTA**.

5. **Weißräume, Container-Symmetrie & Fluchtlinien:**
   - Mathematische 4px-/8px-Spacing-Skala (`--space-0` bis `--space-900`).
   - TopBar, Breadcrumb-Leiste, Header und Inhaltssektionen müssen exakt dieselbe Container-Breite (`.container-layout`) und identische horizontale Fluchtlinien nutzen.
   - Keine gedrängten Tabellen, keine abgeschnittenen Kernfakten (`truncate`-Verbot bei wichtigen Angaben) und keine unübersichtlichen Textblöcke.

6. **Responsive Reflow & 0.00px Overflow-Garantie:**
   - Horizontales Überlaufen (`overflow-x`) ist auf allen Viewports (320px bis 4K) **strikt verboten (0.00px Toleranz)**.
   - Jede Komponente muss auf Smartphones (320px–430px), Tablets (768px–1024px) und Desktop (1440px–2560px) visuell perfekt ausbalanciert sein.
