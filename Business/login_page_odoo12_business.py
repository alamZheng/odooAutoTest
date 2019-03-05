# !/usr/bin/python
# -*- coding:utf-8 -*-
import time

from PO import base_page
from PO.login_page_odoo12 import Login_Page_odoo12
import unittest
from selenium import webdriver
import sys
sys.path.append("..")
reload(sys)
sys.setdefaultencoding('utf8')


class LoginPageBusiness(Login_Page_odoo12):
    def login(self, name_value="alam@aqara.com", pwd_value="111111"):
        print(sys._getframe().f_code.co_name)
        Login_Page_odoo12.open()
        Login_Page_odoo12.enter_username(name_value)
        Login_Page_odoo12.enter_password(pwd_value)
        # time.sleep(2)  # 手动输入验证码
        Login_Page_odoo12.click_login()
        time.sleep(2)  # 等待2秒，登录后的页面加载完成

    def logout(self):
        Login_Page_odoo12.click_logout()
