#!/usr/bin/python
# -*- coding:utf-8 -*-
import unittest
import HTMLTestRunner_cn as HTMLTestRunner
# import HTMLTestRunner_cn_alam as HTMLTestRunner
import time

# 相对路径
testcase_path = "..\\testcase"
# timeString =str(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()))
timeString = str(time.strftime("%Y-%m-%d", time.localtime()))
report_path = "..\\report\\report" + timeString + ".html"


def creat_suite():
    uit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(testcase_path, pattern="test_5*.py")
    for test_suite in discover:
        # print(test_suite)
        for test_case in test_suite:
            uit.addTest(test_case)
    return uit


if __name__ == '__main__':
    suite = creat_suite()
    fp = open(report_path, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="测试结果", description="测试搜索结果")
    runner.run(suite)
    fp.close()
