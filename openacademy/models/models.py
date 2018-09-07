# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Course(models.Model):
    _name = 'openacademy.course'
    name = fields.Char(string='课程名', required=True)
    description = fields.Text(string='课程描述')
    responsible_id = fields.Many2one('res.users', ondelete='set null', string='负责人', index=True)


class Session(models.Model):
    _name = 'openacademy.session'
    name = fields.Char(required=True, string="课时名称")
    start_date = fields.Date(string="开始日期")
    duration = fields.Float(digits=(6, 2), help="一天中的时段", string="时段")
    seats = fields.Integer(string="座位数")
    instructor_id = fields.Many2one('res.partner', string='教练', domain=[('instructor', '=', True)])
    course_id = fields.Many2one('openacademy.course', ondelete='cascade', string='课程', required=True)
    attendee_ids = fields.Many2many('res.partner', string='学员')
