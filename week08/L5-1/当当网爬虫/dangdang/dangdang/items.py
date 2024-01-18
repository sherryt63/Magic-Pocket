# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DangdangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    name=scrapy.Field() #书名
    author=scrapy.Field() #作者
    introduction=scrapy.Field() #简介
    price=scrapy.Field() #价格
    press=scrapy.Field() #出版社
    time=scrapy.Field() #出版时间
    comment_num=scrapy.Field() #评价数目

    #Field的做法是创建一个字典，给字典添加一个键，暂时不赋值，提取数据后再赋值。
