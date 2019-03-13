# !/usr/bin/python
# -*- coding:utf-8 -*-
import time
from PO.odoo10_login_page import odoo10_Login_Page
from selenium import webdriver
import sys
sys.path.append("..")
reload(sys)
sys.setdefaultencoding('utf8')


class odoo10_Login_Page_Business(odoo10_Login_Page):

    def login(self, name_value="shanshan.lian@aqara.com", pwd_value="123456"):
        self.access_login_page()
        self.type_username(name_value)
        self.type_pwd(pwd_value)
        self.click_login()
        time.sleep(1)

    # def logout(self):
    #     self.click_logout()


if __name__ == '__main__':
    driver = webdriver.Chrome()
    lp = odoo10_Login_Page_Business(driver)
    lp.login()
    # sp.logout()
