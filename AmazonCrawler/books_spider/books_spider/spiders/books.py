import scrapy
from urllib.parse import urlencode
from ..items import BooksSpiderItem

# hier kann man die Suchbegriffe eingeben (Zeile 16-19), oder man kann Links hereinkopieren (Zeile 23-26):

queries = ['Anzug', 'Armbanduhr']


class BooksCrawler(scrapy.Spider):

    name = 'products'

# für die Suche über, indem man Suchbegriffe in 'queries' eintippt (Zeile 7):

    def start_requests(self):
        for query in queries:
            url = 'https://www.amazon.de/s?' + urlencode({'k': query})
            yield scrapy.Request(url= url, callback=self.parse, cb_kwargs=dict(url=url))

# für die Suche, indem man einen oder mehrere Links in 'queries' hereinkopiert (siehe Zeile 7):

    #def start_requests(self):
     #   for query in queries:
      #      url = query
       #     yield scrapy.Request(url=url, callback=self.parse, cb_kwargs=dict(url=url))


    def parse(self, response, url):

        items = BooksSpiderItem()  # Instanz der Klasse BooksItem erstellt
        all_items = response.css('.s-result-item')  # .s-result-item

        for item in all_items:

            product_name = item.css('h2 span ::text').extract()
            picture_link = item.css('img.s-image::attr(src)').extract()
            product_price = item.css('.a-price-whole').css('::text').extract_first()
            rating = item.css('.a-icon-alt::text').extract()
            rating_count = item.css('.a-size-small .a-size-base').css('::text').extract()


            if product_price is not None:
                if picture_link:
                    items['product_name'] = product_name  # ein Feld der Instanz items mit allen Klassenvariablen erstellen
                    items['picture_link'] = picture_link
                    items['page_link'] = url
                    if product_price:
                        items['product_price'] = float(product_price.replace('.','').replace(',', '.'))
                    else:
                        items['product_price'] = -1
                    if rating and rating_count:
                        items['rating'] = float(rating[0].split(' ')[0].replace(',', '.'))
                        items['rating_count'] = float(rating_count[0].replace('.',''))
                    else:
                        items['rating'] = -1
                        items['rating_count'] = -1


                    yield items

        # um alle erschienenen Produktseiten zu crawlen, einfach Folgendes entkommentieren:

        #next_page = response.xpath('//li[@class="a-last"]/a/@href').extract_first()

        #if next_page:
         #   url = "https://www.amazon.de" + str(next_page)
          #  yield scrapy.Request(url=url, callback=self.parse, cb_kwargs=dict(url=url))

