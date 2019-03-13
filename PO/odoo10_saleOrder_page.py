#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
from utils.Util_configparser import ConfigUtils
from PO import base_page

import sys
sys.path.append("..")


class odoo10_SaleOrder_Page(base_page.BasePage):
    '''根据element.ini动态生成每个元素和定位值
            name_loc = id,login'''
    names = locals()
    keys = ConfigUtils("PO").get_keys_by_section('odoo10_SaleOrder_Page')
    for key in keys:
        # print(key)
        names[key] = ConfigUtils("PO").get_values_by_key('odoo10_SaleOrder_Page', key)

    def access_saleOrder(self):
        self.click_className_by_js("fa.fa-th-large")
        self.click_a_text_by_js("销售")
        self.click_a_text_by_js("销售")
        self.click_a_text_by_js("全部销售")


    new_SaleOrder_partner_loc = 'xpath', "//td[2]/div/div/input"
    new_SaleOrder_pay_loc = 'xpath', "//tr[6]/td[2]/div/div/input"
    new_SaleOrder_new_project_new_product_loc = 'xpath', "//div[2]/div/div/div/input"
    new_SaleOrder_NO_loc = 'xpath', "//h1/span"

    def click_save_SaleOrder_button(self):
        self.click_button_text_by_js('保存')
        self.click_button_text_by_js('提交审批')

    def click_new_project_a(self):
        self.click_a_text_by_js("添加项目")

    def click_new_SaleOrder(self):
        self.click_button_text_by_js("创建")
        self.find_element(*self.new_SaleOrder_partner_loc).click()
        self.find_element(*self.new_SaleOrder_partner_loc).send_keys(u"中山市正鑫投资有限公司")
        self.send_enter(*self.new_SaleOrder_partner_loc)
        self.find_element(*self.new_SaleOrder_pay_loc).send_keys(u"月结30天")
        self.send_enter(*self.new_SaleOrder_pay_loc)
        self.click_new_project_a()
        self.find_element(*self.new_SaleOrder_new_project_new_product_loc).send_keys(u"2030140")
        self.send_enter(*self.new_SaleOrder_new_project_new_product_loc)
        self.click_save_SaleOrder_button()
        self.save_new_SaleOrder_NO()

    def save_new_SaleOrder_NO(self):
        # while (self.find_element(*self.new_SaleOrder_NO_loc).text == '新建'):
        while (str(self.driver.current_url).find('#id=') < 0):
            time.sleep(1)
            # url_new_saleOrder_approval = self.driver.current_url
        ConfigUtils("testdata").set_section_key_value('odoo10', "url_new_saleOrder_approval", self.driver.current_url)

    def save_new_pickingout_NO(self):
        while (str(self.driver.current_url).find('stock.picking') < 0):
            time.sleep(1)
            # url_new_saleOrder_approval = self.driver.current_url
        ConfigUtils("testdata").set_section_key_value('odoo10', "url_new_pickingout", self.driver.current_url)

    def click_Approval(self, url):
        self.open(url)
        time.sleep(2)
        self.click_button_text_by_js("审批")
        time.sleep(1)
        self.click_button_text_by_js("确认")

    # 出库单
    picking_type_loc = ('xpath', '//tr[3]/td[2]/div/div/input')

    def click_Picking(self, url):
        '''
        出库全部，拣货类型"LM销售出库",confirn,'预留'

        :return:
        '''
        self.open(url)
        self.click_button_text_by_js("出库全部")
        self.find_element(*self.picking_type_loc).send_keys(u"LM销售出库")
        self.send_enter(*self.picking_type_loc)
        self.click_button_text_by_js("Confirm")

    def click_Pickingout(self, url):
        self.open(url)
        self.click_className_text_by_js("o_stat_text", "交货")
        # self.click_button_text_by_js("交货")
        self.click_button_text_by_js('提交')
        self.save_new_pickingout_NO()

    def click_Pickingout_Approval(self, url):
        self.open(url)
        self.click_button_text_by_js('确认')
        self.click_button_text_by_js('确认')
        self.click_button_text_by_js('标记为待办')
        self.click_button_text_by_js('预留')
        self.click_button_text_by_js('验证')
        self.click_button_text_by_js('应用')


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    import sys
    sys.path.append("..")
    from Business.odoo10_login_page_business import odoo10_Login_Page_Business
    lp = odoo10_Login_Page_Business(driver)
    # lp.login()
    # sop = odoo10_SaleOrder_Page(driver)
    # sop.access_saleOrder()
    # sop.click_new_SaleOrder()

    lp.login("li.li-fin@aqara.com", "123456")
    sop = odoo10_SaleOrder_Page(driver)
    # sop.access_saleOrder()
    #
    import sys
    sys.path.append("..")
    from utils.Util_configparser import ConfigUtils
    #
    url_new_saleOrder_approval = ConfigUtils("testdata").get_values_by_key("odoo10", "url_new_saleOrder_approval")
    sop.click_Approval(url_new_saleOrder_approval)
