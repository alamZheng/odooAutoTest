#!/usr/bin/python
# -*- coding:utf-8 -*-

from utils.Util_configparser import ConfigUtils
from PO import base_page

import sys
sys.path.append("..")


class odoo12_pos_page(base_page.BasePage):

    '''根据element.ini动态生成每个元素和定位值
    name_loc = id,login'''
    names = locals()
    keys = ConfigUtils("PO").get_keys_by_section('odoo12_Pos_page')
    for key in keys:
        # print(key)
        names[key] = ConfigUtils("PO").get_values_by_key('odoo12_Pos_page', key)

    def access_Pos(self):
        # self.open(str(self.login_url))
        self.click_element_className_by_js('i',"fa.fa-th-large")
        self.click_a_text_by_js("POS")

    def access_Pos_dashboard(self):
        # self.open(str(self.login_url))
        self.click_element_className_by_js('i',"fa.fa-th-large")
        self.click_a_text_by_js("POS")
        self.click_a_text_by_js("仪表板")
        self.click_button_text_by_js("重新开始")

    search_product_loc = 'xpath','//input'
    pos_last_pay_loc ='css selector',"div.payment-screen.screen > div.screen-content > div.top-content > span.button.next"
    def place_Pos_order(self):
        #搜索产品
        self.wait(2)
        self.find_element(*self.search_product_loc).send_keys("2030140")
        self.send_enter(*self.search_product_loc)
        self.click_className_text_by_js("button.pay","付款")
        self.find_element(*self.pos_last_pay_loc).click()

if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    # from Business.odoo12_login_page_business import odoo12_LoginPage_Business
    # lp12 = odoo12_LoginPage_Business(driver)
    # lp12.access_Login_page()
