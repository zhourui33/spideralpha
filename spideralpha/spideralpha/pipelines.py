# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SpideralphaPipeline(object):
    def __init__(self):
    	self.file = open("farmer.txt",mode="wb")
    def process_item(self, item, spider):
    	i=0
    	for title in item["title"]:
    		self.file.write(title.encode("utf-8"))
    		self.file.write("\n")
    		self.file.write(item['link'][i].encode("utf-8"))
    		self.file.write("\n")
    		i=i+1
        return item
