from test1.items import Test1Item
import scrapy

class HuxiuSpider(scrapy.Spider):
    name='huxiu'
    allowed_domains=['huxiu.com']
    start_urls=[
        'http://www.huxiu.com/index.php',]

    def parse(self,response):
        for sel in response.xpath('//div[@class="mod-info-flow"]/div/div[@class="mob-ctt"]'):
            item = Test1Item()
            #print(dir(item))
            try:
                item['title'] = sel.xpath('h2/a/text()')[0].extract()
            except IndexError:
                item['title']='空'
                
            try:
                item['link'] = sel.xpath('h2/a/@href')[0].extract()
                url = response.urljoin(item['link'])
                print(url)
            except IndexError:
                item['title']='空'
                
            try:
                item['desc'] = sel.xpath('div[@class="mob-sub"]/text()')[0].extract()
            except IndexError:
                item['desc']='空'
                
            yield scrapy.Request(url,callback=self.parse_article)

    def parse_article(self,response):
        #self.logger.info('Hi, this is an item page! %s', response.url)
        detail = response.xpath('//div[@class="article-wrap"]')
        item = Test1Item()
        item['title'] = detail.xpath('h1/text()')[0].extract()
        item['link'] = response.url
        item['posttime'] = detail.xpath('//span[@class="article-time pull-left"]/text()')[0].extract()
        print(item['title'],item['link'],item['posttime'])
        yield item

