# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Feitas_course(models.Model):
    _name = 'feitas.course'
    name = fields.Char(string="名称", required=True)
    description = fields.Text(string="课程描述")
