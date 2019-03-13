#!/usr/bin/python
# -*- coding:utf-8 -*-

from utils.Util_configparser import ConfigUtils
from PO import base_page

import sys
sys.path.append("..")


class odoo12_Login_page(base_page.BasePage):
    login_url = 'http://192.168.100.26:8899/web/login'

    '''根据element.ini动态生成每个元素和定位值
    name_loc = id,login'''
    names = locals()
    keys = ConfigUtils("PO").get_keys_by_section('odoo12_Login_page')
    for key in keys:
        # print(key)
        names[key] = ConfigUtils("PO").get_values_by_key('odoo12_Login_page', key)

    def access_Login_page(self):
        self.open(str(self.login_url))

    def enter_username(self, name_value):
        self.find_element(*self.name_loc).send_keys(name_value)

    def enter_password(self, pwd_value):
        self.find_element(*self.password_loc).send_keys(pwd_value)

    def click_login(self):
        self.find_element(*self.submit_loc).click()

    def click_logout(self):
        self.find_element(*self.user_icon_loc).click()
        self.find_element(*self.logout_loc).click()

    def get_alert_msg(self):
        print(sys._getframe().f_code.co_name)
        return self.find_element(*self.alert_loc).text

    def test(self):
        print(sys._getframe().f_code.co_name)


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    lp12 = odoo12_Login_page(driver)
    lp12.access_Login_page()
