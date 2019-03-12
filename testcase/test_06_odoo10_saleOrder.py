#!/usr/bin/python
# -*- coding:utf-8 -*-
from utils.Util_configparser import ConfigUtils
from Business.odoo10_saleOrder_page_business import odoo10_SaleOrder_Page_Business
from Business.odoo10_login_page_business import odoo10_Login_Page_Business
from parameterized import parameterized
import unittest
from selenium import webdriver
import sys
sys.path.append("..")
reload(sys)
sys.setdefaultencoding('utf8')


class Test_odoo10_saleOrder_page(unittest.TestCase):
    imgs = []
    """UI自动化登录"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        globals()['lp'] = odoo10_Login_Page_Business(self.driver)
        globals()['url_new_saleorder_approval'] = ConfigUtils("testdata").get_values_by_key("odoo10", "url_new_saleorder_approval")

    def tearDown(self):
        # pass
        self.driver.quit()

    # @unittest.skip("had tested")
    def test_01_new_saleOrder(self):
        globals()['lp'].login("shanshan.lian@aqara.com", "123456")
        sop = odoo10_SaleOrder_Page_Business(self.driver)
        sop.new_saleOrder()

    # @unittest.skip("had tested")
    def test_02_Approval_saleOrder(self):
        globals()['lp'].login("li.li-fin@aqara.com", "123456")
        sop = odoo10_SaleOrder_Page_Business(self.driver)
        sop.Approval_saleOrder(globals()['url_new_saleorder_approval'])

    # @unittest.skip("had tested")
    def test_03_Picking(self):
        globals()['lp'].login("li.li-fin@aqara.com", "123456")
        sop = odoo10_SaleOrder_Page_Business(self.driver)
        sop.Picking(globals()['url_new_saleorder_approval'])

    # @unittest.skip("had tested")
    def test_04_Pickingout(self):
        globals()['lp'].login("li.li-fin@aqara.com", "123456")
        sop = odoo10_SaleOrder_Page_Business(self.driver)
        sop.Pickingout(globals()['url_new_saleorder_approval'])


if __name__ == '__main__':
    unittest.main()
