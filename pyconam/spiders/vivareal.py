import scrapy

class VivaRealSpider(scrapy.Spider):

    name = 'vivareal'
    start_urls = ['https://www.vivareal.com.br/venda/pernambuco/recife/bairros/boa-viagem/apartamento_residencial/']

    def parse(self, response):
        for item in response.xpath("//div[contains(@class, 'results-list')]/div"):
            href = item.xpath(".//h2/a/@href").extract_first()
            yield scrapy.Request(
                f'https://www.vivareal.com.br{href}', self.parse_detail
            )
    def parse_detail(self, response):
        yield {
            'title': response.xpath("//title/text()").extract_first().strip()
        }
