
import scrapy


class BooksSpiderItem(scrapy.Item):
    product_name = scrapy.Field()
    product_price = scrapy.Field()
    rating = scrapy.Field()
    rating_count = scrapy.Field()
    picture_link = scrapy.Field()
    page_link = scrapy.Field()

