import scrapy
import re


class DolarSpider(scrapy.Spider):

    name = 'dolar_hoje'
    start_urls = ['https://www.melhorcambio.com/dolar-hoje']

    def parse(self, response):
        preco = response.xpath('//input[@id="taxa-comercial"]/@value')
        self.log(preco.extract_first())
        preco = response.css('#taxa-comercial')[0]
        self.log(preco.attrib['value'])
