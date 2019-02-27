#!/usr/bin/python
# -*- coding:utf-8 -*-
import unittest
from selenium import webdriver
import sys
sys.path.append("..")
from PO.login_page import LoginPage
from PO.approval_page import ApprovalPage

class TestApproval(unittest.TestCase):

    imgs=[]

    def setUp(self):
        # print("setup")
        self.driver = webdriver.Chrome()

    def tearDown(self):
        # pass
        self.driver.quit()

    @unittest.skip("had tested")
    def test_01_access_approval(self,username='qingbin.tao@aqara.com'):
        sp = LoginPage(self.driver)
        sp.login(username, "123456")
        ap = ApprovalPage(self.driver)
        ap.access_approvalPage()
        ap.add_img(self.imgs)

    @unittest.skip("had tested")
    def test_02_access_approval_01st_detail(self,username='qingbin.tao@aqara.com'):
        sp = LoginPage(self.driver)
        sp.login(username, "123456")
        ap = ApprovalPage(self.driver)
        ap.access_approval_1st_detail()
        ap.add_img(self.imgs)

if __name__ == '__main__':
    unittest.main()