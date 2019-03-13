#!/usr/bin/python
# -*- coding:utf-8 -*-
from configparser import ConfigParser
import sys

sys.path.append("..")
reload(sys)
sys.setdefaultencoding('utf8')

class ConfigUtils(object):
    fileName = ""

    def __init__(self,fileName="po"):
        super(ConfigUtils, self).__init__()
        try:
            self.config = ConfigParser()
            if fileName == "po" or fileName == "PO":
                self.fileName = "..\\PO\\element.ini"
            if fileName == "testdata":
                self.fileName = "..\\testcase\\testdata.ini"
            self.config.read(self.fileName,encoding= 'utf-8-sig')
        except IOError:
            print("Error: 没有找到文件或读取文件失败")

    def get_sections(self):
        return self.config.sections()

    def get_keys_by_section(self, section):
        return self.config.options(section)

    def get_values_by_key(self, section, key):
        value = tuple(self.config.get(section, key).split(","))
        if len(value)==1:
            value = value[0]
        return value

    def get_element(self, key):
        classname=self.__class__.__name__
        print(classname)
        # section = self.__class__.__name__
        # print(section)
        # return self.get_values_by_key(section, key)

    def set_section_key_value(self, section, key, value):
        self.config.set(section, key, value)
        with open(self.fileName, "w+") as f:
            self.config.write(f)


if __name__ == '__main__':
    # print(ConfigUtils("PO").get_values_by_key('LoginPage',"name_loc"))
    # print(ConfigUtils("PO").get_sections())
    # print(ConfigUtils("PO").get_keys_by_section('LoginPage'))
    # print(ConfigUtils("PO").get_values_by_key('login_page_odoo12', "name_loc"))
    # print(ConfigUtils("PO").get_values_by_key('login_page_odoo12', "loginpage_url"))
    print(ConfigUtils("PO").get_element("test"))

    # print(ConfigUtils("PO").get_values_by_key('LoginPage'))
    # print(ConfigUtils("po").get_values_by_key('LoginPage', "name_loc"))
