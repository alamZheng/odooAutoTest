#!/usr/bin/env python
# -*- coding: utf-8 -*-
import psycopg2


class DBoperation():

    def __init__(self, host, db, user, pwd, port):
        self.host = host
        self.db = db
        self.user = user
        self.pwd = pwd
        self.port = port
        try:
            self._conn = psycopg2.connect(
                database=self.db,
                user=self.user,
                password=self.pwd,
                host=self.host,
                port=self.port)
            self._cursor = self._conn.cursor()
        except Exception as e:
            print("get error: %s" % e)



    def try_except(self):
        def wrapper(*args, **kwargs):
            try:
                self(*args, **kwargs)
            except Exception as e:
                print("get error: %s" % e)
        return wrapper

    @try_except
    def _connect(self):
        return psycopg2.connect(
            database=self.db,
            user=self.user,
            password=self.pwd,
            host=self.host,
            port=self.port)

    def common(self, sqlCode):
        try:
            self._cursor.execute(sqlCode)
            row = self._cursor.fetchall()
            print(row)
        except Exception as e:
            print(e)
            self._conn.rollback()
            self._cursor.execute(sqlCode)
        self._conn.commit()

    def close(self):
        self._cursor.close()
        self._conn.close()

    def __del__(self):
        print("最后一步，关闭数据库")
        self.close()


if __name__ == '__main__':
    dbo = DBoperation(host="192.168.100.26",
                      db="erp",
                      user="odoo",
                      pwd="odoo",
                      port="54327")
    # sqlCode = ["UPDATE sale_order SET shop_type = 1,order_id=77,state = 'sale' WHERE id = 77;",
    #            "select state,shop_type,order_id from sale_order where id =77;"]

    sqlCode = ["select * from lumi_crm_product_stock_warning;"]
    for sql in sqlCode:
        dbo.common(sql)
