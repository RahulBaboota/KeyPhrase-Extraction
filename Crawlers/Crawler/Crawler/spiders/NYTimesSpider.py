"""

												Importing all the necessary libraries and classes 

"""
import scrapy
from scrapy.selector import Selector
from scrapy.spider import Spider
from Crawler.items import *

""" 

												Initiating the SpiderClass

"""

class NYTimes(Spider):
	name = 'NYTimesSpider'
	start_urls = ['http://international.nytimes.com/']
	allowed_domains = []

	'''


												Parsing through News Categories Layer 

	'''

	def parse(self,response):

		## Obtaining the various links for news categories 
		category_links = response.xpath('//div[2]/header/nav/ul/li/a/@href').extract()

		##Obtaining the categories for the corresponding links
		categories = response.xpath('//div[2]/header/nav/ul/li/a/text()').extract()

