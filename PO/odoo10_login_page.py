#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
from utils.Util_configparser import ConfigUtils
from PO import base_page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import sys
sys.path.append("..")


class odoo10_Login_Page(base_page.BasePage):
    # name_loc = (By.ID, "login")
    # password_loc = (By.ID, "password")
    # submit_loc = (By.XPATH, "/html/body/div/div/form/div[3]/button")
    # LoginPage_url = "http://192.168.100.26:8069/web/login"
    # alert_loc = (By.XPATH, '/html/body/div/div/form/p')
    # reset_loc = (By.LINK_TEXT, '重置密码')
    # register_loc = (By.LINK_TEXT, '注册')

    names = locals()
    keys = ConfigUtils("PO").get_keys_by_section('odoo10_Login_Page')
    for key in keys:
        # print(key)
        names[key] = ConfigUtils("PO").get_values_by_key('odoo10_Login_Page', key)

    url_login = ConfigUtils("testdata").get_values_by_key('odoo10', 'url_login')

    def access_login_page(self):
        self.open(self.url_login)

    def type_username(self, name_value):
        self.find_element(*self.name_loc).send_keys(name_value)

    def type_pwd(self, pwd_value):
        self.find_element(*self.password_loc).send_keys(pwd_value)

    def click_login(self):
        self.click_button_text_by_js("登录")

    def get_alert_msg(self):
        return self.find_element(*self.alert_loc).text

    def reset(self):
        self.open(self.url_login)
        self.find_element(*self.reset_loc).click()

    def register(self):
        self.open(self.url_login)
        self.find_element(*self.register_loc).click()

    def logout(self):
        self.find_element(*self.user_icon_loc).click()
        self.find_element(*self.logout_loc).click()
    # def get_username(self):
    #     return self.find_element(*self.username_top).text


if __name__ == '__main__':
    from selenium import webdriver
    driver=webdriver.Chrome()
    import sys
    sys.path.append("..")
    lp=odoo10_Login_Page(driver)
    lp.access_login_page()
    # lp.click_login()
