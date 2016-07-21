# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy 
from scrapy.pipelines.images import ImagesPipeline


class CrawlerPipeline(object):
    def process_item(self, item, spider):
        return item

## Defining a pipeline to store images locally obtained from each article

class ImagePipeline(ImagesPipeline):

	def get_media_requests(self,item,info):
		for image in item['image_urls']:
			return scrapy.Request(image, meta={'item': item})

	def file_path( self , request , response= None , info = None):
		return '{}.jpg'.format(request.meta['item']['article_title'])
