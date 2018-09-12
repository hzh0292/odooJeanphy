# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order.line'
    x_value = fields.Float(string='暂存仓余量', compute='_compute_buffer_store')

    @api.depends('product_id')
    def _compute_buffer_store(self):
        for r in self:
            r.x_value = 3.14
