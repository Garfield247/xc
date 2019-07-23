#!/home/lvgang/.pyenv/shims/python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-26 10:18:56
# @Author  : LvGang/Garfield
# @Email   : Garfield_lv@163.com


import os

import re
from selenium import webdriver
from lxml import etree
from utils import new_browser,memory_status
from selenium.webdriver.common.keys import Keys

def get_prices(url):
    browser = new_browser('firefox')
    memory_status()
    browser.delete_all_cookies()
    memory_status()
    browser.get(url)
    page = 1
    html = browser.page_source
    page = etree.HTML(html)
    prices = list(set([t.replace(r'<span class=\"line\">|</span>','') for t in page.xpath('.//td[@class="child_name J_Col_RoomName"]/@data-baseroominfo')]))
    browser.close()
    # print(prices)
    return prices

