# ki-lernjournal

**Öffentliches Lernjournal auf dem Weg zur KI-Expertise — dokumentiert seit 11.05.2026.**

> **Aktueller Stand (19.11.2026, Lerntag 80):** Das Fundament steht (Python, lineare Algebra, Andrew Ng Course 1). Zurzeit arbeite ich an neuronalen Netzen (Andrew Ng Course 2) und habe mein erstes durchgängiges Projekt abgeschlossen: ein Credit-Scoring-Modell von den Rohdaten bis zur Bewertung in Euro. Als Nächstes folgt ein RAG-Prototyp. Details weiter unten.

## Wer schreibt das hier

Ich bin Alp Dalkilic, Jahrgang 1971, Ex-Vorstand (CFO,CDO,Dep.CEO) im Banking. Mein Hauptprojekt ist die Beratung kleiner und mittelgroßer Unternehmen auf der Grundlage fundierter Expertise zu KI-Systemen, primär im Financial-Services-Sektor, aber auch industrieübergreifend. Dafür baue ich seit Mai 2026 substanzielles KI-Handwerk auf — nicht als Marketing-Label, sondern als belastbare Grundlage.

## Warum öffentlich

Öffentlich zu lernen ist die härteste Form von Commitment.

Das Repo ist außerdem ein Angebot: Wer ähnliche Wege geht, findet hier Notebooks, Notizen, Fehler und Kurs-Korrekturen. Wer konkrete Kooperationen sucht (Banking × KI), findet Kontakt.

## Projekt: Credit-Scoring (Oktober–November 2026)

Mein erstes Projekt vom Rohdatensatz bis zur Bewertung. Es ist ein **Lernprojekt** auf einem öffentlichen Übungsdatensatz und nicht für echte Kreditentscheidungen bestimmt.

**Worum es geht:** Ein Modell schätzt für einen Kreditantrag die Ausfallwahrscheinlichkeit. Ich habe es zweimal gebaut, einmal mit einer selbst geschriebenen logistischen Regression und einmal mit scikit-learn, und danach mit einem kleinen neuronalen Netz verglichen.

**Daten:** German Credit (OpenML „credit-g"): 1.000 vergebene Konsumentenkredite, 20 Merkmale, 30 % Ausfälle. 700 Kredite zum Lernen, 300 zum Testen.

**Ergebnis im Testteil (300 Kredite, davon 90 Ausfälle):**

| Modell | Richtig auf Lerndaten | Richtig auf Testdaten |
|---|---|---|
| „Alle genehmigen" (kein Modell) | — | 70 % |
| Logistische Regression (scikit-learn) | 79 % | 78 % |
| Neuronales Netz 61 → 4 → 1 (TensorFlow) | 88 % | 71 % |

- Die logistische Regression erkennt 48 der 90 Ausfälle und lehnt 23 von 210 guten Kunden zu Unrecht ab.
- Das neuronale Netz hat die Lerndaten weitgehend auswendig gelernt (Overfitting) und ist auf neuen Daten kaum besser als gar kein Modell. Die logistische Regression bleibt das Modell der Wahl, auch weil sich ihre Gewichte je Merkmal nachvollziehen lassen.

**Was ich dabei gelernt habe:**

- Die Reihenfolge ist zwingend: erst in Lern- und Testteil aufteilen, dann alles Weitere nur aus dem Lernteil ableiten. Sonst sieht das Modell die Testdaten.
- Der Datensatz enthält nur vergebene Kredite. Merkmale wie „kein Girokonto" wirken deshalb sicher, weil solche Kunden damals streng geprüft wurden. Das Modell beschreibt die alte Kreditpolitik, nicht das Risiko des Merkmals.
- Eine Trefferquote sagt wenig, solange man sie nicht in Euro übersetzt und gegen „alle genehmigen" stellt.

**Grenzen:** Der Datensatz ist nicht repräsentativ (30 % Ausfälle), die Wahrscheinlichkeiten sind nicht kalibriert, der Testteil ist klein, und eine Prüfung auf Benachteiligung einzelner Gruppen hat nicht stattgefunden.

**Regulatorische Einordnung:** Bei einem Einsatz in der Kreditvergabe an Privatkunden wäre ein solches Modell ein Hochrisiko-KI-System nach der KI-Verordnung der EU (Anhang III Nummer 5 Buchstabe b). Für ein Lernprojekt gelten diese Pflichten nicht; die Lücken zu den dort verlangten Anforderungen dokumentiere ich in einer Model Card, die hier ergänzt wird.

**Dateien:** [`notebooks/credid_scoring_v1.ipynb`](./notebooks/credid_scoring_v1.ipynb) (Daten, Vorverarbeitung, beide Regressionen, Bewertung) · [`notebooks/NN_exercise.ipynb`](./notebooks/NN_exercise.ipynb) (neuronales Netz) · [`requirements.txt`](./requirements.txt). Die Aufteilung nutzt `random_state=42`, das Netz den Seed 42.

## Was hier liegt

- `notebooks/` — Jupyter-Notebooks aus Übungen, Kursen und Projekten: Python-Grundlagen, NumPy, lineare Algebra bis zur PCA von Hand, Pandas, eigene Klassen, logistische Regression, scikit-learn, TensorFlow.
- `Pythons/` — Python-Skripte aus der Anfangsphase (*Automate the Boring Stuff*).
- `data/` — kleine Beispiel-Datensätze für Übungen (große Dateien via `.gitignore` ausgeschlossen).
- `requirements.txt` — die verwendeten Pakete.

## Der Weg bisher

- **Mai–Oktober 2026: Fundament.** Python (*Automate the Boring Stuff*, Kaggle Learn), lineare Algebra mit einer PCA, die ich Schritt für Schritt selbst programmiert habe, danach Andrew Ng Machine Learning Specialization, Course 1 (Supervised ML), abgeschlossen am 08.10.2026.
- **Oktober 2026: Werkzeuge und erstes Projekt.** Pandas, eigene Klassen nach dem Muster von scikit-learn (`fit`, `transform`, `predict`), dann das Credit-Scoring-Projekt.
- **November 2026: Neuronale Netze.** Andrew Ng Course 2, Wochen 1 und 2 abgeschlossen; das eigene Netz in NumPy und TensorFlow nachgebaut. Dazu der Einstieg in Sprachmodelle: wie ein LLM funktioniert.

## Wie es weitergeht

Den ursprünglichen 18-Monats-Plan habe ich nach der Fundament-Phase ersetzt. Ich plane jetzt in Abschnitten von drei Monaten und richte den nächsten Abschnitt an dem aus, was im vorigen wirklich getragen hat. Im laufenden Abschnitt (bis Mitte Januar 2027) stehen an:

- Andrew Ng Course 2 abschließen (Modellbewertung, Regularisierung, Entscheidungsbäume).
- Ein RAG-Prototyp: ein Sprachmodell beantwortet Fragen zu einem Gesetzestext mit Quellenangabe.
- Was zwischen Prototyp und Betrieb liegt: Monitoring, Tests, Sicherheit, Kosten.

## Mein Lernsystem

Aus dem Lernen ist über die Monate ein eigenes System geworden: geplant, gemessen und jede Woche nachgeschärft. Ich habe es zusammen mit meinem KI-Assistenten (Claude) entwickelt. Wer aus der Banksteuerung kommt, erkennt das Muster: Planung, Messung, Abweichungsanalyse, Maßnahme.

**1 · Planung in vier Ebenen**

Richtung (was ich am Ende können will) → Abschnitt von drei Monaten → Wochenskizze → Tagesplan. Geplant wird in Dauern statt Uhrzeiten und nach gemessener Geschwindigkeit, nicht nach Stoffumfang. An jeder Abschnittsgrenze sortiere ich neu, und einmal im Quartal prüfe ich, ob die Inhalte noch dem Stand der Technik entsprechen.

**2 · Feste Lernmethoden**

| Methode | Was ich tue |
|---|---|
| Denkmodell vor Werkzeug | Bevor ich eine Bibliothek oder ein Verfahren benutze, arbeite ich eine kurze Unterlage durch, die die Logik an einem Mini-Beispiel Schritt für Schritt vorrechnet. |
| Zerlegung vor dem Bau | Bevor ich Code schreibe, zerlege ich die Aufgabe auf Deutsch in Schritte. Erst dann lasse ich mir den passenden Befehl zeigen und prüfe, was er mit meinen Daten macht. Die Zerlegungen stehen als Textzellen in den Notebooks. |
| Abruf ohne Vorlage | Regelmäßig und am Ende jedes Kurses schreibe ich aus dem Kopf auf, was sitzt. Was fehlt, wird gezielt nachgearbeitet. |
| Erklären ohne Fachwörter | Am Ende eines Themas erkläre ich es schriftlich einem gedachten Kollegen ohne Vorkenntnisse. |
| Karteikarten | Eine kleine Portion je Lerntag. |

**3 · Tages- und Wochenrhythmus**

Ich arbeite in einem festen Rhythmus: Montag bis Donnerstag sind Stoff- und Projekttage, der Freitag ist Puffer- und Meta-Tag. Jeder Lerntag beginnt mit einem Plan mit Pausen und endet mit einem kurzen Rückblick: erster Eindruck, Selbsteinschätzung von 1 bis 10 und die gemessene Netto-Stoffzeit. Gesteuert wird nach dieser Netto-Zeit und nach dem, was im Abruf ohne Vorlage tatsächlich sitzt, nicht nach abgesessenen Stunden.

**4 · Regeln für die Zusammenarbeit mit der KI und ein Fehlerprotokoll**

Für den Assistenten gelten vier Grundregeln: nichts annehmen, was sich prüfen oder fragen lässt · jede Nachricht ist ohne Vorgeschichte verständlich · vollständig liefern · erst die Kernaussage, dann am eigenen Beispiel vorführen. Jede Antwort, die ich beanstanden muss, wird am Tagesende notiert und einer Fehlerart zugeordnet. Damit liegen am Ende der Woche Daten vor und keine Eindrücke.

**5 · Der Meta-Tag: So lernt das System**

Jeden Freitag steht das System selbst auf dem Prüfstand, höchstens zwei Stunden lang:

- **Auswerten:** Ein Wochenrückblick liegt vorbereitet vor. Die Beanstandungen der Woche werden je Fehlerart gezählt, die Stoffzeit mit dem Plan verglichen.
- **Entscheiden:** Was wirkt nicht und fällt weg, was fehlt und kommt dazu? Höchstens eine Regel pro Woche wird geändert, und jede Änderung bekommt einen Prüftermin, an dem ihre Wirkung an Zahlen gemessen wird.
- **Nachziehen:** Die Entscheidung wandert in die Arbeitsregeln und in die Skizze der nächsten Woche.

So wird das System mit jeder Woche besser, ohne zu wuchern: Regeln, die ihre Wirkung nicht belegen, werden wieder gestrichen. Dieselbe Schleife aus Messen, Entscheiden und Nachprüfen braucht jede Organisation, die KI einsetzt, nur in größerem Maßstab.

**Wo was liegt:** Notion ist die Steuerzentrale: das Lernjournal mit einer Zeile je Lerntag, die Wochenskizzen, eine einzige Aufgabenliste und die Arbeitsregeln. Unterlagen und Referenzen liegen in einem privaten Arbeitsordner mit täglicher Sicherung. Hier im Repo liegt der ausführbare Teil.

## Kadenz & Transparenz

Der Fokus liegt auf Substanz statt Sichtbarkeit: Die LinkedIn-Lernlog-Reihe pausiert, neue Commits erscheinen laufend hier.

## Kontakt

- LinkedIn: to come
- Website: to come
- E-Mail: to come

## Lizenz

[MIT License](./LICENSE). Notebooks, Notizen und Code sind frei verwendbar; PDFs von Dritten sind nicht im Repo.
