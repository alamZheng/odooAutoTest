#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
from utils.Util_configparser import ConfigUtils
from PO import base_page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import sys
sys.path.append("..")


class PLMPage(base_page.BasePage):
    _PLM_url = 'http://192.168.100.26:8069/web?#view_type=kanban&model=mrp.eco.type&menu_id=867&action=1117'
    oe_dashboard_loc = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[1]/div[2]/div/div[1]/button")
    eco_new_loc = (By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[1]/div/button")
    product_loc = (By.XPATH, "//*[@id=\"o_field_input_11\"]")
    submitter_loc = (By.XPATH, "//*[@id=\"o_field_input_22\"]")
    change_loc = (By.XPATH, "//*[@id=\"o_field_input_23\"]")
    action_loc = (By.XPATH, "//*[@id=\"o_field_input_26\"]")
    start_loc = (By.XPATH, "(//button[@type='button'])[17]")
    approval_loc = (By.XPATH, "(//button[@type='button'])[24]")
    alert_loc = (By.XPATH, "/html/body/div[7]/div/div/div[2]/div")
    wuliao_list_loc = (By.XPATH, "(//button[@type='button'])[27]")
    edit_wuliao_loc = (By.XPATH, "(//button[@type='button'])[7]")
    add_wuliao_loc = (By.LINK_TEXT, "添加项目")
    add_wuliao_name_loc = (By.XPATH, "(//input[@type='text'])[10]")
    add_wuliao_number1_loc = (By.XPATH, "(//input[@type='text'])[11]")
    add_wuliao_number2_loc = (By.XPATH, "(//input[@type='text'])[12]")
    save_wuliao_loc = (By.XPATH, "(//button[@type='button'])[9]")
    ecnNO_loc = (By.XPATH, "/html/body/div[1]/div/div[1]/ol/li[3]/a")
    edit_eco_loc = (By.XPATH, "(//button[@type='button'])[7]")
    wuliao_method_tap_lco = (By.LINK_TEXT, u"物料处理方式")

    lm_handling_loc = (By.XPATH, "//div[@id='notebook_page_79']/div[2]/div[2]/div[2]/table/tbody/tr/td[3]")
    lm_handling_dropdown_loc = (By.NAME, "lm_handling")
    factory_handling_loc = (By.XPATH, "(//button[@type='button'])[7]")
    factory_handling_dropdown_loc = (By.NAME, "factory_handling")
    shipped_handling_loc = (By.XPATH, "(//button[@type='button'])[7]")
    shipped_handling_dropdown_loc = (By.NAME, "shipped_handling")

    save_ecn_loc = (By.XPATH, "(//button[@type='button'])[9]")
    approval_ecn_loc = (By.XPATH, "(//button[@type='button'])[18]")

    switch_ecn_list_loc = (By.XPATH, "(//button[@type='button'])[19]")

    approval_ecn_01node_loc = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/header/button[2]")

    def click_oe_dashboard(self):
        self.find_element(*self.oe_dashboard_loc).click()
        time.sleep(2)  # 等待5秒，页面加载完成

    def new_eco(self):
        print(sys._getframe().f_code.co_name)

        self.find_element(*self.eco_new_loc).click()
        time.sleep(2)  # 等待5秒，页面加载完成

    def click_action(self):
        print(sys._getframe().f_code.co_name)

        self.find_element(*self.action_loc).click()
        time.sleep(2)  # 等待5秒，页面加载完成

    def click_start(self):
        print(sys._getframe().f_code.co_name)
        self.find_element(*self.start_loc).click()
        time.sleep(2)  # 等待5秒，页面加载完成

    def click_approval(self):
        print(sys._getframe().f_code.co_name)

        self.find_element(*self.approval_loc).click()
        time.sleep(2)  # 等待5秒，页面加载完成

    def type_product(self, product_id='6010444'):
        print(sys._getframe().f_code.co_name)
        self.find_element(*self.product_loc).send_keys(product_id)
        time.sleep(2)
        print('send_ENTER keys')
        self.find_element(*self.product_loc).send_keys(Keys.ENTER)
        time.sleep(2)  # 等待5秒，页面加载完成

    def type_submitter(self, submitter_name='wes'):
        print(sys._getframe().f_code.co_name)
        self.find_element(*self.submitter_loc).send_keys(submitter_name)
        time.sleep(2)
        print('send_ENTER keys')
        self.find_element(*self.submitter_loc).send_keys(Keys.ENTER)
        time.sleep(2)  # 等待5秒，页面加载完成

    def type_change(self, optionIndex=1):
        print('change_index 变更类别')
        Select(self.find_element(*self.change_loc)).select_by_index(optionIndex)
        time.sleep(2)

    def type_action(self, optionIndex=1):
        print('action_index 执行方案	')
        Select(self.find_element(*self.action_loc)).select_by_index(optionIndex)
        time.sleep(2)

    def click_wuliao_list(self):
        print(sys._getframe().f_code.co_name)

        self.find_element(*self.wuliao_list_loc).click()
        time.sleep(2)  # 等待5秒，页面加载完成

    def click_edit_wuliao(self):
        print(sys._getframe().f_code.co_name)
        self.find_element(*self.edit_wuliao_loc).click()
        time.sleep(2)  # 等待5秒，页面加载完成

    def get_alert_msg(self):
        return self.find_element(*self.alert_loc).text

    def click_add_wuliao(self):
        print(sys._getframe().f_code.co_name)

        self.find_element(*self.add_wuliao_loc).click()
        time.sleep(2)  # 等待5秒，页面加载完成

    def click_save_wuliao(self):
        print(sys._getframe().f_code.co_name)

        self.find_element(*self.save_wuliao_loc).click()
        time.sleep(2)  # 等待5秒，页面加载完成

    def type_wuliao_name(self, wuliao_name='10'):
        print(sys._getframe().f_code.co_name)
        self.find_element(*self.add_wuliao_name_loc).send_keys(wuliao_name)
        time.sleep(2)
        print('send_ENTER keys')
        self.find_element(*self.add_wuliao_name_loc).send_keys(Keys.ENTER)
        time.sleep(2)  # 等待5秒，页面加载完成

    def type_wuliao_number1(self, wuliao_number1='2'):
        print(sys._getframe().f_code.co_name)
        self.find_element(*self.add_wuliao_number1_loc).send_keys(wuliao_number1)

    def type_wuliao_number2(self, wuliao_number2='2'):
        print(sys._getframe().f_code.co_name)
        self.find_element(*self.add_wuliao_number2_loc).send_keys(wuliao_number2)
        # time.sleep(2)
        # print('send_ENTER keys')
        # self.find_element(*self.add_wuliao_name_loc).send_keys(Keys.ENTER)
        # time.sleep(2)  # 等待5秒，页面加载完成

    def click_ecnNO(self):
        print(sys._getframe().f_code.co_name)
        self.find_element(*self.ecnNO_loc).click()
        time.sleep(2)  # 等待5秒，页面加载完成

    def click_ecn_edit(self):
        print(sys._getframe().f_code.co_name)
        self.find_element(*self.edit_eco_loc).click()
        time.sleep(2)  # 等待5秒，页面加载完成

    def click_ecn_tap(self):
        print(sys._getframe().f_code.co_name)
        ecn_tap_href = self.find_element(*self.wuliao_method_tap_lco).get_attribute("href")
        ecn_tap_href = ecn_tap_href[-16:]
        print(ecn_tap_href)
        self.lm_handling_loc = "//div[@id='" + ecn_tap_href + "']/div[2]/div[2]/div[2]/table/tbody/tr/td[3]"
        print(self.lm_handling_loc)
        self.find_element(*self.wuliao_method_tap_lco).click()

        time.sleep(5)  # 等待5秒，页面加载完成

    def select_lm_handling(self, optionIndex=3):
        '''
        "normal":可正常使用;"rework":返工后使用;"return":退换货;"scrapped":申请报废;"other":其他
        '''
        print(sys._getframe().f_code.co_name)
        time.sleep(3)
        self.find_element(By.XPATH, self.lm_handling_loc).click()
        self.find_element(By.NAME, "lm_handling").click()
        self.find_element(By.XPATH, "//option[@value='\"return\"']").click()
        time.sleep(2)

    def select_factory_handling(self, optionIndex=3):
        print(sys._getframe().f_code.co_name)
        self.find_element(By.XPATH, "(//option[@value='\"scrapped\"'])[2]").click()
        time.sleep(2)

    def select_shipped_handling(self, optionIndex=3):
        print(sys._getframe().f_code.co_name)
        self.find_element(By.XPATH, "(//option[@value='\"other\"'])[3]").click()
        time.sleep(2)

    def click_ecn_save(self):
        print(sys._getframe().f_code.co_name)
        self.find_element(*self.save_ecn_loc).click()
        time.sleep(2)  # 等待5秒，页面加载完成

    def click_ecn_approval(self):
        print(sys._getframe().f_code.co_name)
        self.find_element(*self.approval_ecn_loc).click()
        time.sleep(2)  # 等待5秒，页面加载完成

    def click_ecn_01node_approval(self):
        print(sys._getframe().f_code.co_name)
        self.find_element(*self.approval_ecn_01node_loc).click()
        time.sleep(2)  # 等待5秒，页面加载完成

    def click_switch_ecn_list(self):
        print(sys._getframe().f_code.co_name)
        self.find_element(*self.switch_ecn_list_loc).click()
        time.sleep(2)  # 等待5秒，页面加载完成

    def create_ecn_without_upadate(self):
        self.new_eco()
        self.type_product()
        self.type_submitter()
        self.type_change()
        self.type_action()
        self.click_start()
        self.click_approval()

    def save_new_ecn_number(self):
        ecn_number = self.find_element(By.XPATH, "//h2/span").text
        print(ecn_number)
        ConfigUtils("testdata").set_section_key_value('PLMPage', "ecn_number", ecn_number)
        ecn_id = int(ecn_number[-4:]) - 2
        ConfigUtils("testdata").set_section_key_value('PLMPage', "ecn_id", str(ecn_id))

    def create_ecn_with_upadate(self):
        self.new_eco()
        self.type_product()
        self.type_submitter()
        self.type_change()
        self.type_action()
        self.click_start()
        self.save_new_ecn_number()
        self.click_wuliao_list()
        self.click_edit_wuliao()
        self.click_add_wuliao()
        self.type_wuliao_name("10")
        self.type_wuliao_number1("2")
        self.type_wuliao_number2("2")
        self.click_save_wuliao()
        self.click_ecnNO()
        self.click_approval()

    _new_msg_loc = '/html/body/div[1]/div/div[2]/div/div/div[6]/div[1]/button[1]'

    def approval_01node(self):
        self.click_edit_wuliao()
        self.find_element(By.XPATH, self._new_msg_loc).send_keys(Keys.DOWN)
        self.click_ecn_tap()
        self.select_lm_handling()
        self.select_factory_handling()
        self.select_shipped_handling()
        self.click_ecn_save()
        self.click_ecn_01node_approval()

    def approval_02345678node(self):
        self.click_ecn_01node_approval()

    def access_PLM_page(self):
        self.open(self._PLM_url)

    _apply_ecn_loc = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/header/button[6]")

    def apply_ecn(self):
        print(sys._getframe().f_code.co_name)
        time.sleep(2)
        self.find_element(*self._apply_ecn_loc).click()
        time.sleep(2)  # 等待5秒，页面加载完成
