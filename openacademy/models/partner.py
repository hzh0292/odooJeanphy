from odoo import fields, models


class Partner(models.Model):
    _inherit = 'res.partner'
    instructor = fields.Boolean("是否教练", default=False)
    session_ids = fields.Many2many('openacademy.session', string='参与课时', readonly=True)
