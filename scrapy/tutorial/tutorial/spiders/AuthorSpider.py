import scrapy

class AuthorSpide(scrapy.Spider):
    name='author'

    strat_urls=['http://quotes.toscrape.com/']

    #先提取出需要的URL
    def parse(self,response):
        item=MyItem()
        for href in response.css('.authon + a::attr(href)'):
            yield response.follow(href,self.parse_author)

        for href in response.css('li.next a::attr(href)'):
            yield respons.follow(href,self.parse)

    def parse_author(self,response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()

        yield{
            'name': extract_with_css('h3.author-title::text'),
            'birthdate': extract_with_css('.author-born-date::text'),
            'bio': extract_with_css('.author-description::text'),            
            }
