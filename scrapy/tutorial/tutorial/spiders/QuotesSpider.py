import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    
    
    def start_requests(self):
        url = 'http://quotes.toscrape.com/'
        
        #获取tag内置方法
        tag=getattr(self,'tag',None)
        if tag is not None:
            print(tag)
            print('='*50)
            url=url+'tag/'+tag
        
        #每收到链接的响应，就将响应对象实例化
        #for url in urls:
        yield scrapy.Request(url=url, callback=self.parse)
    
    '''
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]
    '''
    
    #parse() is Scrapy’s default callback method(回调函数)
    def parse(self, response):
        '''
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        '''
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }

        #next_page=response.xpath('//ul[@class='pager']/li[@class='next']/a/@href').extract_first()
        #等于
        #next_page = response.css('li.next a::attr(href)').extract_first()
        next_page=None
        if next_page is not None:
            '''
            next_page = response.urljoin(next_page)
                                            #回调自己的解析函数,即此处递归
            yield scrapy.Request(next_page, callback=self.parse)
            '''
            #此处支持相对地址，不需要使用urljoin方法生成绝对地址
            yield response.follow(next_page, callback=self.parse)
        #等于
        #response.follow uses their href attribute automatically  
        #for a in response.css('li.next a'):
                    #response.follow方法包含了response.Request方法，
                    #传入选择器参数可自动进行下一页的爬取            
        #    yield response.follow(a, callback=self.parse)
        #====or====
        #for href in response.css('li.next a::attr(href)'):
        #    yield response.follow(href, callback=self.parse)

#>>> response.css('title::text').()
#['Quotes to Scrape']
#extract 提取

#There are two things to note here: one is that we’ve added ::text to the CSS
#query, to mean we want to select only the text elements directly inside <title>
#element. If we don’t specify ::text, we’d get the full title element,
#including its tags:


#>>> response.css('title').extract()
#['<title>Quotes to Scrape</title>']

#>>> response.css('title::text').extract_first()
#'Quotes to Scrape'
