#!/usr/bin/python
#!/usr/bin/python
# -*- coding:utf-8 -*-
from Business.odoo12_saleOrder_page_business import odoo12_SaleOrder_Page_business
from Business.odoo12_login_page_business import odoo12_LoginPage_Business
from parameterized import parameterized
import unittest
from selenium import webdriver
import sys
sys.path.append("..")
# python2需要这三行，python3不需要
reload(sys)
sys.setdefaultencoding('utf8')


class Test_odoo12_saleOrder_page(unittest.TestCase):
    imgs = []
    """UI自动化登录"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        sp = odoo12_LoginPage_Business(self.driver)
        sp.login()

    def tearDown(self):
        # pass
        self.driver.quit()

    # @unittest.skip("had tested")
    def test_01_access_saleOrder(self):
        """测试进入销售menu"""
        sop = odoo12_SaleOrder_Page_business(self.driver)
        sop.access_odoo12_SaleOrder_Page()
        # print(sop.get_menu_title())
        # self.assertEqual(sop.get_menu_title(), "电商", msg="验证失败！")
        sop.add_img(self.imgs)

    @unittest.skip("had tested")
    def test_02_new_Quotation_saleOrder(self):
        """测试新建报价单"""
        sop = odoo12_SaleOrder_Page_business(self.driver)
        sop.new_order_Quotation()
        # print(sop.get_menu_title())
        # self.assertEqual(sop.get_menu_title(), "电商", msg="验证失败！")
        sop.add_img(self.imgs)

    @parameterized.expand([
        ('1'),
        ('0'),
    ])
    # @unittest.skip("had tested")
    def test_03_new_partner_saleOrder(self,pOrC):
        """测试新建客户"""
        sop = odoo12_SaleOrder_Page_business(self.driver)
        sop.new_order_partner(pOrC=1)
        sop.add_img(self.imgs)


if __name__ == '__main__':
    unittest.main()
