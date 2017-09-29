# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from urllib import parse
import datetime


class WechatSpider(scrapy.Spider):
    name = 'wechat'
    # allowed_domains = ['bigdata']
    start_urls = ['http://wx.shenchuang.com/article/list-3.html']

    def parse(self, response):

        #解析列表页面中的所有文章
        post_urls=response.css(".list2 h3 a::attr(href)").extract()
        print(response.url+"==============")
        #解析具体页面
        for post_url in post_urls:
            print("--------------"+parse.urljoin(response.url,post_url)+"---------------")
            # yield Request(url=parse.urljoin(response.url,post_url),callback=self.parse_detail)
            yield Request(url=parse.urljoin(response.url, post_url),callback=self.parse_detail)

        #解析下一页 extract_first()取第一个
        next_url= response.css(".list2 .easypagerNormalpage::attr(href)").extract_first()
        if next_url:
            yield Request(url=parse.urljoin(response.url,next_url),callback=self.parse)

        pass

    def parse_detail(self,response):
        title=response.css(".listltitle h3::text").extract()
        date_time=response.css(".spanimg3::text").extract_first().split()[0]
        date_time=datetime.datetime.strptime(date_time,'%Y-%m-%d').date()
        content= response.css(".article-content")

        
        pass