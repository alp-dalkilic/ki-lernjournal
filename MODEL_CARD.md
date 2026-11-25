# Model Card — Credit-Scoring (German Credit)

Stand: 25.11.2026 · Lernprojekt von Alp Dalkilic · Notebooks: [`notebooks/credid_scoring_v1.ipynb`](./notebooks/credid_scoring_v1.ipynb), [`notebooks/NN_exercise.ipynb`](./notebooks/NN_exercise.ipynb)

Eine Model Card ist der Beipackzettel eines Modells: wofür es gebaut wurde, womit es gelernt hat, wie gut es ist und wofür man es nicht verwenden darf.

## 1 · Modell

Logistische Regression (scikit-learn, `LogisticRegression(max_iter=1000)`), 62 Parameter. Sie schätzt für einen Kreditantrag die Ausfallwahrscheinlichkeit. Ob daraus eine Ablehnung wird, entscheidet eine Schwelle, die nicht Teil des Modells ist.

## 2 · Zweck und Nicht-Zweck

**Zweck:** zeigen, wie ein Antragsscoring von den Rohdaten bis zur Bewertung in Euro aufgebaut wird.

**Nicht-Zweck:** nicht für echte Kreditentscheidungen; nicht für andere Länder, Zeiträume oder Produkte als im Datensatz; keine Wirtschaftlichkeitsrechnung für ein Portfolio.

## 3 · Daten

German Credit (OpenML „credit-g", Version 1): 1 000 **vergebene** Konsumentenkredite, Deutschland, 1990er, 20 Merkmale, 30 % Ausfälle. 700 Kredite zum Lernen, 300 zum Testen, gleiche Ausfallquote in beiden Teilen (stratifizierte Aufteilung). Abgelehnte Anträge und das Einkommen fehlen im Datensatz.

## 4 · Vorverarbeitung (gehört zum Modell)

Kategorien werden in Null-Eins-Spalten umgewandelt (aus 20 Merkmalen werden 61 Spalten); die 7 Zahlenspalten werden standardisiert, und zwar nur mit Mittelwert und Streuung aus dem Lernteil. Ohne dieselbe Spaltenreihenfolge und dieselbe Standardisierung läuft das Modell fehlerfrei und liefert Unsinn.

## 5 · Ergebnis im Testteil (300 Kredite, 90 Ausfälle, Schwelle 0,5)

| Kennzahl | Wert | Lesart |
| --- | --- | --- |
| Richtig eingestuft (Accuracy) | 235 von 300 = 78 % | ohne Modell („alle genehmigen"): 70 % |
| Erkannte Ausfälle (Recall) | 48 von 90 = 53 % | 42 Ausfälle werden übersehen |
| Treffer unter den Markierten (Precision) | 48 von 71 = 68 % | zwei von drei Warnungen stimmen |
| Zu Unrecht abgelehnte gute Kunden | 23 von 210 | kosten entgangenen Ertrag |
| Vermiedener Verlust | 203 221 von 342 124 EUR = 59 % weniger | gegenüber „alle genehmigen" |
| Brier score | 0,157 | ohne Modell (immer 30 % vorhersagen): 0,21 |

Annahme hinter den Euro-Werten: Verlust je Ausfall = 85 % des Kreditbetrags (Recovery 15 %), Ausfall am ersten Tag, keine Tilgung.

**Kalibrierung im Testteil** (300 Kredite nach vorhergesagter Wahrscheinlichkeit sortiert, 5 Gruppen zu je 60):

| Gruppe | Mittlere Vorhersage | Tatsächliche Ausfallquote | Abweichung |
| --- | --- | --- | --- |
| 1 | 4,0 % | 8,3 % | −4,4 Punkte |
| 2 | 11,8 % | 10,0 % | +1,8 Punkte |
| 3 | 23,4 % | 23,3 % | +0,1 Punkte |
| 4 | 42,9 % | 38,3 % | +4,6 Punkte |
| 5 | 69,2 % | 70,0 % | −0,8 Punkte |

In einer Gruppe von 60 macht ein einzelner Kredit 1,7 Prozentpunkte aus. Die Tabelle zeigt keine grobe Fehlkalibrierung, erlaubt aber keine feinere Aussage.

## 6 · Modellwahl

| Modell | Parameter | Lerndaten | Testdaten |
| --- | --- | --- | --- |
| „Alle genehmigen" (kein Modell) | 0 | — | 70 % |
| Logistische Regression | 62 | 79 % | 78 % |
| Neuronales Netz 61 → 4 → 1 | 253 | 88 % | 71 % |

Das neuronale Netz hat die Lerndaten im Wesentlichen auswendig gelernt (Overfitting). Die logistische Regression verliert von Lern- zu Testdaten nur rund einen Punkt, ist auf neuen Daten genauer, und ihre Gewichte lassen sich je Merkmal nachvollziehen.

## 7 · Grenzen

1. **Nicht repräsentativ:** 30 % Ausfälle statt eines niedrigen einstelligen Werts in echten Portfolios.
2. **Wahrscheinlichkeiten nur innerhalb des Datensatzes kalibriert:** Auf dem Testteil weichen Vorhersage und tatsächliche Ausfallquote höchstens 4,6 Prozentpunkte ab (Abschnitt 5). Die Werte sind aber auf eine Ausfallquote von 30 % geeicht. In einem Portfolio mit niedrigerer Ausfallquote überschätzen sie das Risiko systematisch (Beispiel 3 %: aus 40 % werden rund 5 %) und müssen vor jeder Verwendung umgerechnet oder an echten Daten neu kalibriert werden.
3. **Selektionseffekt:** Der Datensatz enthält nur vergebene Kredite. „Kein Girokonto" und „kritische Kredithistorie" erscheinen als sicher, weil solche Kunden streng geprüft wurden. Das Modell beschreibt die alte Kreditpolitik, nicht das Risiko des Merkmals.
4. **Kleiner Testteil:** Bei 90 Ausfällen verschiebt ein einzelner Fall die Erkennungsquote um gut einen Prozentpunkt.
5. **Wirtschaftlichkeit:** Bei 5 % Marge und 85 % Verlust im Ausfall trägt sich ein Kredit nur bis etwa 11 % Ausfallwahrscheinlichkeit. Bei 30 % ist jedes Portfolio negativ; die Euro-Rechnung zeigt die Mechanik, keine Wirtschaftlichkeit.
6. **Persönliche Merkmale:** siehe Abschnitt 8.

## 8 · Regulatorische Einordnung nach der KI-Verordnung der EU (EU AI Act)

| Punkt | Eintrag |
| --- | --- |
| Geltung heute | Lernprojekt auf einem öffentlichen Übungsdatensatz. Nicht in Verkehr gebracht, nicht in Betrieb genommen. Forschung, Tests und Entwicklung vor dem Einsatz sind von der Verordnung ausgenommen (Artikel 2 Absatz 8). |
| Zweckbestimmung | Veranschaulichung eines Vorgehens. Ausdrücklich nicht für echte Kreditentscheidungen bestimmt. |
| Risikostufe bei echtem Einsatz | Hochrisiko-System, weil die Kreditwürdigkeitsprüfung natürlicher Personen ausdrücklich in Anhang III genannt ist (Nummer 5 Buchstabe b, über Artikel 6 Absatz 2). Die Ausnahme nach Artikel 6 Absatz 3 greift nicht, weil das Modell ein Profiling vornimmt. |
| Rollen bei echtem Einsatz | Anbieter: wer das Modell unter eigenem Namen in Betrieb nimmt, bei Eigenentwicklung die Bank. Betreiber: die einsetzende Bank. |
| Lücken zu den Anbieterpflichten | Alter Datensatz, heute nicht mehr repräsentativ · keine Prüfung auf Benachteiligung · keine Protokollierung · menschliche Aufsicht nicht gestaltet · kein Risikomanagement- und Qualitätsprozess · keine Konformitätsbewertung. Vorhanden: Zweck und Grenzen beschrieben, Genauigkeit gemessen, Ergebnisse reproduzierbar. |
| Pflichten des Betreibers | Nutzung nach Anleitung, geschulte Aufsicht mit Befugnis zum Übersteuern, Information der Antragsteller, Folgenabschätzung für Grundrechte vor dem ersten Einsatz, Erläuterung auf Verlangen. |
| Persönliche Merkmale | Das Modell verwendet persönliche Merkmale aus dem Datensatz: Alter, Geschlecht und Familienstand (eine kombinierte Spalte), Zahl der Unterhaltsberechtigten und die Angabe „ausländischer Arbeitnehmer". Alle gehen in die Ausfallwahrscheinlichkeit ein. Am stärksten wirkt „ausländischer Arbeitnehmer" (Gewicht +0,65, eines der größeren im Modell, gestützt auf nur 37 Vergleichsfälle); Geschlecht und Familienstand verschieben den Score um bis zu 0,7 zwischen zwei Gruppen. Vor einem echten Einsatz wäre rechtlich zu prüfen, ob diese Merkmale verwendet werden dürfen. Ob das Modell Gruppen im Ergebnis unterschiedlich behandelt, ist nicht untersucht; dafür fehlt der Vergleich von Ablehnungs- und Fehlerquoten je Gruppe. |
| Frist | Pflichten für Hochrisiko-Systeme nach Anhang III ab 02.12.2027 (nach dem Digital Omnibus). |
| Stand der Einordnung | 25.11.2026. Fachliche Einordnung, keine Rechtsberatung. |

**Vor einem echten Einsatz außerdem:** eigene, aktuelle Portfoliodaten einschließlich abgelehnter Anträge · unabhängige Validierung · Überwachung im Betrieb · menschliche Letztentscheidung mit begründbarer Ablehnung.

## 9 · Nachvollziehen

[`requirements.txt`](./requirements.txt) · Aufteilung mit `random_state=42` · Netz mit `tf.keras.utils.set_random_seed(42)` · Notebooks `credid_scoring_v1.ipynb` und `NN_exercise.ipynb`.
