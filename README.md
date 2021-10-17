# amazon-web-crawler
WebCrawler to scrape product data off of Amazon.

Dieser Crawler läuft über Amazon-Produktseiten und extrahiert 6 Attribute pro Produkt:

Name
Preis
Sternebewertung
Anzahl der Sternebewertungen
Bild des Produktes
Link zur Produktseite

Darüber hinaus wird das aktuelle Datum des Crawl-Prozesses gespeichert, um Preis Monitoring zu ermöglichen.
Nach Produkten suchen kann man über die Datei 'books.py'.
Dort findet man in Zeile 7 das Feld 'queries'.
Es gibt zwei Wege nach Produkten zu suchen:
1. Suchbegriff/e eingeben --> queries = ['Amazon Link einfügen'], Zeile 23-26 entkommentieren und 16-19 kommentieren
2. Link/s eingeben --> queries = ['Suchbegriff'], Zeile 16-19 entkommentieren, Zeile 23-26 kommentieren

Um alle Seiten crawlen zu lassen und nicht nur die Erste, müssen Zeile 64 bis 67 entkommentiert werden.
Wenn man nur etwas testen möchte, ist es natürlich effizienter nur die erste Seite zu crawlen ;)
Um den Crawler zu starten öffnet man in der Pycharm IDE ein Terminal (unten Links auf dem Bildschirm zu finden).
Zuerst navigiert man mit dem Befehl: cd products_spider in den richtigen Ordner.
Danach kann der Crawling Prozess mithilfe des Befehls: scrapy crawl products gestartet werden.
Nachdem die Produkte gecrawled wurden, wird automatisch eine sqlite Datenbank namens 'items.db' erstellt.
Diese kann man beispielsweise über https://sqliteonline.com/ aufrufen.
Nachdem man Daten gecrawled hat und die SQL-Datenbank erstellt wurde, ist es essentiell im File 'pipelines.py' Zeile
10 zu kommentieren, da sonst durch einen neuen Crawl-Prozess die alte Tabelle mit den neuen Daten überschrieben wird
und die alten Werte nicht mehr zu finden sind.
Sollten die alten Werte nicht mehr gebraucht werden, kann man Zeile 10 entkommentieren und dadurch eine neue Tabelle
anlegen.
Generell lässt sich der ganze SQL-Teil über das File 'pipelines.py' steuern und dementsprechend ist es von Vorteil,
etwas SQl-Knowledge mitzubringen.
Jetzt wünsche ich euch viel Erfolg mit dem Crawler. Falls bestimmte Funktionen verbuggt erscheinen sollten,
Schwierigkeiten auftreten oder Modifikationen gewünscht sind könnt ihr mich gerne kontaktieren.
Außerdem freue ich mich auf euer Feedback, um den Crawler in Zukunft zu verbessern.
