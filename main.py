# -*- coding: utf-8 -*-

from selenium import webdriver

driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe')
#  driver = webdriver.PhantomJS('D:/Program Files/phantomjs-2.1.1-windows/bin/phantomjs.exe')
#  url = 'http://www.gsxt.gov.cn/corp-query-homepage.html'
url = 'http://www.gsxt.gov.cn'
driver.get(url)
driver.execute_script(driver.page_source)
driver.get(url)
with open('./companys.txt', 'w') as f:
    f.write(driver.page_source)
