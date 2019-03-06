#!/usr/bin/python
# -*- coding:utf-8 -*-
from utils.Logger import Log
from Business.login_page_odoo12_business import LoginPageBusiness
import unittest
from selenium import webdriver
import sys
sys.path.append("..")

log = Log()


class Test_login_page_odoo12(unittest.TestCase):

    imgs = []
    """Test_login_page_odoo12登录"""

    # @classmethod
    # def setUpClass(self):
    #     # pass
    #     self.driver = webdriver.Chrome()
    #     self.sp = LoginPageBusiness(self.driver)

    def setUp(self):
        # pass
        self.driver = webdriver.Chrome()
        self.sp = LoginPageBusiness(self.driver)

    def tearDown(self):
        # self.sp.logout()
        self.sp.quit_driver()

    # @classmethod
    # def tearDownClass(self):
    #     self.sp.quit_driver()

    # @unittest.skip("had tested")
    def test_login_01_default(self):
        """登录"""
        log.info(self.__class__.__name__)
        log.info(sys._getframe().f_code.co_name)
        self.sp.login()
        # self.add_img()
        self.sp.add_img(self.imgs)
        # self.assertEqual(sp.get_username(),"hanxiaobei",msg="验证失败！")

    # @unittest.skip("had tested")
    def test_login_02_customer(self):
        """登录自定义的账户和密码"""
        log.info("---test_login_02_customer----")
        self.sp.login("admin", "123456")
        # self.add_img()
        self.sp.add_img(self.imgs)
        # self.assertEqual(sp.get_username(),"hanxiaobei",msg="验证失败！")

    # @unittest.skip("had tested")
    def test_login_03_wrongPWD(self):
        """登录自定义的账户和密码"""
        self.sp.login("andy.yang@aqara.com", "111111")
        # self.add_img()
        self.sp.add_img(self.imgs)
        print(self.sp.get_alert_msg())
        self.assertEqual(self.sp.get_alert_msg(), "错误的登录名/密码", msg="验证失败！")

    # @unittest.skip("had tested")
    def test_login_04_wrongUser(self):
        """登录自定义的账户和密码"""
        self.sp.login("test.yang@aqara.com", "123456")
        # self.add_img()
        self.sp.add_img(self.imgs)
        # print(sp.get_alert_msg())
        self.assertEqual(self.sp.get_alert_msg(), "错误的登录名/密码", msg="验证失败！")

    # @unittest.skip("had tested")
    def test_login_05_logout(self):
        """测试登出"""
        self.sp.login("test.yang@aqara.com", "123456")
        self.sp.login()
        self.sp.logout()
        # self.add_img()
        self.sp.add_img(self.imgs)

if __name__ == '__main__':
    unittest.main()
