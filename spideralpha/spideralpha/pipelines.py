# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SpideralphaPipeline(object):
    def __init__(self):
    	self.file = open("farmer.txt",mode="wb")
    def process_item(self, item, spider):
    	self.file.write(item['title'][1].encode("utf-8"))
    	self.file.write("\n")
    	self.file.write(item['link'][1].encode("utf-8"))
    	self.file.write("\n")
        return item
