# !/usr/bin/python
# -*- coding:utf-8 -*-
import time
from Business.odoo10_login_page_business import odoo10_Login_Page_Business
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
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    @unittest.skip("had tested")
    def test_01_login_default(self):
        """登录"""
        sp = odoo10_Login_Page_Business(self.driver)

        # sp.open(self.url)
        sp.login()
        # self.add_img()
        sp.add_img(self.imgs)
        # self.assertEqual(sp.get_username(),"hanxiaobei",msg="验证失败！")

    # @unittest.skip("had tested")
    def test_02_login_customer(self):
        """登录自定义的账户和密码"""
        # print("111")
        sp = odoo10_Login_Page_Business(self.driver)

        # sp.open(self.url)
        sp.login("andy.yang@aqara.com", "123456")
        # self.add_img()
        sp.add_img(self.imgs)
        # self.assertEqual(sp.get_username(),"hanxiaobei",msg="验证失败！")


if __name__ == '__main__':
    unittest.main()
