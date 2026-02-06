# -*- coding: utf-8 -*-
{
    'name': "alquiler",

    'summary': "Sistema de alquiler de productos",

    'description': """
        Módulo para gestionar el alquiler de productos, incluyendo clientes, productos y contratos de alquiler.
    """,

    'author': "Israel Gago",
    'website': "https://www.agrotec.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "views/alquiler_producto_views.xml",
        "views/views.xml"
    ]
}

