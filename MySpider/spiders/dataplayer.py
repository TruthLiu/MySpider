# -*- coding: utf-8 -*-
import scrapy
from urllib import parse
from scrapy import Request
from datetime import datetime

from MySpider.settings import PATH
import os
from selenium import webdriver
from scrapy.selector import Selector
#将加载的网页导过来
from MySpider.seleniumwechat.datayuanparse import reloaddata
import re
import time

import pdfkit

class DataplayerSpider(scrapy.Spider):
    name = 'dataplayer'
    # allowed_domains = ['bigdata']
    start_urls = ['http://www.datayuan.cn//searchTime.htm?time=2017-09-18']


    def parse(self,response):


        for i in range(1):
            articletime="http://www.datayuan.cn//searchTime.htm?time=2017-09-"+str(i)
            response=reloaddata(timesearch=articletime)
            response=Selector(text=response)
            try:
                url_lists=response.css(".main-div-l h2 a::attr(href)").extract()
            except:
                re_article=re.match(".*time=(\d{4}-\d{1,2}-\d{1,2})")
                notime=re_article.group(1)
                print(notime+"没有文章!!!!!!!!!!!")
                continue

            for url_list in url_lists:
                # url_list=parse.urljoin(response.url,url_list)
                # print(url_list)

                # yield Request(url=url_list,callback=self.parse_detail)

                browser=webdriver.Chrome(executable_path="/home/truthliu/Downloads/chromedriver")
                browser.get(url_list)
                t_selector=Selector(text=browser.page_source)
                try:
                    title=t_selector.css(".wz-div h1::text").extract_first().strip()
                except:
                    print("文章为空-------")
                    continue
                # for i in 2:
                #     #加载数据
                #     browser.execute_script("window.scrollTo(0,document.body.scrollHeight); var lenOfPage=document.body.scrollHeight; return lenOfPage")

                file_name=title+".pdf"
                file_path="%s/%s"%(PATH+"/dataplayer",file_name)
                pdfkit.from_url(browser.current_url,file_path)

                # browser.get_screenshot_as_file(file_path)
                # os.system("cd /home/truthliu/Downloads/wkhtmltox/bin/wkhtmltopdf")

                time.sleep(2)
                browser.close()
                # file_=open(file_path,'w')
                # file_.write(browser.page_source)
                # file_.close()

                pass













            # def parse_detail(self,response):
            #     title= response.css(".wz-div h1::text").extract()[0].strip()
            #     # create_time=datetime.strptime(create_time,"%Y-%m-%d").date()
            #     content=response.css(".wz-div").extract()
            #
            #     #对动态页面进行加载
            #
            #
            #
            #
            #     # isExists=os.path.exists(PATH+"/dataplayer")
            #     # if not isExists:
            #     #     os.mkdir(PATH+"/dataplayer")
            #     #
            #     #
            #     #
            #     # with open(file_path,'wb') as file_write:
            #     #
            #     #     file_write.write(content)
            #     #     file_write.close()

            #     # browser.get(response)


