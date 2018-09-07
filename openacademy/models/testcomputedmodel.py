from odoo import models, fields, api


# import random


class ComputedModel(models.model):
    _name = 'test.computed'

    name = fields.Char(compute='_compute_name')
    value = fields.Integer()

    # @api.multi
    @api.depends('value')
    def _compute_name(self):
        for record in self:
            # record.name = str(random.randint(1, 1e6))
            record.name = "Record with value %s" % record.value
