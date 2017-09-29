# -*- coding: utf-8 -*-
import datetime
import re

import scrapy


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    #开始爬虫的入口
    # start_urls = ['http://blog.jobbole.com/111968/']
    start_urls = ['http://blog.jobbole.com/112530/']

    def parse(self, response):

        title=response.css(".entry-header h1::text").extract()
        create_time=response.css(".entry-meta-hide-on-mobile::text").extract()[0].split()[0]
        create_time=datetime.datetime.strptime(create_time,"%Y/%m/%d").date()
        thumbup_nums=response.css(".post-adds h10::text").extract()[0]
        match_re=re.match(".*?(\d+).*",thumbup_nums)
        if match_re:
            thumbup_nums=int(match_re.group(1))
        else:
            thumbup_nums=0
        bookmark_nums=response.css(".post-adds .bookmark-btn::text ").extract()[0]
        match_re = re.match(".*?(\d+).*", bookmark_nums)
        if match_re:
            bookmark_nums = int(match_re.group(1))
        else:
            bookmark_nums = 0
        comment_nums=response.css(".post-adds a span::text ").extract()[0]
        match_re = re.match(".*?(\d+).*", comment_nums)
        if match_re:
            comment_nums = int(match_re.group(1))
        else:
            comment_nums = 0
        content=response.css(".entry p").extract()

        tags=response.css(".entry-meta-hide-on-mobile a::text").extract()
        tags=[element for element in tags if not element.strip().endswith("评论")]
        tags=','.join(tags)





        pass


