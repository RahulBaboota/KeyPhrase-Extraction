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