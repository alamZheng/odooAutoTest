#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
from utils.Util_configparser import ConfigUtils
from parameterized import parameterized
# from nose_parameterized import parameterized
from PO.approval_page import ApprovalPage
from PO.PLM_page import PLMPage
from PO.index_page import IndexPage
from PO.login_page import LoginPage
import unittest
from selenium import webdriver
import sys
# python2需要这三行，python3不需要
reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append("..")


class TestPLM(unittest.TestCase):
    imgs = []
    """PLM"""

    @classmethod
    def setUpClass(self):
        # print("setup")
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.PhantomJS()
        globals()['sp'] = LoginPage(self.driver)

    def tearDown(self):
        globals()['sp'].logout()
        # pass
        # self.driver.quit()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    # @unittest.skip("had tested")
    def test_01_oe_dashboard(self):
        """测试PLM 正常进入PLM页面"""
        globals()['sp'].login("qingbin.tao@aqara.com", "123456")
        ip = IndexPage(self.driver)
        ip.click_Index()
        ip.click_PLM()
        pp = PLMPage(self.driver)
        pp.click_oe_dashboard()
        pp.add_img(self.imgs)
        # self.add_img()

    @unittest.skip("had tested")
    def test_02_ecn_new_withoutUpdate(self):
        """测试 新建ecn 不更新BOM提交会提示"""

        globals()['sp'].login("qingbin.tao@aqara.com", "123456")
        pp = PLMPage(self.driver)
        pp.access_PLM_page()
        pp.click_oe_dashboard()
        pp.create_ecn_without_upadate()

        self.assertEqual(pp.get_alert_msg(), "未发现任何变更,请确认内容有修改后再提交", msg="验证失败！")

        pp.add_img(self.imgs)
        # self.add_img()

    @unittest.skip("had tested")
    def test_03_ecn_with_add_wuliao(self):
        """测试 新建ecn with添加物料到BOM"""

        globals()['sp'].login("qingbin.tao@aqara.com", "123456")
        pp = PLMPage(self.driver)
        pp.access_PLM_page()
        pp.click_oe_dashboard()
        pp.create_ecn_with_upadate()
        pp.add_img(self.imgs)

    @unittest.skip("had tested")
    def test_04_ecn_with_add_wuliao_01node(self, node01_name="qingbin.tao@aqara.com"):
        "测试ecn with添加物料到BOM单的第一个节点"

        globals()['sp'].login(node01_name, "123456")
        ecn_id = ConfigUtils("testdata").get_values_by_key('PLMPage', "ecn_id")
        pp = PLMPage(self.driver)
        pp.open("http://192.168.100.26:8069/web#id=" + str(ecn_id) + "&view_type=form&model=mrp.eco&action=1113&active_id=1")
        pp.approval_01node_add()
        pp.add_img(self.imgs)

    @parameterized.expand([
                 ("chun.fu@aqara.com"),
                 ("ying.xiao@aqara.com"),
                 ("meiping.huang@aqara.com"),
                 ("heyang.yan@aqara.com"),
                 ("jialiang.lian@aqara.com"),
                 ("qiping.hu@aqara.com"),
              ])
    @unittest.skip("had tested")
    def test_05_ecn_with_add_wuliao_02345678node_without_coo(self, username):
        "测试ecn with添加物料到BOM单的第2345678个节点"
        globals()['sp'].login(username, "123456")
        # ap = ApprovalPage(self.driver)
        # ap.access_approval_1st_detail()
        ecn_id = ConfigUtils("testdata").get_values_by_key('PLMPage', "ecn_id")
        pp = PLMPage(self.driver)
        pp.open("http://192.168.100.26:8069/web#id=" + str(ecn_id) + "&view_type=form&model=mrp.eco")
        pp.approval_02345678node()
        pp.add_img(self.imgs)

    @unittest.skip("had tested")
    def test_06_ecn_with_add_wuliao_last_node_without_coo(self, lastNode_name="qiping.hu@aqara.com"):
        """测试ecn with添加物料到BOM单的最后应用变更节点"""
        globals()['sp'].login(lastNode_name, "123456")
        ap = ApprovalPage(self.driver)
        ap.access_approval_1st_detail()
        pp = PLMPage(self.driver)
        ecn_number = ConfigUtils("testdata").get_values_by_key('PLMPage', "ecn_number")
        ecn_id = int(ecn_number[-4:]) - 2
        print(ecn_id)
        pp.open("http://192.168.100.26:8069/web#id=" + str(ecn_id) + "&view_type=form&model=mrp.eco")
        pp.apply_ecn()
        pp.add_img(self.imgs)

    @unittest.skip("had tested")
    def test_07_ecn_with_delete_wuliao(self):
        """测试 新建ecn with添加物料到BOM"""

        globals()['sp'].login("qingbin.tao@aqara.com", "123456")
        pp = PLMPage(self.driver)
        pp.access_PLM_page()
        pp.click_oe_dashboard()
        pp.create_ecn_with_delete()
        pp.add_img(self.imgs)

    @unittest.skip("had tested")
    def test_08_ecn_with_delete_wuliao_01node(self, node01_name="qingbin.tao@aqara.com"):
        "测试ecn with添加物料到BOM单的第一个节点"

        globals()['sp'].login(node01_name, "123456")
        ecn_id = ConfigUtils("testdata").get_values_by_key('PLMPage', "ecn_id")
        pp = PLMPage(self.driver)
        pp.open("http://192.168.100.26:8069/web#id=" + str(
            ecn_id) + "&view_type=form&model=mrp.eco&action=1113&active_id=1")
        pp.approval_01node_delete()
        pp.add_img(self.imgs)


if __name__ == '__main__':
    unittest.main()
