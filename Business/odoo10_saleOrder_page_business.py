# !/usr/bin/python
# -*- coding:utf-8 -*-
import time
from PO.odoo10_saleOrder_page import odoo10_SaleOrder_Page
from selenium import webdriver
import sys
sys.path.append("..")
reload(sys)
sys.setdefaultencoding('utf8')


class odoo10_SaleOrder_Page_Business(odoo10_SaleOrder_Page):


    def new_saleOrder(self):
        """新建订单"""
        self.access_saleOrder()
        self.click_new_SaleOrder()

    def Approval_saleOrder(self, url):
        """审批订单"""
        self.click_Approval(url)

    def Picking(self, url):
        """创建全部出库单"""
        self.click_Picking(url)

    def Pickingout(self, url):
        """提交全部出库单"""
        self.click_Pickingout(url)

    def Pickingout_Approval(self, url):
        """审批全部出库单"""
        self.click_Pickingout_Approval(url)


if __name__ == '__main__':
    from selenium import webdriver

    driver = webdriver.Chrome()
    import sys

    sys.path.append("..")
    from Business.odoo10_login_page_business import odoo10_Login_Page_Business

    lp = odoo10_Login_Page_Business(driver)
    # lp.login("shanshan.lian@aqara.com","123456")
    #
    # sop =odoo10_SaleOrder_Page_Business(driver)
    # sop.new_saleOrder()
    lp.login("li.li-fin@aqara.com", "123456")
    sop = odoo10_SaleOrder_Page_Business(driver)
    sop.access_saleOrder()

    import sys

    sys.path.append("..")
    from utils.Util_configparser import ConfigUtils

    url_new_SaleOrder_url = ConfigUtils("testdata").get_values_by_key("odoo10", "url_new_saleOrder_Approval_url")
    sop.Approval_saleOrder(url_new_SaleOrder_url)
