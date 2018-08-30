# -*- coding: utf-8 -*-

import requests
from requests.cookies import RequestCookieJar
import lxml

headerdata = {
    "geetest_challenge":   "a1d0c6e83f027327d8461063f4ac58a692",
    "geetest_seccode": "be6bbff39c53eab75a68af2347b57fd7|jordan",
    "geetest_validate":    "be6bbff39c53eab75a68af2347b57fd7",
    "province":"",
    "searchword":  "区块链",
    "tab": "ent_tab",
    "token":   "98583642"
}

headers = {
    "Accept": "text/html,application/xhtml+xm…plication/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Connection": "keep-alive",
    "Content-Length":  "227",
    "Content-Type":  "application/x-www-form-urlencoded",
    "Host": "www.gsxt.gov.cn",
    "Referer": "http://www.gsxt.gov.cn/index.html",
    "Upgrade-Insecure-Requests": "1",
    "X-Forwarded-For": "120.85.102.227",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"
}

cookies_jar = RequestCookieJar()
cookies_jar.set("__jsl_clearance", "1535634953.458|0|cdSFaASwJvSt+sRwc6WrZMfwxUg=")
cookies_jar.set("__jsluid", "e5ae9c0dff28dc050d15f2676609698c")
cookies_jar.set("CNZZDATA1261033118", "290523213-1535351681-http%3A%2F%2Fwww.gsxt.gov.cn%2F|1535632575")
cookies_jar.set("JSESSIONID", "31CCD2A85CC7269A62ABD3EF85A94BE4-n2:4")
cookies_jar.set("SECTOKEN", "7097534261986329306")
cookies_jar.set("tlb_cookie", "S172.16.12.68")
cookies_jar.set("UM_distinctid", "165835499288e-03d2b6d633fa3a-4c312b7b-1fa400-165835499291e6")

url = 'http://www.gsxt.gov.cn/corp-query-search-1.html'
page = requests.post(url, data = headerdata, cookies = cookies_jar)
html = page.text
print(html)
#  selector = etree.HTML(html)
#  company = selector.xpath()
