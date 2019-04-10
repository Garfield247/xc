#!/home/lvgang/.pyenv/shims/python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-26 09:08:30
# @Author  : LvGang/Garfield
# @Email   : Garfield_lv@163.com

from selenium import webdriver

def new_browser():
    opt = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    opt.add_experimental_option("prefs", prefs)
    opt.add_argument('disable-infobars')
    opt.add_experimental_option('excludeSwitches', ['enable-automation'])
#    opt.add_argument('--headless')
    opt.add_argument('--no-sandbox')
    opt.add_argument('--disable-extensions')
    opt.add_argument('--disable-gpu')
    opt.add_argument('--window-size=1280,800')  # 设置窗口大小
    opt.add_experimental_option('excludeSwitches', ['enable-automation'])
    b = webdriver.Chrome(options=opt)
    return b
