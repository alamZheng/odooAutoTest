# !/usr/bin/python
# -*- coding:utf-8 -*-
import time
from PO.odoo12_pos_page import odoo12_pos_page
from selenium import webdriver
import sys
sys.path.append("..")
reload(sys)
sys.setdefaultencoding('utf8')


class odoo12_PosPage_Business(odoo12_pos_page):

    def access_Pos_page(self):
        self.access_Pos()

    def access_Pos_dashboard_page(self):
        self.access_Pos_dashboard()
        self.wait_until_url_find("action=pos")
        self.place_Pos_order()


if __name__ == '__main__':
    driver = webdriver.Chrome()
    # sp = odoo12_LoginPage_Business(driver)
    # sp.login()
    # sp.logout()
