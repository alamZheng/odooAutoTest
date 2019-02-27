# coding:utf-8

from selenium import webdriver
import sys


sys.path.append("..")


class Screen(object):
    u'''这个应该截图功能的装饰器'''

    def __init__(self, driver):
        self.driver = driver

    def __call__(self, f):
        def inner(*args):
            try:
                return f(*args)
            except BaseException:
                pass
                raise
            finally:
                import time
                time.sleep(2)
                nowTime = time.strftime("%Y_%m_%d_%H_%M_%S")
                self.driver.get_screenshot_as_file('.\screenshot\%s.jpg' % nowTime)
        return inner


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    @Screen(driver)
    def search(driver):
        driver.get("https://www.baidu.com")
        driver.find_element_by_id("kw11").send_keys("python")  # 此行运行失败的
        driver.find_element_by_id("su").click()

    search(driver)
