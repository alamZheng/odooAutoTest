#!/usr/bin/python
# -*- coding:utf-8 -*-
from parameterized import parameterized
import time
from PO.login_page_odoo12 import LoginPage
from PO.saleOrder_page_odoo12 import SaleOrderPage
import unittest
from selenium import webdriver
import sys
sys.path.append("..")


class TestSaleOrder(unittest.TestCase):
    imgs = []
    """UI自动化登录"""

    def setUp(self):
        options = webdriver.ChromeOptions()
        prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'D:\\odooAuTest\\testData'}
        options.add_experimental_option('prefs', prefs)
        self.driver = webdriver.Chrome(chrome_options=options)
        # self.driver = webdriver.Chrome()
        # self.driver = webdriver.PhantomJS()
        # self.driver.implicitly_wait(5)
        sp = LoginPage(self.driver)
        sp.login()
        # time.sleep(2)

    def tearDown(self):
        # pass
        self.driver.quit()

    @unittest.skip("had tested")
    def test_01_access_sale_order_withURL(self):
        """登录"""
        sop = SaleOrderPage(self.driver)
        sop.access_sale_order()
        # print(sop.get_menu_title())
        self.assertEqual(sop.get_menu_title(), "电商", msg="验证失败！")
        sop.add_img(self.imgs)

    @parameterized.expand([
        ("access_menu_order", "Sales Orders"),
        ("access_menu_stock_picking", "调拨"),
        ("access_menu_partner", "客户"),
        ("access_menu_einvoice", "Invoice"),
        ("access_menu_platform_backend", "Platform Backend"),

    ])
    @unittest.skip("had tested")
    def test_02_access_menu_(self, method, assertContent):
        """登录"""
        sop = SaleOrderPage(self.driver,)
        sop.access_sale_order()
        eval('sop.' + method + '()')
        self.assertEqual(sop.get_menu2_title(), assertContent, msg="验证失败！")
        sop.add_img(self.imgs)

    @unittest.skip("had tested")
    def test_03_sale_order_download_template_file(self):
        sop = SaleOrderPage(self.driver)
        sop.access_sale_order()
        sop.download_template_file()

    @unittest.skip("had tested")
    def test_04_sale_order_import_order(self):
        sop = SaleOrderPage(self.driver)
        sop.access_sale_order()
        sop.import_order()
        # self.assertEqual(sop.get_menu_title(), "电商", msg="验证失败！")
        sop.add_img(self.imgs)


if __name__ == '__main__':
    unittest.main()
