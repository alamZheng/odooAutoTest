#!/usr/bin/python
# -*- coding:utf-8 -*-
import unittest
from selenium import webdriver
import sys
sys.path.append("..")
from PO.login_page import LoginPage
from PO.index_page import IndexPage
import time

class TestHeader(unittest.TestCase):

    imgs=[]

    """UI自动化登录"""
    ip =""
    def setUp(self):
        # print("setup")
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.PhantomJS()
        sp = LoginPage(self.driver)
        sp.login("dade.zhan@aqara.com","123456")
        # ip = IndexPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    # def add_img(self):
    #     self.imgs.append(self.driver.get_screenshot_as_base64())
    #     return True

    
    def test_01_Header(self):
        """测试header icon"""
        # print("111")
        ip = IndexPage(self.driver)
        ip.clickHead()
        ip.add_img(self.imgs)
        # self.add_img()

    def test_02_Workflow(self):
        """测试审批流 icon"""
        # print("111")
        ip = IndexPage(self.driver)
        ip.clickWorkflow()
        ip.add_img(self.imgs)
        # self.add_img()

    def test_03_Msg(self):
        """测试消息icon"""
        # print("111")
        ip = IndexPage(self.driver)
        ip.clickMsg()
        ip.add_img(self.imgs)
        # self.add_img()

    def test_04_Inbox(self):
        """测试收件箱icon"""
        # print("111")
        ip = IndexPage(self.driver)
        ip.clickInbox()
        ip.add_img(self.imgs)
        # self.add_img()


if __name__ == '__main__':
    unittest.main()