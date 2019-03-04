# -*- coding: utf-8 -*-
{
    'name': "待办事项",

    'summary': """
        这是一个待办事项的模块，用来熟悉odoo模块的开发过程
        主要是可以记录一些待办事项以及相应的分类""",

    'description': """
        可以插入多条待办事项
    """,

    'author': "jeanphy",
    'website': "http://www.walrus.com.cn",
    'application': True,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/todo_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/menus.xml',
    ]
}
