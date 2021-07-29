# -*- coding: utf-8 -*-
{
    'name': "Send  Order",

    'summary': """
        this module allows to send orders""",

    'description': """
    """,

    'author': "Belporo Jules",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Project',
    'version': '14.0.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        'views/add_button.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}