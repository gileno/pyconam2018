import scrapy
import re


class DolarSpider(scrapy.Spider):

    name = 'dolar_hoje'
    start_urls = ['https://www.melhorcambio.com/dolar-hoje']
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/5'
    }

    def parse(self, response):
        html = response.text
        preco = re.findall(
            r'<input type="hidden" value="(.*)" id="taxa-comercial">', html
        )[0]
        self.log(preco)
