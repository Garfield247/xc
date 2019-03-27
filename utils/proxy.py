#!/home/lvgang/.pyenv/shims/python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-26 09:08:30
# @Author  : LvGang/Garfield
# @Email   : Garfield_lv@163.com


import os
import requests



def random_proxy():
    proxy = 'http://'+requests.get(url='http://192.168.3.51:9527/api/rp').text
    proxies = {
        'http':proxy
    }
    return proxies
