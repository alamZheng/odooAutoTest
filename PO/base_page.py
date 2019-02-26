#!/usr/bin/python
# -*- coding:utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import time


class BasePage(object):
    #初始化
    def __init__(self,se_driver):
        self.driver = se_driver

    #定义open方法
    def open(self,url,page_title=None):
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.get(url)
        if page_title is not None:
            assert page_title in self.driver.title

    #重写元素定位的方法
    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except AttributeError:
            print(u"%s 页面中未能找到 %s 元素" % (self, loc))

    #定义script方法，用于执行js脚本
    def script(self,src):
        self.driver.execute_script(src)

    #重写send_keys方法
    def send_keys(self,value,clear_first=True,click_first=True,*loc):
        try:
            if click_first:
                self.find_element().click()
            if clear_first:
                self.find_element().clear()
                self.find_element().send_keys(value)

        except AttributeError:
            print(u'找不到元素:'+str(loc))

    # def send_enter(self,*loc):
    #     try:
    #         time.sleep(5)
    #         self.find_element(*loc).send_keys(Keys.ENTER)
    #     except AttributeError:
    #         print("未找到%s"%(self,*loc))

    # def take_screenshot(self):
    #     timeString =str(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()))
    #     pic_path = '.\\report\\report' + timeString +'screenshow.png'
    #     self.driver.save_screenshot(pic_path)

    def add_img(self,imgs):
        imgs.append(self.driver.get_screenshot_as_base64())
        return True

    # def select_dropdown(self,*loc,optionName):
    #     try:
    #         Select(self.find_element(*loc)).select_by_visible_text(optionName)
    #     except AttributeError:
    #         print("select_dropdown未找到%s"%(self,loc))
        
