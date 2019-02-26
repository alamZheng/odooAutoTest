from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import sys
sys.path.append("..")
from PO import base_page
from utils.Util_configparser import ConfigUtils
import time

class LoginPage(base_page.BasePage):
    # name_loc = cu.get_values_by_key('LoginPage',"name_loc")
    # print(type(name_loc))
    # print(name_loc)
    # name_loc = tuple(cu.get_values_by_key('LoginPage',"name_loc").split(","))
    # print(type(name_loc))
    # print(name_loc)
    name_loc = (By.ID,"login")
    password_loc = (By.ID,"password")
    submit_loc = (By.XPATH,"/html/body/div/div/form/div[3]/button")
    LoginPage_url = "http://192.168.100.26:8069/web/login"
    alert_loc = (By.XPATH,'/html/body/div/div/form/p')
    reset_loc = (By.LINK_TEXT, '重置密码')
    register_loc = (By.LINK_TEXT, '注册')



    # def click_link(self):
    #     self.find_element(*self.link_loc).click()
    #     time.sleep(3)           #等待3秒，等待登录弹窗加载完成

    def login(self,name_value="dade.zhan@aqara.com",pwd_value="123456"):
        self.open(self.LoginPage_url)
        self.find_element(*self.name_loc).send_keys(name_value)
        self.find_element(*self.password_loc).send_keys(pwd_value)
        time.sleep(2)          #手动输入验证码
        self.find_element(*self.submit_loc).click()   
        time.sleep(5)          #等待5秒，登录后的页面加载完成

    def get_alert_msg(self):
        return self.find_element(*self.alert_loc).text

    def reset(self):
        self.open(self.LoginPage_url)
        self.find_element(*self.reset_loc).click()

    def register(self):
        self.open(self.LoginPage_url)
        self.find_element(*self.register_loc).click()


    # def get_username(self):
    #     return self.find_element(*self.username_top).text