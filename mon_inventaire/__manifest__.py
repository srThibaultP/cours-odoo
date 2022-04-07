# -*- coding: utf-8 -*-
{
    'name': "Mon inventaire",

    'summary': """
        Exercice d'une application de gestion d'inventaire""",

    'description': """
        Exercice d'une application de gestion d'inventaire
    """,

    'author': "Thibault Pech",
    'website': "http://www.github.com/srthibaultp",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/monInventaire.xml',
        'views/templates.xml',
        'views/menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
