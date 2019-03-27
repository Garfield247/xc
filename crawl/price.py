#!/home/lvgang/.pyenv/shims/python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-26 10:18:56
# @Author  : LvGang/Garfield
# @Email   : Garfield_lv@163.com


import os

import re
from selenium import webdriver
from lxml import etree
import time
from selenium.webdriver.common.keys import Keys

def get_prices(url):
    opt = webdriver.ChromeOptions()
    opt.add_argument('--headless')
    opt.add_argument('--no-sandbox')
    opt.add_argument('--disable-extensions')
    opt.add_argument('--disable-gpu')
    browser = webdriver.Chrome(options=opt)
    browser.get(url)
    page = 1
    html = browser.page_source
    page = etree.HTML(html)
    prices = list(set([t.replace(r'<span class=\"line\">|</span>','') for t in page.xpath('.//td[@class="child_name J_Col_RoomName"]/@data-baseroominfo')]))

    browser.close()
    print(prices)
    return prices

