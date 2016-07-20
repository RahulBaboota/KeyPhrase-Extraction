# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field , Item


class NYTimesItem(Item):
	article = Field()
	post_date = Field()
	text_type = Field()
	article_title = Field()
	article_description = Field()
	category = Field()
	authors = Field()
	keywords = Field()


