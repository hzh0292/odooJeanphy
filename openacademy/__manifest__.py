# -*- coding: utf-8 -*-
{
    'name': "开源学院",

    'summary': """
        开源学院系统
        用来管理一些培训事宜""",

    'description': """
        开源学院管理系统主要管理如下细则：
          - 培训课程管理
          - 培训现场管理
          - 参与者登记
    """,

    'author': "Jeanphy",
    'website': "http://www.walrus.com.cn",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': '学习',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/openacademy.xml',
        'views/partner.xml',
        'views/scheduler_demo.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
