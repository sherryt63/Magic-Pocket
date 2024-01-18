#爬取所需网页内容


#导入scrapy库；导入在items.py（由于在上一个文件夹，故要加..）里定义的类
import scrapy
from ..items import DangdangItem

#定义爬虫类spider
class DdSpider(scrapy.Spider):
    name='csbook'
    allowed_domains=['dangdang.com'] #爬取的网站
    start_urls=['https://search.dangdang.com/?key=%BC%C6%CB%E3%BB%FA'] #爬取的特定书籍网站


    def parse(self,response):
        #使用XPath从页面的HTML源码中选择需要提取的数据
        #根据对HTML源码的观察，设置XPath解析规则提取出所有书籍信息csbooks
        csbooks=response.xpath('//ul[@class="bigimg"]/li')

        #对提取到的所有图书信息遍历，提取每一本书的相关信息
        for csbook in csbooks:
            item=DangdangItem() #生成item对象，用于存储提取到的信息
            item['name']=csbook.xpath('./a[@class="pic"]/@title').extract()
            item['author']=csbook.xpath('./p/span[1]/a[1]/@title').extract() if len(csbook.xpath('./p/span[1]/a[1]/@title'))>0 else '无作者信息'
            item['introduction']=csbook.xpath('./p[@class="detail"]/text()').extract() if len(csbook.xpath('./p[@class="detail"]/text()'))>0 else '无简介信息'
            item['price']=csbook.xpath('./p/span[@class="search_now_price"]/text()').extract()
            item['press']=csbook.xpath('./p[5]/span[3]/a/text()').extract() if len(csbook.xpath('./p/span[3]/a/text()'))>0 else '无出版社信息'
            item['time']=csbook.xpath('./p[5]/span[2]/text()').extract() if len(csbook.xpath('./p/span[2]/text()'))>0 else '无出版时间信息'
            item['comment_num']=csbook.xpath('./p[4]/a[@class="search_comment_num"]/text()').extract() if len(csbook.xpath('./p[4]/a[@class="search_comment_num"]/text()'))>0 else'无评论信息'

            #将提取到的数据交给pipelines进行保存输出
            yield item

        #设置爬取的页面pageNum，爬取10个页面的图书信息
        pageNum=10
        #根据url的规则构建新的url，即page，将page提交给scrapy engine进行处理
        for page in range(2,pageNum):
            page='https://search.dangdang.com/?key=%BC%C6%CB%E3%BB%FA&act=input&page_index={}'.format(page)

            #对页面page提交request请求，用自定义的解析方法parse对获取到的页面进行解析
            yield scrapy.Request(page,callback=self.parse)

