import scrapy

class TxtSpider(scrapy.Spider):
	name = "txt"
	allowed_domains = ["farmer.com.cn"]
	start_urls = ["http://www.farmer.com.cn"]

	def parse(self,response):
		for sel in response.xpath(''):
			item=SpideralphaItem
			item['title']=sel.xpath('').extract()
			item['content']=sel.xpath('').extract()
			yield item
