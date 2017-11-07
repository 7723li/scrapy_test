# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from sqlalchemy.orm import sessionmaker
from test1.models import Article,db_connect,create_news_table

class Test1Pipeline(object):
    def __init__(self):
        engine=db_connect()
        create_news_table(engine)
        DBSession=sessionmaker(bind=engine)
        self.session=DBSession()

    def open_spider(self,Spider):
        """This method is called when the spider is opened."""
        pass

    def process_item(self,item,spider):
        a = Article(link=item["link"],
                    title=item["title"],
                    posttime=item["posttime"],)

        self.session.add(a)
        self.session.commit()
        self.session.close()

    def close_spider(self, spider):
        pass
