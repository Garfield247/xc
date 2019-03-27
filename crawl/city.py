#!/home/lvgang/.pyenv/shims/python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-25 15:47:14
# @Author  : LvGang/Garfield
# @Email   : Garfield_lv@163.com


import re
import json
import requests

def get_city():
    city_url = 'http://hotels.ctrip.com/Domestic/Tool/AjaxGetCitySuggestion.aspx'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
        }
    r_city = requests.get(url = city_url,headers=headers)
    citys = [{'city_name':city.split('|')[1],'city_pinyin':city.split('|')[0],'city_id':city.split('|')[2]} for city in list(set(re.findall(r'{display:".*?",data:"(.*?)",group:".*?"}',r_city.text)))]
    return citys

