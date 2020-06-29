# -*- coding: utf-8 -*-
# from odoo import http


# class CashTransReport(http.Controller):
#     @http.route('/cash_trans_report/cash_trans_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cash_trans_report/cash_trans_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cash_trans_report.listing', {
#             'root': '/cash_trans_report/cash_trans_report',
#             'objects': http.request.env['cash_trans_report.cash_trans_report'].search([]),
#         })

#     @http.route('/cash_trans_report/cash_trans_report/objects/<model("cash_trans_report.cash_trans_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cash_trans_report.object', {
#             'object': obj
#         })
