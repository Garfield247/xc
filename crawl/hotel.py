#!/home/lvgang/.pyenv/shims/python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-25 14:09:17
# @Author  : LvGang/Garfield
# @Email   : Garfield_lv@163.com


import os
import json
import redis
import requests
from lxml import etree
from urllib import parse
from datetime import datetime,timedelta
from utils import RedisDB,random_proxy

class Xchtl(object):
    """docstring for Xchtl"""
    def __init__(self, city):
        self.db = RedisDB()
        self.city = city
        self.city_name = city['city_name']
        self.city_pinyin = city['city_pinyin']
        self.city_id = city['city_id']
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
            }

    def _get(self,url):
        response = requests.get(url=url,headers=self.headers,proxies=random_proxy(),timeout=3)
        return response

    def _post(self,url,formdata):
        try:
            response = requests.post(url=url,data=formdata,headers=self.headers,proxies=random_proxy(),timeout=5)
        except:
            response = requests.post(url=url,data=formdata,headers=self.headers,proxies=random_proxy(),timeout=5)
        return response

    def parse_htl(self, response):
        try:
            res = json.loads(response.text)
            # print(res)
            htl_count = res.get('hotelAmount')
            htl_l = res.get('hotelPositionJSON')
            page_count = len(htl_l)
            for htl in htl_l:
                htl['city_name'] = self.city_name
                htl['url'] = 'http://hotels.ctrip.com/'+htl['url']
                self.db.write_data(key='xchtl:hotels',item=htl)
            return (page_count%htl_count+1)
        except Exception as e:
            print(e)
            self.db.write_data(key='xchtl:citys',item=self.city)
            return 1

    def crawl_htl(self,page):
        url_hl = 'http://hotels.ctrip.com/Domestic/Tool/AjaxHotelList.aspx'
        data_hl = {
            'cityName':parse.quote(self.city_name),
            'StartTime':str(datetime.now().date()),
            'DepTime':str(datetime.now().date()+timedelta(days=1)),
            'cityId':self.city_id,
            'cityPY':self.city_pinyin,
            'page':page,
        }

        pgnu = self.parse_htl(self._post(url=url_hl, formdata=data_hl))

        return pgnu




    def main(self):
        pgnu = self.crawl_htl(1)
        for i in range(pgnu):
            self.crawl_htl(i+1)
