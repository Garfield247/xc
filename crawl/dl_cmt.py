#!/home/lvgang/.pyenv/shims/python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-25 15:53:04
# @Author  : LvGang/Garfield
# @Email   : Garfield_lv@163.com

import os
import re
from selenium import webdriver
from bs4 import BeautifulSoup
from lxml import etree
import time
import json
from selenium.webdriver.common.keys import Keys

def save_data(hotel):
    city_name = hotel['city_name']
    hotel_name = hotel['name']
    data = json.dumps(hotel,ensure_ascii=False)
    file_path = os.path.abspath('./data/%s/'%city_name)
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    file_name = os.path.join(file_path,'%s.json'%hotel_name)
    with open(file_name,'a',encoding='utf-8') as fp:
        fp.write(data+'\n')

def parse_cmt(html,hotel):
    page = etree.HTML(html)
    items = []
    for cmt in page.xpath('.//div[@class="comment_block J_asyncCmt"]'):
        item = {}
        item['cmt_usr_name'] = cmt.xpath('.//div[@class="user_info  J_ctrip_pop"]/p[@class="name"]/span/text()')
        item['cmt_score'] = cmt.xpath('.//div[@class="comment_main"]/p[@class="comment_title"]/span[@class="small_c"]/@data-value')
        item['cmt_room_type'] = cmt.xpath('.//div[@class="comment_main"]/p[@class="comment_title"]/a/text()')
        item['cmt_check_in_date'] = cmt.xpath('.//span[@class="date"]/text()')
        item['cmt_cause'] = cmt.xpath('.//span[@class="type"]/text()')
        item['cmt_content'] = cmt.xpath('.//div[@class="J_commentDetail"]/text()')
        item['cmt_device'] = cmt.xpath('.//p[@class="comment_bar_info"]/i/@class')
        item['cmt_date'] = cmt.xpath('.//p[@class="comment_bar_info"]/span[@class="time"]/text()')
        item['cmt_upvote'] = cmt.xpath('.//a[@class="useful"]/@data-voted')
        for k in item.keys():
            if len(item[k])==1:
                item[k] = item[k][0]
            elif len(item[k])==0:
                item[k] = None
        item['cmt_score'] = {i[0]:i[1] for i in re.findall(r'(.*?):(.*?),',item['cmt_score']+',')}
        hotel['comment'] = item
        save_data(hotel)


def dl_cmt_page(hotel):
    url = hotel['url']
    opt = webdriver.ChromeOptions()
    opt.add_argument('--headless')
    opt.add_argument('--no-sandbox')
    opt.add_argument('--disable-extensions')
    opt.add_argument('--disable-gpu')
    browser = webdriver.Chrome(options=opt)
    browser.get(url)
    page = 1
    html = browser.page_source
    body = BeautifulSoup(html,"html.parser")
    # pages = int(re.findall(r'\((\d+)\)',body.find('span',{"id":"All_Comment"}).get_text())[0])/15+1
    pages = 2
    while page<pages:
        html = browser.page_source
        parse_cmt(html,hotel)
        page += 1
        input = browser.find_element_by_xpath("//input[@id='cPageNum']")
        input.clear()
        input.send_keys(page)
        input.send_keys(Keys.ENTER)
        time.sleep(2)
    browser.close()


