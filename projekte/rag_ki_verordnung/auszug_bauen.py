"""Schneidet ausgewaehlte Artikel der KI-Verordnung (EU) 2024/1689 aus der
EUR-Lex-HTML-Seite und schreibt sie als reine Textdatei.

Aufbau der Ausgabe:
    Artikel 26 | Pflichten der Betreiber von Hochrisiko-KI-Systemen
    (1) Wortlaut des ersten Absatzes ...
    (2) Wortlaut des zweiten Absatzes ...
    <Leerzeile>
Jeder Absatz steht in genau einer Zeile. Buchstaben-Aufzaehlungen a), b) ...
bleiben Teil ihres Absatzes.

Aufruf (im Ordner projekte/rag_ki_verordnung):
    python3 auszug_bauen.py
"""
import re
from pathlib import Path
from bs4 import BeautifulSoup

ARTIKEL = [5, 6, 9, 14, 26, 50]
ORDNER = Path(__file__).parent / "data"
QUELLE = sorted(ORDNER.glob("*.html"))[0]
ZIEL = ORDNER / "ki_verordnung_auszug_2024.txt"


def sauber(text):
    """Zeilenumbrueche und Mehrfach-Leerzeichen zu einem Leerzeichen."""
    return re.sub(r"\s+", " ", text.replace("\xa0", " ")).strip()


soup = BeautifulSoup(QUELLE.read_text(encoding="utf-8"), "html.parser")
zeilen = []
for nr in ARTIKEL:
    art = soup.find("div", id=f"art_{nr}")
    titel = sauber(art.find("p", class_="oj-sti-art").get_text(" "))
    zeilen.append(f"Artikel {nr} | {titel}")
    absaetze = art.find_all("div", id=re.compile(rf"^{nr:03d}\.\d{{3}}$"))
    for absatz in absaetze:
        zeilen.append(sauber(absatz.get_text(" ")))
    zeilen.append("")

ZIEL.write_text("\n".join(zeilen), encoding="utf-8")
print("Quelle:", QUELLE.name)
print("Ziel:  ", ZIEL.name)
