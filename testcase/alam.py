#!/user/bin/env python
# -*-coding:utf-8 -*-
import logging
import sys
reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append("..")


class alamClass():
    def alam(self):
        print(dir(sys._getframe()))
        # log = Log()
        # print(sys._getframe().__class__.__name__)
        print(sys._getframe().f_code.co_name)
        # print "alam"

if __name__ == '__main__':
    a= alamClass()
    a.alam()
