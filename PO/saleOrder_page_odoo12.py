from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import sys
sys.path.append("..")
from PO import base_page
from utils.configparserUtil import ConfigUtils
import time

class SaleOrderPage(base_page.BasePage):
    SaleOrderPage_url = "http://192.168.100.26:8899/web#action=455&model=sale.order&view_type=list&menu_id=304"
    menu_title_loc = (By.XPATH,"/html/body/header/nav/a")

    def accessSaleOrder(self):
        print(sys._getframe().f_code.co_name)
        self.open(self.SaleOrderPage_url)
        time.sleep(2)

    # def login(self,name_value="admin",pwd_value="123456"):
    #     self.open(self.LoginPage_url)
    #     self.find_element(*self.name_loc).send_keys(name_value)
    #     self.find_element(*self.password_loc).send_keys(pwd_value)
    #     time.sleep(2)          #手动输入验证码
    #     self.find_element(*self.submit_loc).click()
    #     time.sleep(5)          #等待5秒，登录后的页面加载完成

    def get_menu_title(self):
        return self.find_element(*self.menu_title_loc).text
    #
    # def reset(self):
    #     self.open(self.LoginPage_url)
    #     self.find_element(*self.reset_loc).click()
    #
    # def register(self):
    #     self.open(self.LoginPage_url)
    #     self.find_element(*self.register_loc).click()


    # def get_username(self):
    #     return self.find_element(*self.username_top).text