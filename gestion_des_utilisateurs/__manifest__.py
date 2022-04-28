# -*- coding: utf-8 -*-
{
    'name': "Gestion des utilisateurs",

    'summary': """
        Projet Gestion des Utilisateurs""",

    'description': """
        Projet M36
    """,

    'author': "Thibault PECH",
    'website': "http://github.com/srthibaultp",

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
        'views/gestionDesUtilisateurs.xml',
        'views/templates.xml',
        'views/menus.xml',
        'views/kanban.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
