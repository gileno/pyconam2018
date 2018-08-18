import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class VivarealSpider(CrawlSpider):
    
    name = 'vivareal_crawl'
    start_urls = ['https://www.vivareal.com.br/venda/pernambuco/recife/bairros/boa-viagem/apartamento_residencial/']
    rules = (
        Rule(
            LinkExtractor(allow='/venda/pernambuco/recife/bairros/boa-viagem/apartamento_residencial/')
        ),
        Rule(
            LinkExtractor(
                allow='/imovel/',
            ), callback='parse_imovel'
        )
    )

    def parse_imovel(self, response):
        yield {
            'title': response.xpath("//title/text()").extract_first()
        }

# yield {
#             'title': response.xpath("//title/text()").extract_first(),
#             'price': response.xpath("//*[contains(@class, 'js-detail-sale-price')]/text()").extract_first(),
#             'area': response.xpath("//*[contains(@class, 'js-detail-area-value')]/text()").extract_first(),
#             'latitude': response.xpath("//meta[contains(@property, 'place:location:latitude')]/@content").extract_first(),
#             'longitude': response.xpath("//meta[contains(@property, 'place:location:longitude')]/@content").extract_first(),
#         }