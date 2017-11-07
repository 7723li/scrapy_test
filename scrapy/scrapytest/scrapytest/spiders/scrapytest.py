import scrapy
from bs4 import BeautifulSoup as bs

class TestSpider(scrapy.Spider):
    name='test'
    start_urls=['https://www.xncoding.com/2016/03/08/scrapy-01.html'
                ,]

    def parse(self,response):
        code=response.xpath('//figure[@class="highlight python"]/table/tr/td[@class="code"]').extract()[0]
        soup=bs(code,'lxml')
        line_div=soup.find_all('div',class_='line')
        for i,j in enumerate(line_div):
            print(i,j)
            yield {
                i:j.text
            }
