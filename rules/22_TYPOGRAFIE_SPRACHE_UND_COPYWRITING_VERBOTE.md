# Richtlinie 22 Typografie-, Sprach-, Überschriften- & Copywriting-Verbote

## Status & Verbindlichkeit
- **Gültigkeit:** Strikt verbindlich für alle Seitentitel, Überschriften (`H1`–`H6`), Fachartikel, Analysen, UI-Texte, Metadaten (`title`, `description`) und Schema.org-Texte.
- **Priorität:** Kritisch / Redaktionelle Exzellenz & Markenintegrität.

---

## 1. Strikter H1-Formatierungs-Vertrag (Doppelpunkt-, Fragezeichen- & Mehr-Satz-Verbot)

Für sämtliche `H1`-Überschriften (Startseite, Kategorieseiten, Detailseiten, Lexikon- und Ratgeberseiten) gilt ein unverletzlicher typografischer und grammatikalischer Standard:

1. **Absolutes Doppelpunkt-Verbot (`:`):**
   - Doppelpunkte in `H1`-Überschriften und Haupttiteln sind **ausnahmslos verboten**.
   - Synthetische KI-Konstruktionen nach dem Muster *„Thema: Untertitel“* sind unzulässig. Der Gedanke muss stets in einem einzigen, flüssigen grammatikalischen Satzgefüge oder als klarer Fachterminus formuliert werden.
2. **Absolutes Fragezeichen-Verbot (`?`):**
   - Eine `H1` darf niemals als Frage formuliert sein (keine rhetorischen Fragen). Eine `H1` benennt Fakten und Gegenstand klar und sachlich.
3. **Einzelsatz-Gebot (Single Statement Principle) & Schlusspunkt-Verbot (`.`):**
   - Eine `H1` darf niemals aus zwei getrennten Sätzen bestehen und trägt keinen Schlusspunkt (`.`).
   - Über `--measure-h1: 32ch` wird sichergestellt, dass auch längere deutsche Komposita in 1 bis 2 Zeilen harmonisch umbrechen.
4. **Verbot von Jahreszahl-Klammern (`[2026]`):**
   - Eckige Klammern mit Jahreszahlen am Ende von Überschriften oder Seitentiteln sind verboten. Aktualität zeigt sich durch den `last_verified_at`-Zeitstempel und strukturierte Metadaten.
5. **Erklärende Hero-Subheadline (`h1 + h2`) vs. Sektions-Überschrift (`h2`):**
   - Eine unmittelbar auf `<h1>` folgende `<h2>` (`h1 + h2`) bleibt für Suchmaschinen semantisch ein `<h2>`, wird über das zentrale Design-System (`global.css`) jedoch automatisch in ruhiger Lead-Typografie (`font-weight: 400`, `max-width: 65ch`) dargestellt, damit sie optisch nicht mit der `700`-Bold-`H1` konkurriert. Eigenständige Sektions-`<h2>`-Überschriften stehen in `700` Bold (`max-width: 48ch`).

---

## 2. Absolutes Geviertstrich-Verbot (Em-Dash `U+2014` & `--`)

- Die Verwendung des langen englischen Geviertstrichs (Em-Dash, `U+2014`) sowie doppelter Bindestriche (`--`) ist im gesamten Textkorpus **ausnahmslos verboten (0 Treffer)**.
- Sätze werden sauber durch Kommas, Punkte, Semikolons oder bei Einschüben durch den regulären deutschen Gedankenstrich (Halbgeviertstrich `–`, `U+2013`, mit Leerzeichen davor und danach) gegliedert.

---

## 3. Fettungsverbot im Fließtext (Anti-Bolding-Inflation)

- Innerhalb regulärer Fließtext-Absätze (`<p>`) ist das künstliche, inflationäre Fetten einzelner Wörter oder Satzteile (`**...**`, `<b>`, `<strong>`) zur vermeintlichen Lesesteuerung **strikt verboten**.
- Fließtext bleibt ruhig, sachlich und typografisch sauber.
- Hervorhebungen gehören ausschließlich in strukturierte Tabellenköpfe (`<th>`), Definitionslisten, Voranstellungen in Aufzählungspunkten (`<li><strong>Begriff:</strong> Erklärung</li>`) oder dedizierte Kennzahlen-Badges.

---

## 4. Anti-Floskel-Blacklist, Tabu-Wörter & Anti-Clickbait

1. **Verbot typischer KI-Einleitungs- und Schlussfloskeln:**
   - Ausdrücke wie *„In der heutigen schnelllebigen/digitalen Welt“*, *„Tauchen wir ein“*, *„Zusammenfassend lässt sich sagen“*, *„Ein facettenreicher Bereich“*, *„Willkommen bei / in“*, *„Es ist wichtig zu beachten“* oder *„Nicht zuletzt“* sind ausnahmslos verboten.
2. **Verbot von Agentur-Hype, Marketing-Buzzwords & unnötigem US-Fachjargon:**
   - Wörter wie *„Gamechanger“*, *„Quantensprung“*, *„Hack / Lifehack“*, *„Revolution / revolutionär“*, *„Geheimnis / Secret“*, *„Guru“*, *„Next Level“*, *„orchestrieren“*, *„State-of-the-Art“* oder *„ganzheitliches Ökosystem“* sind auf der gesamten Website verboten.
   - Ebenso wird unnötiger US-Agenturjargon wie *„C-Level“*, *„Cutover“*, *„Zero-Downtime“*, *„Quick-Wins“*, *„Content Pruning“*, *„Staging“*, *„One-Pager“* oder *„Pagebuilder“* im sichtbaren Kundentext durch präzise deutsche Fachbegriffe (*„Geschäftsführung & Inhaber“*, *„unterbrechungsfreie Live-Schaltung“*, *„Sofort-Maßnahmen“*, *„geschützte Vorschau-Umgebung“*, *„Seitenbaukasten“*) ersetzt.
3. **Sprachliche Aktions-Kohäsion (CTA-Button $\rightarrow$ Bestätigungsmeldung):**
   - Der exakte Wortlaut eines primären Handlungsbuttons (z. B. *„Kostenlose URL- & 301-Risiko-Kurzanalyse anfordern“*) muss in der darauffolgenden Formular-Bestätigungsmeldung wortgleich wieder aufgegriffen werden (*„Ihre Anfrage zur kostenlosen URL- & 301-Risiko-Kurzanalyse ist eingegangen...“*).
4. **Verbot martialischer Rhetorik, Panikmache & Schmähkritik:**
   - Begriffe wie *„vernichten“*, *„tödlich“*, *„Todesurteil“*, *„zerstören“*, *„Auslöschung“*, *„Gift“*, *„Betrug“*, *„Abzocke“* oder *„Schwindel“* sind sowohl stilistisch als auch äußerungsrechtlich strengstens untersagt.
5. **Strikte Anti-Clickbait-Vorgabe:**
   - Keine reißerischen Schlagzeilen und keine Vorenthaltung relevanter Fakten im Titel (*„Das passierte dann...“* ist verboten). Fakten werden nach dem Prinzip der umgekehrten Pyramide sofort im Titel und ersten Satz benannt.

---

## 5. DIN 5008 Typografie, Sie-Form, Parenthesen-Formel & Markenname

1. **DIN 5008 Leerzeichen-Pflicht (Zahlen, Prozentwerte & Einheiten):**
   - Vor dem Prozentzeichen (`%`) sowie vor physikalischen und rechtlichen Maßeinheiten (`g`, `mg`, `kg`, `ml`, `l`, `km`, `EUR`, `€`) und Paragraphen-/Artikelzeichen (`§`, `Art.`) steht zwingend ein (vorzugsweise geschütztes) Leerzeichen:
   - **Richtig:** `100 %`, `12,4 g`, `250 EUR`, `Art. 5 GG`, `§ 8c UWG`.
   - **Falsch (Verboten):** `100%`, `12,4g`, `250EUR`.
2. **Höfliche „Sie“-Form (sofern nicht anders spezifiziert):**
   - Im deutschsprachigen Auftritt gilt standardmäßig die respektvolle, sachliche **„Sie“-Form** (Ausnahme nur, wenn das Projektkonzept explizit eine Vereins- oder Gaming-„Du“-Kultur festlegt).
3. **Die Parenthesen-Formel (Alltagssprache + Fachbegriffe in Klammern):**
   - Komplexe juristische, technische oder wissenschaftliche Sachverhalte werden im Hauptsatz zunächst in klarer, sofort verständlicher Alltagssprache erklärt; der präzise Fachterminus folgt in Klammern dahinter.
4. **Markenname vs. Domain im Fließtext (sowie Schweizer Standard bei `.ch`):**
   - Im redaktionellen Fließtext, in Überschriften, FAQs, Badges und Buttons wird der saubere Markenname (ohne `.de` / `.ch` / `.com`) verwendet; die Domain-Schreibweise bleibt technischen URLs, Canonicals, SERP-Title-Suffixen und dem Impressum/Datenschutz vorbehalten.
   - Bei Schweizer Projekten (`de-CH`) gilt zusätzlich strikte `ss`-Schreibung statt `ß` (0 Treffer für `ß`) sowie die Nutzung von Guillemets (`«...»`).
