# -*- coding: utf-8 -*-
{
    'name': "Feitas学院",

    'summary': """
        odoo11开发项目实践""",

    'description': """
        该项目实践课程涵盖odoo开发常用技能点
    """,

    'author': "Jeanphy",
    'website': "http://malijie.cc",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'training',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'reports/course_template.xml',
        'reports/report.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}