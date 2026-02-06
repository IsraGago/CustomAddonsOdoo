# -*- coding: utf-8 -*-
{
    'name': "alquilerv2",

    'summary': "Modulo para el alquiler de productos",

    'description': """
Modulo para gestionar el alquiler de productos, permitiendo controlar disponibilidad, reservas y devoluciones.
    """,

    'author': "ISRAEL BENJAMÍN GAGO ACUÑA",
    'website': "https://www.israelgago.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','product'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/product_inherit_views.xml',
    ],
}

