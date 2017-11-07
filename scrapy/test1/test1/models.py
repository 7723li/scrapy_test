from sqlalchemy import Column, String, Text, Integer, TIME, create_engine
from sqlalchemy.ext.declarative import declarative_base
import os

Base=declarative_base()# 创建对象的基类

class Article(Base):
    __tablename__='Article'
    id=Column(Integer(),primary_key=True)
    link=Column(String(50))
    title=Column(String(50))
    posttime=Column(String(50))

def db_connect():
    basedir = os.path.abspath(os.path.dirname(__file__))#'C:\\Users\\Administrator\\scrapy\\test1\\test1'
    engine=create_engine('sqlite:///' + os.path.join(basedir, 'data.sqlite'))#create_engine()用来初始化数据库连接
    return engine

def create_news_table(engine):
    meta=Base.metadata
    meta.create_all(engine)
'''
DBSession=sessionmaker(bind=engine)# 创建DBSession类型
session = DBSession()# 创建session对象,DBSession对象可视为当前数据库连接
'''
