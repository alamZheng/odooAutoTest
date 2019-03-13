#!/usr/bin/python
# -*- coding:utf-8 -*-
from utils.Logger import Log
from Business.odoo12_pos_page_business import odoo12_PosPage_Business
from Business.odoo12_login_page_business import odoo12_LoginPage_Business
import unittest
from selenium import webdriver
import sys

from utils.alamWrapper import alamWrapper

sys.path.append("..")

log = Log()


class Test_pos_page_odoo12(unittest.TestCase):

    imgs = []
    """Test_pos_page_odoo12"""

    # @classmethod
    # def setUpClass(self):
    #     # pass
    #     self.driver = webdriver.Chrome()
    #     self.sp = LoginPageBusiness(self.driver)

    def setUp(self):
        # pass
        self.driver = webdriver.Chrome()
        # globals()['lp'] = odoo12_LoginPage_Business(self.driver)
        self.lp = odoo12_LoginPage_Business(self.driver)

    def tearDown(self):
        self.driver.quit()

    # @classmethod
    # def tearDownClass(self):
    #     self.sp.quit_driver()

    @unittest.skip("had tested")
    def test_01_pos_access(self):
        """进入pos页面"""
        # log.info(self.__class__.__name__)
        # log.info(sys._getframe().f_code.co_name)
        # globals()['lp'].login("zszx.pos@qq.com", "123456")
        self.lp.login("zszx.pos@qq.com", "111111")
        op = odoo12_PosPage_Business(self.driver)
        op.access_Pos_page()
        op.add_img(self.imgs)
        # self.assertEqual(sp.get_username(),"hanxiaobei",msg="验证失败！")

    # @unittest.skip("had tested")
    def test_02_menu_pos_dashboard(self):
        """生成pos订单"""
        # log.info(self.__class__.__name__)
        # log.info(sys._getframe().f_code.co_name)
        # globals()['lp'].login("zszx.pos@qq.com", "123456")
        self.lp.login("zszx.pos@qq.com", "111111")
        op = odoo12_PosPage_Business(self.driver)
        op.access_Pos_dashboard_page()
        op.add_img(self.imgs)
        # self.assertEqual(sp.get_username(),"hanxiaobei",msg="验证失败！")



if __name__ == '__main__':
    unittest.main()
