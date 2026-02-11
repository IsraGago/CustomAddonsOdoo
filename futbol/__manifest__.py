# -*- coding: utf-8 -*-
{
    'name': "futbol",

    'summary': "Gestión de equipos de fútbol",

    'description': """
Módulo para gestionar equipos de fútbol.
    """,

    'author': "Israel Gago",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],

}

