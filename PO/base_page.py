#!/usr/bin/python
# -*- coding:utf-8 -*-
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


class BasePage(object):
    # 初始化
    def __init__(self, se_driver):
        self.driver = se_driver

    # 定义open方法
    def open(self, url, page_title=None):
        time.sleep(1)
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.get(url)
        time.sleep(1)
        if page_title is not None:
            assert page_title in self.driver.title

    # 重写元素定位的方法
    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except AttributeError:
            print(u"%s 页面中未能找到 %s 元素" % (self, loc))

    # 重写元素定位的方法
    def find_elements(self, *loc):
        try:
            # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            time.sleep(1)
            return self.driver.find_elements(*loc)
        except AttributeError:
            print(u"%s 页面中未能找到 %s 元素" % (self, loc))

    # 定义script方法，用于执行js脚本

    def script(self, src):
        self.driver.execute_script(src)

    # 定义script方法，用于执行js脚本
    def _click_element_text_by_js(self, element, text):
        '''js = '$("'+element+':contains('+text+'):visible").click()'
        '''
        time.sleep(2)
        js = '$("' + element + ':contains(' + text + '):visible").click()'
        self.script(js)
        time.sleep(2)

    def click_className_by_js(self, className):
        '''js = '$("'+element+':contains('+text+'):visible").click()'
        '''
        time.sleep(2)
        js = '$(".' + className + ':visible").click()'
        self.script(js)
        time.sleep(2)

    def click_element_className_by_js(self, element, className):
        '''js = '$("'+element+':contains('+text+'):visible").click()'
        '''
        time.sleep(2)
        js = '$("' + element + '.' + className + ':visible").click()'
        self.script(js)
        time.sleep(2)

    def click_className_text_by_js(self, className, text):
        '''js = '$("'+element+':contains('+text+'):visible").click()'
        '''
        time.sleep(2)
        # js = '$(".'+className+':visible").click()'
        js = '$(\'.' + className + ':contains(' + text + ')\').click()'

        self.script(js)
        time.sleep(2)

    # 定义script方法，用于执行js脚本
    def click_button_text_by_js(self, text):
        '''js = '$("'+element+':contains('+text+'):visible").click()'
        '''
        self._click_element_text_by_js("button", text)

    # 定义script方法，用于执行js脚本
    def click_p_text_by_js(self, text):
        '''js = '$("'+element+':contains('+text+'):visible").click()'
        '''
        self._click_element_text_by_js("p", text)

    # 定义script方法，用于执行js脚本
    def click_a_text_by_js(self, text):
        '''js = '$("'+element+':contains('+text+'):visible").click()'
        '''
        self._click_element_text_by_js("a", text)

    def send_id_value_by_js(self, id, text):
        time.sleep(2)
        js = '$("#' + id + '").val(' + text + ')'
        self.script(js)
        time.sleep(2)

    def click_button_byText(self, text):
        try:
            # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            time.sleep(2)
            # return self.driver.find_elements(*loc)
            button_loc = 'tag name', 'button'
            elements = self.find_elements(*button_loc)
            # print(type(submits))
            for i in elements:
                # print(type(i))
                # print(i.get_attribute("textContent"))
                if i.get_attribute("textContent").find(text) >= 0:
                    i.click()
                    break
        except AttributeError:
            print(u"%s 页面中未能找到 %s 元素" % (self, text))

    # 重写send_keys方法
    def send_keys(self, value, clear_first=True, click_first=True, *loc):
        try:
            if click_first:
                self.find_element().click()
            if clear_first:
                self.find_element().clear()
                self.find_element().send_keys(value)

        except AttributeError:
            print(u'找不到元素:' + str(loc))

    def send_enter(self, *loc):
        try:
            time.sleep(2)
            # self.wait(1)
            from selenium.webdriver.common.keys import Keys
            self.find_element(*loc).send_keys(Keys.ENTER)
        except AttributeError:
            print(u'找不到元素:' + str(loc))

    # def take_screenshot(self):
    #     timeString =str(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()))
    #     pic_path = '.\\report\\report' + timeString +'screenshow.png'
    #     self.driver.save_screenshot(pic_path)

    def add_img(self, imgs):
        time.sleep(1)
        imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def quit_driver(self):
        self.driver.quit()

    def wait(self, time=2):
        self.driver.implicitly_wait(time)

    def wait_until_url_find(self, findStr):
        i = 0
        while i < 5:
            if (str(self.driver.current_url).find(findStr) < 0):
                continue
            i = i + 1
            time.sleep(1)

    # def select_dropdown(self, optionName, *loc):
    #     try:
    #         Select(self.find_element(*loc)).select_by_visible_text(optionName)
    #     except AttributeError:
    #         print("select_dropdown未找到%s" % (self, loc))
