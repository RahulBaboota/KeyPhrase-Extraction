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
            if (re.match(regex_pattern,link)):
                article_links_list.append(link)
            else:
                pass

        ## Sending scrapy requests to the article links to extract the article text
        for article_link in article_links_list:

            request2 = scrapy.Request( article_link , callback = self.parse_article_info )
            request2.meta['article_info'] = article_links
            yield request2

    '''


                                                Parsing through Article Information Layer 

    '''

    def parse_article_info(self,response):

        article_info = response.meta['article_info']

        ## Creating a list of the article text
        text_list = response.xpath('//*[contains(@class, "story-body")]//p/text()').extract()
        article_info['article'] = ' '.join(text_list).strip()

        ## Article post date
        try:
            article_info['post_date'] = response.xpath('//meta[@name="dat"]/@content').extract()[0]
        except IndexError:
            article_info['post_date'] = ''

        ##  Defining the text type
        article_info['text_type'] = response.xpath('//meta[@property="og:type"]/@content').extract()[0]

        ## Defining the article title
        article_info['article_title'] = response.xpath('//meta[@property="og:title"]/@content').extract()[0]

        ## Defining the article description
        article_info['article_description'] = response.xpath('//meta[@property="og:description"]/@content').extract()[0]

        ## Article Category
        article_info['category'] = response.xpath('//meta[@itemprop="articleSection"]/@content').extract()[0]

        ## Article Authors
        article_info['authors'] = response.xpath('//meta[@name="author"]/@content').extract()[0]

        ## Extracting the keywords from the article
        article_info['keywords'] = response.xpath('//meta[@name="keywords"]/@content').extract()[0]

        yield article_info
















