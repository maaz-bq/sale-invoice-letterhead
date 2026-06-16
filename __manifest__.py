# -*- coding: utf-8 -*-
{
    'name': "Sale Invoice Letterhead Report",
    'Category': 'Account',
    'summary': "Invoice PDF with fixed-height empty letterhead header area",

    'depends': ['account', 'hotel_management_system', 'sale_management',],

    'data': [
        # 'security/ir.model.access.csv',
        'report/report.xml',
        'report/report_action.xml',
    ],
    'installable': True,
    'application': False,
}

