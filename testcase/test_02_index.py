#!/usr/bin/python
# -*- coding:utf-8 -*-
import unittest
from selenium import webdriver
import sys
sys.path.append("..")
from PO.login_page import LoginPage
from PO.index_page import IndexPage
import time

class TestIndex(unittest.TestCase):

    imgs=[]

    """测试index和header页面"""
    def setUp(self):
        # print("setup")
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.PhantomJS()
        sp = LoginPage(self.driver)
        sp.login()

    def tearDown(self):
        pass
        # self.driver.quit()

    # def add_img(self):
    #     self.imgs.append(self.driver.get_screenshot_as_base64())
    #     return True

    @unittest.skip("had tested")
    def test_01_Index(self):
        """测试index页面"""
        # print("111")
        ip = IndexPage(self.driver)
        ip.click_Index()
        # self.add_img()
        ip.add_img(self.imgs)

    # @unittest.skip("had tested")
    def test_02_Approval(self):
        """测试index页面"""
        # print("111")
        ip = IndexPage(self.driver)
        # ip.click_Index()
        ip.open('http://192.168.100.26:8069/web?#min=1&limit=80&view_type=list&model=lumi.workflow.task&menu_id=867&action=976')
        # self.add_img()
        ip.add_img(self.imgs)


if __name__ == '__main__':
    unittest.main()