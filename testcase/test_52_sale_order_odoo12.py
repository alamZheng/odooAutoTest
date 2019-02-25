import unittest
from selenium import webdriver
import sys
sys.path.append("..")
from PO.saleOrder_page_odoo12 import SaleOrderPage
from PO.login_page_odoo12 import LoginPage
import time

class TestSaleOrder(unittest.TestCase):
    imgs=[]
    """UI自动化登录"""
    def setUp(self):
        # print("setup")
        # self.url = "http://192.168.100.26:8069/web/login"
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.PhantomJS()
        # self.driver.implicitly_wait(5)
        sp = LoginPage(self.driver)
        sp.login()
        # time.sleep(2)

    def tearDown(self):
        self.driver.quit()

    def test_access_sale_order_01_withURL(self):
        """登录"""
        sop = SaleOrderPage(self.driver)
        sop.accessSaleOrder()
        # print(sop.get_menu_title())
        self.assertEqual(sop.get_menu_title(),"电商",msg="验证失败！")
        sop.add_img(self.imgs)

    @unittest.skip("had tested")
    def test_login_02_customer(self):
        pass


if __name__ == '__main__':
    unittest.main()