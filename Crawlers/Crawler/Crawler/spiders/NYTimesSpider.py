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

        item = NYTimesItem()

        ## Obtaining the various links for news categories 
        category_links = response.xpath('//div[2]/header/nav/ul/li/a/@href').extract()
        print category_links

        ## Obtaining the categories for the corresponding links
        categories = response.xpath('//div[2]/header/nav/ul/li/a/text()').extract()
        print categories

        ## Yielding scrapy requests to the category links obtained above 
        for ( category , category_link ) in zip( categories , category_links ):

            request1 = scrapy.Request( category_link , callback = self.parse_article_link )
            request1.meta['article_links'] = item
            yield request1

    def parse_article_link(self,response):

        article_links = response.meta['article_links']


        ## Extracting the links for the subcategories on the category landing page

        category_links = response.xpath('body//a/@href').extract()
        # print len(category_links)

