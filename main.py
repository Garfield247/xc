#!/home/lvgang/.pyenv/shims/python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-25 15:28:46
# @Author  : LvGang/Garfield
# @Email   : Garfield_lv@163.com


import os
import re
import json
import requests
from time import sleep
from utils import RedisDB
from crawl import get_city,Xchtl

db = RedisDB()


def main():
    if db.get_data_count(key='xchtl:citys')==0:
        citys = get_city()
        for city in citys:
            db.write_data(key='xchtl:citys',item=city)
    while db.get_data_count('xchtl:citys')>0:
        city = db.get_data('xchtl:citys')
        xchtl = Xchtl(city=city)
        xchtl.main()





if __name__ == '__main__':
    main()
