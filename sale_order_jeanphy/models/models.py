# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order.line'
    # x_value = fields.Float(string='在手量', readonly=True)
    x_value = fields.Float(string='在手量', compute='_compute_buffer_store', store=True)

    @api.depends('product_id')
    def _compute_buffer_store(self):
        for r in self:
            r.x_value = r.product_id.qty_available

    # @api.onchange('product_id')
    # def _qty_avaiable_store(self):
    #     for r in self:
    #         if r.product_id:
    #             r.x_value = r.product_id.qty_available
