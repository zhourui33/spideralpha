import scrapy
from spideralpha.items import SpideralphaItem


class TxtSpider(scrapy.Spider):
	name = "txt"
	allowed_domains = ["farmer.com.cn"]
	start_urls = ["http://www.farmer.com.cn"]

	def parse(self,response):
		for sel in response.xpath('//div[@class="yaodian-xinwen"]'):
			item=SpideralphaItem()
			item['title']=sel.xpath('//p[@class="text-new"]/a/text()').extract()
			item['link']=sel.xpath('//p[@class="text-new"]/a/@href').extract()
			yield item
