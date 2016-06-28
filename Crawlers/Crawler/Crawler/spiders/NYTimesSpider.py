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

		world_news = response.xpath('//div[2]/header/nav/ul/li[3]/a/@href').extract()[0]
		US_news = response.xpath('//div[2]/header/nav/ul/li[4]/a/@href').extract()[0]
		politics_news = response.xpath('//div[2]/header/nav/ul/li[5]/a/@href').extract()[0]
		NY_news = response.xpath('//div[2]/header/nav/ul/li[6]/a/@href').extract()[0]
		business_news = response.xpath('//div[2]/header/nav/ul/li[7]/a/@href').extract()[0]
		int_business_news = response.xpath('//div[2]/header/nav/ul/li[8]/a/@href').extract()[0]
		opinions_news = response.xpath('//div[2]/header/nav/ul/li[9]/a/@href').extract()[0]
		int_opinions_news = response.xpath('//div[2]/header/nav/ul/li[10]/a/@href').extract()[0]
		technology_news = response.xpath('//div[2]/header/nav/ul/li[11]/a/@href').extract()[0]
		science_news = response.xpath('//div[2]/header/nav/ul/li[12]/a/@href').extract()[0]
		health_news = response.xpath('//div[2]/header/nav/ul/li[13]/a/@href').extract()[0]
		sports_news = response.xpath('//div[2]/header/nav/ul/li[14]/a/@href').extract()[0]
		int_sports_news = response.xpath('//div[2]/header/nav/ul/li[15]/a/@href').extract()[0]
		art_news = response.xpath('//div[2]/header/nav/ul/li[16]/a/@href').extract()[0]
		int_art_news = response.xpath('//div[2]/header/nav/ul/li[17]/a/@href').extract()[0]
		fashion_news = response.xpath('//div[2]/header/nav/ul/li[18]/a/@href').extract()[0]
		int_fashion_news = response.xpath('//div[2]/header/nav/ul/li[19]/a/@href').extract()[0]
		food_news = response.xpath('//div[2]/header/nav/ul/li[20]/a/@href').extract()[0]
		int_food_news = response.xpath('//div[2]/header/nav/ul/li[21]/a/@href').extract()[0]
		travel_news = response.xpath('//div[2]/header/nav/ul/li[22]/a/@href').extract()[0]
		magazine_news = response.xpath('//div[2]/header/nav/ul/li[23]/a/@href').extract()[0]
		tmagazine_news = response.xpath('//div[2]/header/nav/ul/li[24]/a/@href').extract()[0]
		real_estate_news = response.xpath('//div[2]/header/nav/ul/li[25]/a/@href').extract()[0]



