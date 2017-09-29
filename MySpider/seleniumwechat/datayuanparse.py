from scrapy.selector import Selector
from selenium import webdriver
import time



def reloaddata(timesearch):
    browser = webdriver.Chrome(executable_path="/home/truthliu/Downloads/chromedriver")
    #打开网页
    browser.get(timesearch)
    #加载当天更多的文章
    try:
        while browser.find_element_by_css_selector(".morediv"):
            browser.find_element_by_css_selector(".morediv").click()
            time.sleep(1)
    except:
        print("--------------------")
    # print(browser.page_source)

    return browser.page_source






print(reloaddata(timesearch="http://www.datayuan.cn//searchTime.htm?time=2017-09-18"))
