from odoo import models, fields, api, exceptions
import logging
from datetime import datetime

_logger = logging.getLogger(__name__)


class Scheduler_demo(models.Model):
    _name = 'scheduler.demo'
    name = fields.Char(required=True, string='名称')
    numberOfUpdates = fields.Integer('更新次数')
    lastModified = fields.Datetime('上次更新时间')

    def process_demo_scheduler_queue(self):
        scheduler_line_ids = self.env['scheduler.demo'].search([])
        for scheduler_line in scheduler_line_ids:
            _logger.info('line' + scheduler_line.name)
            scheduler_line.numberOfUpdates += 1
            scheduler_line.lastModified = datetime.utcnow()
