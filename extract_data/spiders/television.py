import scrapy;
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from extract_data.items import ExtractDataItem
import re

class TelevisionSpider(CrawlSpider):
    name = 'television'
    allowed_domains = ['uae.souq.com']
    start_urls = ['https://uae.souq.com/ae-en/lcd-led-dlp-tv/l/']

    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('.pagination-next',), process_value= lambda value: value + '&section=2'),
             callback="parse_item",
             follow=True),)

    def parse_item(self, response):
        item_links = response.css('.itemTitle > .itemLink::attr(href)').extract()
        print(len(item_links))
        for a in item_links:
            yield scrapy.Request(a, callback=self.parse_detail_page)

    def parse_detail_page(self, response):
        title = response.css('h1::text').extract()[0].strip()
        price_value = response.css('.price.is.sk-clr1').extract()[0]
        price = re.findall("\d+(?:[\d,.]*\d)", price_value)[0]
        currency = response.css('.price > .currency-text::text').extract()[0].strip()
        size = response.css('.size-value::text').extract()[0]
        image = response.css('.img-bucket > img').xpath('@src').extract()[0].strip()

        item = ExtractDataItem()
        item['title'] = title
        item['price'] = price
        item['currency'] = currency
        item['size'] = size
        item['image'] = image
        item['url'] = response.url
        yield item

    def process_value(val): 
        return val + '&section=2'