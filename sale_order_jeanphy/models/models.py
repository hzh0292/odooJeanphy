# -*- coding: utf-8 -*-

from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order.line'
    x_value = fields.Integer('暂存仓余量')
