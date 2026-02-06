# -*- coding: utf-8 -*-
{
    'name': "alquilerv2",

    'summary': "Sistema de alquiler de productos",

    'description': """
Long description of module's purpose
    """,

    'author': "Israel Benjamín Gago Acuña",
    'website': "https://www.israelgago.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock','product'],

    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "views/alquiler_reserva_views.xml",
        "views/templates.xml",
        "views/views.xml"
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

