# !/usr/bin/python
# -*- coding:utf-8 -*-
import time
from PO.login_page import LoginPage
import unittest
from selenium import webdriver
import sys
sys.path.append("..")
reload(sys)
sys.setdefaultencoding('utf8')

class TestLogin(unittest.TestCase):
    imgs = []
    """UI自动化登录"""

    def setUp(self):
        # print("setup")
        # self.url = "http://192.168.100.26:8069/web/login"
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.PhantomJS()
        # self.driver.implicitly_wait(5)
        # self.verificationErrors = []

    def tearDown(self):
        self.driver.quit()

    def test_login_01_default(self):
        """登录"""
        sp = LoginPage(self.driver)

        # sp.open(self.url)
        sp.login()
        # self.add_img()
        sp.add_img(self.imgs)
        # self.assertEqual(sp.get_username(),"hanxiaobei",msg="验证失败！")

    def test_login_02_customer(self):
        """登录自定义的账户和密码"""
        # print("111")
        sp = LoginPage(self.driver)

        # sp.open(self.url)
        sp.login("andy.yang@aqara.com", "123456")
        # self.add_img()
        sp.add_img(self.imgs)
        # self.assertEqual(sp.get_username(),"hanxiaobei",msg="验证失败！")

    def test_login_03_wrongPWD(self):
        """登录自定义的账户和密码"""
        # print("111")
        sp = LoginPage(self.driver)

        # sp.open(self.url)
        sp.login("andy.yang@aqara.com", "111111")
        # self.add_img()
        sp.add_img(self.imgs)
        print(sp.get_alert_msg())
        self.assertEqual(sp.get_alert_msg(), "错误的登录名/密码", msg="验证失败！")

    def test_login_04_wrongUser(self):
        """登录自定义的账户和密码"""
        # print("111")
        sp = LoginPage(self.driver)

        # sp.open(self.url)
        sp.login("test.yang@aqara.com", "123456")
        # self.add_img()
        sp.add_img(self.imgs)
        # print(sp.get_alert_msg())
        self.assertEqual(sp.get_alert_msg(), "错误的登录名/密码", msg="验证失败！")

    def test_login_05_accessReset(self):
        """登录自定义的账户和密码"""
        # print("111")
        sp = LoginPage(self.driver)

        # sp.open(self.url)
        sp.reset()
        # self.add_img()
        sp.add_img(self.imgs)

    def test_login_06_accessRegister(self):
        """登录自定义的账户和密码"""
        # print("111")
        sp = LoginPage(self.driver)

        # sp.open(self.url)
        sp.register()
        # self.add_img()
        sp.add_img(self.imgs)


if __name__ == '__main__':
    unittest.main()
