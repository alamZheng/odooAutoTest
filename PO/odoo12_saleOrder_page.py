#!/usr/bin/python
# -*- coding:utf-8 -*-
import time


from selenium.webdriver.common.by import By

from utils.Util_configparser import ConfigUtils

from PO import base_page

import sys
sys.path.append("..")
reload(sys)
sys.setdefaultencoding('utf8')


class odoo12_SaleOrder_Page(base_page.BasePage):
    # url_SaleOrder = 'http://192.168.100.26:8899/web#action=455&model=sale.order&view_type=list&menu_id=304'
    # url_SaleOrder =ConfigUtils("testdata").get_values_by_key("odoo12",'url_odoo12_host')
    # url_SaleOrder = url_SaleOrder+ConfigUtils("testdata").get_values_by_key("odoo12",'url_SaleOrder')
    url_SaleOrder = '''%s%s''' % \
        (ConfigUtils("testdata").get_values_by_key("odoo10", 'url_odoo10_host'), \
         ConfigUtils("testdata").get_values_by_key("odoo10", 'url_SaleOrder'))
    # print(url_SaleOrder)
    # print(type(url_SaleOrder))
    '''根据element.ini动态生成每个元素和定位值
        name_loc = id,login'''
    names = locals()
    keys = ConfigUtils("PO").get_keys_by_section('odoo10_SaleOrder_page')
    for key in keys:
        # print(key)
        names[key] = ConfigUtils("PO").get_values_by_key('odoo12_SaleOrder_page', key)


    url_SaleOrder ='http://192.168.100.26:8069/web?#min=1&limit=80&view_type=list&model=sale.order&menu_id=365&action=519'
    def access_saleOrder(self):
        self.open(self.url_SaleOrder)

    def access_saleOrder_Quotation(self):
        time.sleep(2)
        self.find_element(*self.menu_order_loc).click()
        self.find_element(*self.menu_order_quotation_loc).click()
        self.find_element(*self.quotation_create_loc).click()

    def access_saleOrder_new_Quotation_url(self, customerName="熙溪智能alam"):
        '''创建报价单'''
        self.open(self.url_SaleOrder_new_quotation)
        self.find_element(*self.quotation_customer_loc).send_keys(u"熙溪智能alam")
        self.send_enter(*self.quotation_customer_loc)
        # self.quotation_add_detail_loc = ('link text', u"添加明细行")
        self.find_element(*self.quotation_add_detail_loc).click()
        # self.quotation_add_detail_product_loc = ('xpath', u"//main/div/div/div/table/tbody/tr/td[2]/div/div/input")
        self.find_element(*self.quotation_add_detail_product_loc).click()
        self.find_element(*self.quotation_add_detail_product_loc).send_keys(u"2020066")
        self.send_enter(*self.quotation_add_detail_product_loc)
        # self.quotation_add_detail_comment_loc = ('xpath', "//main/div/div/textarea")
        self.find_element(*self.quotation_add_detail_comment_loc).send_keys(u"test")
        # self.quotation_add_detail_save_loc = ('css selector', "footer.modal-footer > button.btn.btn-primary")
        self.find_element(*self.quotation_add_detail_save_loc).click()
        # self.quotation_save_loc = ('css selector', "button.btn.btn-primary.o_form_button_save")
        self.find_element(*self.quotation_save_loc).click()
        # self.quotation_add_detail_save_loc = ('css selector', "button.btn.btn-primary.o_list_button_add")
        # self.find_element(*self.quotation_add_detail_save_loc).click()

    def access_saleOrder_new_partner_url(self, partnerName="alam_partner_190306", pOrC=0):
        '''创建客户
        p_c:0 表示创建个人客户
        p_c:1 表示创建公司客户'''
        self.open(self.url_SaleOrder_new_partner)
        # self.partner_person_loc = ('xpath', "//div[2]/div[2]/label")
        # self.partner_company_loc = ('xpath', "//div[2]/div/label")
        if pOrC == 0:
            self.find_element(*self.partner_person_loc).click()
        elif pOrC == 1:
            self.find_element(*self.partner_company_loc).click()
        else:
            print("pOrC must 0 or 1")
        # self.partner_name_loc = ('xpath', "//h1/div/input")
        self.find_element(*self.partner_name_loc).send_keys(partnerName)
        # self.partner_save_loc = ('xpath', "//div[2]/button")
        # self.partner_save_loc = ('css selector', "button.btn.btn-primary.o_form_button_save")
        self.find_element(*self.partner_save_loc).click()

    def access_saleOrder_new_product_url(self, productName="alam_product_190306"):
        '''创建客户
        p_c:0 表示创建个人客户
        p_c:1 表示创建公司客户'''
        self.open(self.url_SaleOrder_new_partner)
        # self.partner_person_loc = ('xpath', "//div[2]/div[2]/label")
        # self.partner_company_loc = ('xpath', "//div[2]/div/label")
        # self.partner_name_loc = ('xpath', "//h1/div/input")
        self.find_element(*self.partner_name_loc).send_keys(productName)
        # self.partner_save_loc = ('xpath', "//div[2]/button")
        # self.partner_save_loc = ('css selector', "button.btn.btn-primary.o_form_button_save")
        self.find_element(*self.partner_save_loc).click()

if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    import sys
    sys.path.append("..")
    from Business.odoo12_login_page_business import odoo12_LoginPageBusiness
    lp = odoo12_LoginPageBusiness(driver)
    lp.login()
    sop = odoo12_SaleOrder_Page(driver)
    # sop.access_saleOrder()
    # sop.access_saleOrder_Quotation()
    # sop.access_saleOrder_new_Quotation_url()
    sop.access_saleOrder_new_partner_url()
