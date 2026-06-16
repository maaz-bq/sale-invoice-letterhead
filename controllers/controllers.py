# -*- coding: utf-8 -*-
# from odoo import http


# class AccountInvoiceNoHeaderFooter(http.Controller):
#     @http.route('/account_invoice_no_header_footer/account_invoice_no_header_footer', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/account_invoice_no_header_footer/account_invoice_no_header_footer/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('account_invoice_no_header_footer.listing', {
#             'root': '/account_invoice_no_header_footer/account_invoice_no_header_footer',
#             'objects': http.request.env['account_invoice_no_header_footer.account_invoice_no_header_footer'].search([]),
#         })

#     @http.route('/account_invoice_no_header_footer/account_invoice_no_header_footer/objects/<model("account_invoice_no_header_footer.account_invoice_no_header_footer"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('account_invoice_no_header_footer.object', {
#             'object': obj
#         })

