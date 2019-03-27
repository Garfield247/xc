#!/home/lvgang/.pyenv/shims/python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-25 15:24:32
# @Author  : LvGang/Garfield
# @Email   : Garfield_lv@163.com




import redis
import json
from random import choice

from .config import REDIS_HOST, REDIS_PORT, REDIS_DB
# REDIS_HOST = '192.168.3.100'
# REDIS_PORT = '6379'
# REDIS_KEY_DATA = 'crawl_data'

class RedisDB(object):
    """docstring for RW_redis"""
    def __init__(self):
        self.redis_cli = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)



    def get_data_count(self,key):
        try:
            count = self.redis_cli.llen(key)
            return count
        except:
            return 0


    def get_data(self,key):
        json_obj = self.redis_cli.lpop(key)
        if json_obj:
            data = json.loads(json_obj)
            return data
        else:
            return None

    def write_data(self,key,item):
        #从右端入队一条数据
        data = json.dumps(item,ensure_ascii=False)
        self.redis_cli.rpush(key,data)
