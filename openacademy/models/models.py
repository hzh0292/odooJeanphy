# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class Course(models.Model):
    _name = 'openacademy.course'
    name = fields.Char(string='课程名', required=True)
    description = fields.Text(string='课程描述')
    responsible_id = fields.Many2one('res.users', ondelete='set null', string='负责人', index=True)
    _sql_constraints = [
        (
            'name_description_check',
            'CHECK(name != description)',
            '课程的详细描述不能就是课程的标题！'
        ),
        (
            'name_unique',
            'UNIQUE(name)',
            '课程名必须是唯一的，不能重复！'
        ),
    ]


class Session(models.Model):
    _name = 'openacademy.session'
    name = fields.Char(required=True, string="课时名称")
    start_date = fields.Date(string="开始日期", default=fields.Date.today)
    duration = fields.Float(digits=(6, 2), help="一天中的时段", string="时段")
    seats = fields.Integer(string="座位数")
    active = fields.Boolean(string="有效", default=True)

    instructor_id = fields.Many2one('res.partner', string='教练', domain=['|', ('instructor', '=', True),
                                                                        ('category_id.name', 'ilike', 'Teacher')])
    course_id = fields.Many2one('openacademy.course', ondelete='cascade', string='课程', required=True)
    attendee_ids = fields.Many2many('res.partner', string='学员')

    taken_seats = fields.Float(string="上座率", compute="_taken_seats")

    @api.depends('seats', 'attendee_ids')
    def _taken_seats(self):
        for r in self:
            if not r.seats:
                r.taken_seats = 0.0
            else:
                r.taken_seats = 100.0 * len(r.attendee_ids) / r.seats

    @api.onchange('seats', 'attendee_ids')
    def _verify_valid_seats(self):
        if self.seats < 0:
            return {
                'warning': {
                    'title': "座位值错误",
                    'message': "座位的数量不能小于0"
                },
            }
        if self.seats < len(self.attendee_ids):
            return {
                'warning': {
                    'title': '座位不够',
                    'message': '请增加座位或者减少参与的学员人数'
                },
            }

    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor_not_in_attendees(self):
        for r in self:
            if r.instructor_id and r.instructor_id in r.attendee_ids:
                raise exceptions.ValidationError('课时的教练不能同时作为学员参与')
