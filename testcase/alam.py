# !/usr/bin/python
# -*- coding:utf-8 -*-
import sys
sys.path.append("..")
from utils.Util_configparser import ConfigUtils
from selenium import webdriver




def alam():
    # str="//div[@id = 'notebook_page_26']/div[2] / div[2] / div[2] / table / tbody / tr / td[3]"
    # print(str.replace("[2]","",1))
    # browser = webdriver.Chrome()
    str = 'aaa,bbb'
    print(tuple(str.split(",")))
    print(tuple(tuple(str.split(","))))

if __name__ == '__main__':
    # api = sys.argv[1]
    # print(api)
    # # ConfigParser.set("testdata","PLMPage","test",api)
    # ConfigUtils("testdata").set_section_key_value('PLMPage', "test", api)
    # print("alam test")
    alam()
