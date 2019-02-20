from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import sys
sys.path.append("..")
from PO import base_page
import time

class IndexPage(base_page.BasePage):
    index_loc = (By.XPATH,"/html/body/header/nav[2]/div[1]/div[1]/a/i")
    head_icon_loc = (By.XPATH,"/html/body/header/nav[2]/div[2]/ul[1]/li/a/span[1]")
    workflow_icon_loc = (By.XPATH,"/html/body/header/nav[2]/div[2]/ul[2]/li[4]/a")
    msg_icon_loc = (By.XPATH,"/html/body/header/nav[2]/div[2]/ul[2]/li[3]/a/i")
    inbox_icon_loc = (By.XPATH,"/html/body/header/nav[2]/div[2]/ul[2]/li[2]/a/span")
    PLM_loc = (By.XPATH,"//*[@id=\"appDrawerAppPanelBody\"]/ul/li[16]/a/img")
    # approval_loc = (By.PARTIAL_LINK_TEXT,"审批中心")
    approval_loc = (By.LINK_TEXT, "审批")


    def click_Index(self):
        self.find_element(*self.index_loc).click()   
        time.sleep(2)           #等待5秒，页面加载完成

    def click_Head(self):
        self.find_element(*self.head_icon_loc).click()   
        time.sleep(2)           #等待5秒，页面加载完成

    def click_Workflow(self):
        self.find_element(*self.workflow_icon_loc).click()   
        time.sleep(2)           #等待5秒，页面加载完成

    def click_Msg(self):
        self.find_element(*self.msg_icon_loc).click()   
        time.sleep(2)           #等待5秒，页面加载完成

    def click_Inbox(self):
        self.find_element(*self.inbox_icon_loc).click()   
        time.sleep(2)           #等待5秒，页面加载完成

    def click_PLM(self):
        self.find_element(*self.PLM_loc).click()
        time.sleep(2)           #等待5秒，页面加载完成

    def click_approval(self):
        self.find_element(*self.approval_loc).click()
        time.sleep(2)           #等待5秒，页面加载完成