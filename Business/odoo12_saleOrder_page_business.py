#!/usr/bin/python
# -*- coding:utf-8 -*-
from PO.odoo12_saleOrder_page import odoo12_SaleOrder_Page

import sys
sys.path.append("..")


class odoo12_SaleOrder_Page_business(odoo12_SaleOrder_Page):

    def access_odoo12_SaleOrder_Page(self):
        self.access_saleOrder()

    def new_order_Quotation(self):
        self.access_saleOrder_new_Quotation_url()

    def new_order_partner(self, partnerName="alam_partner_190306", pOrC=0):
        self.access_saleOrder_new_partner_url(partnerName, pOrC)
