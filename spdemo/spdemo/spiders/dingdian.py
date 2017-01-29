# -*- coding:utf-8 -*-
import scrapy
from lxml import etree
from scrapy.http import Request
from spdemo.items import SpdemoItem
import sys
import pymongo
reload(sys)
sys.setdefaultencoding('utf-8')
class Myspider(scrapy.Spider):
    name = 'dingdian'
    num=0
    def start_requests(self):
        page=1
        s=1
        while page<14:
            url = 'https://search.jd.com/Search?keyword=fpga&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=fpga&page=%d&s=%d&click=0'%(page,s)
            yield Request(url,self.parse)
            page+=2
            s+=60
    def parse(self, response):

        data= response.xpath('//*[@id="J_goodsList"]/ul/li')
        for d in data:

            mo=SpdemoItem()
            first=d.xpath('div/div[3]/a/em/text()[2]').extract()
            second=d.xpath('div/div[3]/a/em/text()[1]').extract()
            key=d.xpath('div/div[3]/a/em/font/text()').extract()
            price=d.xpath('div/div[2]/strong/i/text()').extract()
            bname=d.xpath('div/div[4]/span[1]/a/text()').extract()
            bookurl=d.xpath('div/div[1]/a/@href').extract()
            mo['addr']='http:'+bookurl[0]
            self.num+=1
            if key!=[]:
                if first!=[]:
                    mo['_id']=str(self.num)+'.'+second[0]+key[0]+first[0]
                elif second!=[]:
                    mo['_id']=str(self.num)+'.'+key[0]+second[0]
            if bname!=[]:
                mo['writer']=bname[0];
            if price!=[]:
                mo['price']=price[0];
            yield mo
