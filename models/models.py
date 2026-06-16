# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class account_invoice_no_header_footer(models.Model):
#     _name = 'account_invoice_no_header_footer.account_invoice_no_header_footer'
#     _description = 'account_invoice_no_header_footer.account_invoice_no_header_footer'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

