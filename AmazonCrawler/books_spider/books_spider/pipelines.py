import sqlite3
from datetime import datetime

date = datetime.now().date() 

class BooksSpiderPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("items.db" )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS Produkte""")
        self.curr.execute("""create table Produkte(
                          Datum date,
                          Produktname text,
                          Preis float,
                          Sternebewertung float,
                          Anzahl Bewertungen float,
                          Link zur Produktseite text,
                          Bild text
                          )""")


    def process_item(self, item, spider):
        self.store_db(item)

        return item

    def store_db(self, item):
        self.curr.execute("""insert into Produkte values (?,?,?,?,?,?,?)""", (
                            date,
                            item['product_name'][0],
                            item['product_price'],
                            item['rating'],
                            item['rating_count'],
                            item['page_link'],
                            item['picture_link'][0],
                          ))
        self.conn.commit()