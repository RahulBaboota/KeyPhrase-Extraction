"""

                                                Importing all the necessary libraries and classes 

"""
import scrapy
from scrapy.selector import Selector
from scrapy.spiders import Spider
from Crawler.items import *
import re
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

        ## Obtaining the categories for the corresponding links
        categories = response.xpath('//div[2]/header/nav/ul/li/a/text()').extract()

        ## Yielding scrapy requests to the category links obtained above 
        for ( category , category_link ) in zip( categories , category_links ):

            request1 = scrapy.Request( category_link , callback = self.parse_article_link )
            request1.meta['article_links'] = item
            yield request1

    '''


                                                Parsing through Article Links Layer 

    '''

    def parse_article_link(self,response):

        article_links = response.meta['article_links']


        ## Extracting all the available links from the landing page
        all_links = response.xpath('body//a/@href').extract()

        ## Now , we will filter out these links obtained to just contain the article links
        article_links_list = [] 
        regex_pattern = r"^http:\/\/www.nytimes.com\/(\d+)\/(\d+)\/(\d+)\/.+"

        for link in all_links:
            if (bool(re.match(regex_pattern,link))==True):
                article_links_list.append(link)
            else:
                pass

        ## Sending scrapy requests to the article links to extract the article text
        for article_link in article_links_list:

            request2 = scrapy.Request( article_link )
            request2.meta['article_info'] = article_links
            yield request2












