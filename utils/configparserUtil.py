# coding:utf-8

from configparser import ConfigParser
import sys

sys.path.append("..")

class ConfigUtils(object):
    fileName = ""

    def __init__(self, fileName="po"):
        super(ConfigUtils, self).__init__()
        try:
            self.config = ConfigParser()
            if fileName == "po" or fileName == "PO":
                self.fileName = "..\\PO\\element.ini"
            if fileName == "testdata":
                self.fileName = "..\\testcase\\testdata.ini"
            self.config.read(self.fileName)
        except IOError:
            print("Error: 没有找到文件或读取文件失败")

    def get_sections(self):
        return self.config.sections()

    def get_values_by_key(self, section, key):
        return self.config.get(section, key)

    def set_section_key_value(self, section, key, value):
        self.config.set(section, key, value)
        with open(self.fileName, "w+") as f:
            self.config.write(f)


if __name__ == '__main__':
    # print(ConfigUtils("PO").get_values_by_key('LoginPage',"name_loc"))
    # print(ConfigUtils("po").get_values_by_key('LoginPage', "name_loc"))
    # print(ConfigUtils("testdata").get_values_by_key('PLMPage', "ecn_number"))
    ConfigUtils("testdata").set_section_key_value('PLMPage', "ecn_number", "123123")
    print(ConfigUtils("testdata").get_values_by_key('PLMPage', "ecn_number"))
