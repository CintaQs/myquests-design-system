# Richtlinie 12 Visuelle Verbote & Vermeidung von generischen Stock-AI-UI-Mustern

## Status & Verbindlichkeit
- **Gültigkeit:** Strikt verbindlich für alle UI-Komponenten, Landingpages, Layouts, Farbkonzepte, Icons, Badges, Buttons und visuellen Strukturen.
- **Prinzip:** „To avoid generic stock AI UI patterns“ – Keine austauschbaren KI-Klischee-Designs, kein Neon-Zirkus und kein Kirmes-Effekt, sondern handwerklich exzellente, seriöse Fachportal- und Marken-Ästhetik.

---

## 1. Striktes Verbot greller Zirkusfarben, des „Kirmes-Effekts“ & generischer KI-UI-Klischees

Folgende Design-Muster zerstören die Seriosität einer professionellen Website und sind **ausnahmslos und strikt verboten**:

1. **Absolutes Verbot greller Neon- und Zirkusfarben:**
   - Grelle Zirkusfarben (wie `#CCFF00`, Neon-Gelb, Giftgrün, Textmarker-Grün, schrilles Magenta oder grelles Cyan) sowie bunte Zirkus-Fokusringe sind im gesamten Design-System ausnahmslos verboten.
   - Sie bieten auf hellen Flächen keinen ausreichenden Kontrast nach WCAG 2.2 AA und wirken unprofessionell.
   - Für Tastatur-Fokusringe (`*:focus-visible`) gilt stattdessen ein klarer, hochkontrastreicher Dual- oder Slate-Ring (mindestens 3:1 Kontrast auf allen Hintergründen).

2. **Striktes Verbot des „Kirmes-Effekts“ (Color- & Banner-Chaos):**
   - Es ist ausnahmslos verboten, Seiten wie einen „zusammengewürfelten Haufen“ wirken zu lassen.
   - Kein Aufeinanderprallen aggressiver, bunter Fremdmarken- oder Signalfarben (Cyan, Blau, Grün, Rot, Regenbogen-Verläufe nebeneinander).
   - Alle Aktionen, Badges und Verweise müssen sich harmonisch, ruhig und farblich diszipliniert in das Design-System einfügen. Pro Ansicht bzw. Sektion gibt es immer nur **einen einzigen dominanten Haupt-CTA**.

3. **Striktes Verbot des `Sparkles`-Icons (und generischer KI-Glitzer-/Zauberstab-Icons):**
   - Das `Sparkles`-Icon (sowie `Wand2`, `Bot` oder KI-Sterne-Icons aus `lucide-react` / `lucide-astro` bzw. der SVG-Pfad `m12 3-1.912 5.813`) ist auf der gesamten Website **ausnahmslos und strikt verboten**.
   - Stattdessen sind sachliche, fachbezogene Icons (`Scale`, `ShieldCheck`, `FileText`, `Search`, `SlidersHorizontal`, `AlertTriangle`, `CheckCircle2`, `Building2`) zu nutzen.

4. **Semantische Rollentrennung: Verbot von Button-Styling auf passiven Badges (Affordance-Regel):**
   - **Action Surfaces (Interaktive Buttons & Links):** Besitzen exklusive Vollflächen-Akzentfarben, klares Hover-/Active-Feedback, `cursor: pointer`, Touch-Target-Mindesthöhe ($\ge 44\text{px}$) und **imperative Handlungsverben** (*„Jetzt berechnen“*, *„Details prüfen“*).
   - **Informational Surfaces (Passive Badges, Pills, Tags & Labels):** Dienen der reinen Daten- und Statusanzeige. Für sie gilt:
     - **STRIKTES SCHATTEN-VERBOT (`box-shadow: none !important`):** Passive Badges dürfen niemals einen 3D- oder Drop-Shadow tragen, der Klickbarkeit suggeriert.
     - **Kein Vollton-Primär-CTA-Look:** Passive Labels nutzen dezente Tint-Hintergründe mit dunkler, barrierefreier Textfarbe (Kontrast $\ge 4.5:1$, idealerweise AAA $\ge 7:1$) oder flache Ghost-Rahmen.
     - **Keine Pseudo-Interaktion:** Niemals Hover-Translation, niemals `cursor: pointer`, niemals `role="button"` oder `tabindex="0"` auf statischen Badges.
     - **Verbot von Handlungsverben auf Badges:** Auf nicht-klickbaren `<div>`- oder `<span>`-Elementen sind Handlungsaufforderungen (*„Jetzt öffnen“*, *„Ansehen“*) strengstens verboten (*Zero Dead Clicks*).

5. **Absolutes Glasmorphismus-Verbot (`0 %` Glassmorphism) & Keine diffusen Gradient-Blobs:**
   - **0 % Glasmorphismus:** Verboten sind jegliche `backdrop-filter: blur(...)`-Effekte, Milchglas-Header, halbtransparente überlagernde Flächen und weiche Deko-Schatten (`box-shadow: none`). Alle Oberflächen (`.site-header`, `.card-surface`, `.card-muted`, `.card-highlight`) sind zu 100 % opak und werden durch präzise `1px`-Haarlinien (`--color-surface-border`) abgegrenzt.
   - Verboten sind giftige Neon-Glows, fluoreszierende Ränder, übertriebene leuchtende Box-Shadows („SaaS-AI-Glow“), Farbverläufe auf Überschriften (`no gradient text`) sowie schwebende violette, pinke oder cyanfarbene Farbkleckse im Hintergrund (`blur-3xl bg-purple-500/20`).
   - Hintergründe bleiben sauber, ruhig und lesefreundlich: Reines Weiß (`#FFFFFF`) oder helles Schiefergrau (`#F8FAFC`).

6. **Verbot von Eyebrow-Pill-Badges, einseitigen Karten-Balken & dekorativer Schein-Nummerierung:**
   - **Keine Eyebrow-Pill-Badges oberhalb von Überschriften (`no eyebrow pill tags`):** Kleine umrahmte Pillen-Boxen über jeder `H2` wirken wie ein Baukasten-Klischee. Für den Markt- oder Seitenkontext wird ausschließlich die rahmenlose, rein typografische Dachzeile `.context-kicker` eingesetzt – und zwar **exklusiv einmalig im Seiten-Hero**, niemals repetitiv über jeder Sektions-`H2`.
   - **Keine einseitigen Karten-Akzentbalken (`border-left: 4px`):** Alle Karten besitzen einen umlaufenden `1px`-Rahmen (`border: 1px solid var(--color-surface-border)` bzw. `--color-brand-border`).
   - **Disziplin bei Nummerierungen (`01 / 02 / 03`):** Nummerierte Marker (`1.`–`4.` bzw. `01`–`40`) sind strikt für echte chronologische oder logische Abläufe reserviert (z. B. 4-Wochen-Projektplan, 40-Punkte-Checkliste, Top-10-Fehler) und dürfen niemals als dekorative Ziffern auf gleichrangigen Leistungskarten stehen.
   - **Einheitliche SVG-Linienstärke:** Alle zulässigen Icons innerhalb einer Ansicht nutzen exakt dieselbe Strichstärke (`.icon-svg { width: 1.25rem; height: 1.25rem; stroke-width: 1.75; }`).
   - Verboten sind unruhige Mesh-Hintergründe (`.bg-mesh`), künstliche Noise-Overlays (`.noise-overlay`), dekorative Dot-Grids (`.bg-dots`) und Text-Shimmer-Effekte (`.text-shimmer`).

7. **Kein inhaltsleeres „Bento-Grid-Copycatting“ & kein US-SaaS-Template-Look:**
   - Verboten ist das wahllose Aneinanderreihen von ungleich großen Bento-Karten nur des optischen Effekts wegen sowie verspielte Cartoon-Vektoren, 3D-Plastik-Objekte und substanzlose Buzzwords („Supercharge your workflow with AI“).

8. **Verbot von faulen Text-Ellipsen (`...` / `truncate`) & Verbot von Widget-Redundanzen:**
   - Wichtige Bezeichnungen, Pflichtangaben, Fachdaten und Überschriften dürfen niemals durch faule CSS-Truncation (`truncate`, `text-ellipsis`, `...`) abgeschnitten und unlesbar gemacht werden. Das Layout muss über intrinsische Typografie (`clamp()`) und sauberen Zeilenumbruch den gesamten Fakt darstellen.
   - Auf einer Seite dürfen niemals zwei Widgets oder Sektionen dieselben Daten redundant doppelt anzeigen.

---

## 2. Gebot des maßgeschneiderten Fach- und Editorial-Designs (Editorial Excellence)

1. **Sachliche Gravitas:**
   - Typografie, Abstände und Tabellen orientieren sich an hochwertigen Fachpublikationen und Institutionen.
2. **Klarheit vor Effekthascherei:**
   - Echte Fakten, Messwerte, Leistungen und Rechtsgrundlagen stehen unangefochten im Vordergrund.
3. **Barrierefreie Farbkodierung:**
   - Farben unterstützen die Orientierung, drängen sich aber niemals vor die Fakten und sind stets durch klare Text-Labels begleitet.
