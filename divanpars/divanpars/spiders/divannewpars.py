import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://divan.ru/category/divany-i-kresla"]

    def parse(self, response):

