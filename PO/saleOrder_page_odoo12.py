#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
from PO import base_page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import SendKeys

import sys
sys.path.append("..")


class SaleOrderPage(base_page.BasePage):
    __SaleOrderPage_url = "http://192.168.100.26:8899/web#action=455&model=sale.order&view_type=list&menu_id=304"

    def access_sale_order(self):
        print(sys._getframe().f_code.co_name)
        self.open(self.__SaleOrderPage_url)
        time.sleep(2)

    def access_menu_order(self):
        print(sys._getframe().f_code.co_name)
        self.__click_menu_order_list()
        time.sleep(2)

    def access_menu_stock_picking(self):
        print(sys._getframe().f_code.co_name)
        self.__click_menu_order_stock_picking()
        time.sleep(2)

    def access_menu_partner(self):
        print(sys._getframe().f_code.co_name)
        self.__click_menu_partner()
        time.sleep(2)

    def access_menu_einvoice(self):
        print(sys._getframe().f_code.co_name)
        self.__click_menu_einvoice()
        time.sleep(2)

    def access_menu_platform_backend(self):
        print(sys._getframe().f_code.co_name)
        self.__click_menu_platform_backend()
        time.sleep(2)

    __menu_title_loc = (By.XPATH, "/html/body/header/nav/a")

    def get_menu_title(self):
        print(sys._getframe().f_code.co_name)
        return self.find_element(*self.__menu_title_loc).text

    __menu2_title_loc = (By.XPATH, "//ol/li")

    def get_menu2_title(self):
        print(sys._getframe().f_code.co_name)
        return self.find_element(*self.__menu2_title_loc).text

    __menu_import_order_loc = (By.XPATH, "//li[5]/a/span")
    __url_import_menu_order = "http://192.168.100.26:8899/web#menu_id=310&action=452"

    def __click_menu_import_order(self):
        print(sys._getframe().f_code.co_name)
        time.sleep(2)
        # self.find_element(*self.__import_menu_order_loc).click()
        self.open(self.__url_import_menu_order)
        time.sleep(2)

    __menu_order_list_loc = (By.LINK_TEXT, u"订单")

    def __click_menu_order_list(self):
        print(sys._getframe().f_code.co_name)
        self.find_element(*self.__menu_order_list_loc).click()
        self.find_element(By.XPATH, "//span").click()
        time.sleep(2)

    __menu_order_stock_picking_loc = (By.LINK_TEXT, u"出库单")

    def __click_menu_order_stock_picking(self):
        print(sys._getframe().f_code.co_name)
        self.find_element(*self.__menu_order_stock_picking_loc).click()
        self.find_element(By.XPATH, "//li[2]/div/a/span").click()
        time.sleep(2)

    __menu_partner_loc = (By.LINK_TEXT, u"客户")

    def __click_menu_partner(self):
        print(sys._getframe().f_code.co_name)
        self.find_element(*self.__menu_partner_loc).click()
        self.find_element(By.XPATH, "//li[3]/div/a/span").click()
        time.sleep(2)

    __menu_einvoice_loc = (By.LINK_TEXT, "电子发票")

    def __click_menu_einvoice(self):
        print(sys._getframe().f_code.co_name)
        self.find_element(*self.__menu_einvoice_loc).click()
        self.find_element(By.XPATH, "//li[4]/div/a/span").click()
        time.sleep(2)

    __menu_platform_backend_loc = (By.LINK_TEXT, "电商设置")

    def __click_menu_platform_backend(self):
        print(sys._getframe().f_code.co_name)
        self.find_element(*self.__menu_platform_backend_loc).click()
        self.find_element(
            By.XPATH,
            "/html/body/header/nav/ul[2]/li[6]/div/a[1]/span").click()
        time.sleep(2)

    __import_order_loc = (By.XPATH, "(//button[@type='button'])[23]")

    def __click_import_order(self):
        print(sys._getframe().f_code.co_name)
        self.find_element(*self.__import_order_loc).click()
        time.sleep(2)

    __ufile_loc = (By.NAME, "ufile")

    def __upload_file(self):
        print(sys._getframe().f_code.co_name)
        SendKeys.SendKeys("D:\\odooAuTest\\testData\\importOrderList.xlsx")  # 发送文件地址
        time.sleep(1)
        SendKeys.SendKeys("{ENTER}")
        time.sleep(1)
        SendKeys.SendKeys("{ENTER}")

    __download_template_file_loc = (
        By.NAME, "template_file_name")

    def __download_template_file(self):
        print(sys._getframe().f_code.co_name)
        self.find_element(*self.__download_template_file_loc).click()
        time.sleep(2)

    __check_upload_loc = (By.NAME, "action_check")

    def __check_upload_file(self):
        print(sys._getframe().f_code.co_name)
        self.find_element(*self.__check_upload_loc).click()
        time.sleep(2)

    def import_order(self):
        self.__click_menu_import_order()
        self.__click_import_order()
        self.__upload_file()
        self.__check_upload_file()

    def download_template_file(self):
        self.__click_menu_import_order()
        self.__download_template_file()
