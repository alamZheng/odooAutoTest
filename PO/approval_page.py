#!/usr/bin/python
# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select 

import sys
sys.path.append("..")
from PO import base_page
import time

class ApprovalPage(base_page.BasePage):
    first_approval_loc = (By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td[3]/button")
    approvalPage_url="http://192.168.100.26:8069/web?#min=1&limit=80&view_type=list&model=lumi.workflow.task&action=976"

    def click_approval_list_1st(self):
        self.find_element(*self.first_approval_loc).click()
        time.sleep(2)           #等待5秒，页面加载完成

    def access_approvalPage(self):
        self.open(self.approvalPage_url)

    def access_approval_1st_detail(self):
        self.access_approvalPage()
        self.click_approval_list_1st()