#!/user/bin/env python
# -*-coding:utf-8 -*-
import logging
import time
import os
import sys

from utils.Logger import Log

reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append("..")
# 日志保存本地的路径
log_path = "..\\logs"

def alamWrapper(func):
    def wrapper(*args, **kw):
        # print 'call %s():' % func.__name__
        log = Log()
        log.info(func.__name__)
        # log.info(sys._getframe().f_code.co_name)
        return func(*args, **kw)
    return wrapper

if __name__ == '__main__':
    @alamWrapper
    def alam():
        # log = Log()
        # # log.info(self.__class__.__name__)
        # log.info(sys._getframe().f_code.co_name)
        print("alam")

    alam()