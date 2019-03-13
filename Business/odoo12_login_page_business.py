# !/usr/bin/python
# -*- coding:utf-8 -*-
import time
from PO.odoo12_login_page import odoo12_Login_page
from selenium import webdriver
import sys
sys.path.append("..")
reload(sys)
sys.setdefaultencoding('utf8')


class odoo12_LoginPage_Business(odoo12_Login_page):

    def login(self, name_value="zszx.alam@qq.com", pwd_value="111111"):
        self.access_Login_page()
        self.enter_username(name_value)
        self.enter_password(pwd_value)
        # time.sleep(2)  # 手动输入验证码
        self.click_login()
        self.wait(2)  # 等待2秒，登录后的页面加载完成

    def logout(self):
        self.click_logout()


if __name__ == '__main__':
    driver = webdriver.Chrome()
    sp = odoo12_LoginPage_Business(driver)
    sp.login()
    sp.logout()
