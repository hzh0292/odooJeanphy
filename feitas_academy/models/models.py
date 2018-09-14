# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class feitas_course(models.Model):
    _name = 'feitas.course'
    name = fields.Char(string='名称', required=True)
    description = fields.Text(string='描述')
    manager_id = fields.Many2one('res.users', default=lambda self: self.env.user, string='负责人')
    type = fields.Selection([('i', '理论'),
                             ('e', '实操'),
                             ('both', '理论+实操')], default='both', string='类型')
    total_hours = fields.Float(string='总课程', compute='_total_course_hours')
    lesson_hours = fields.Float(string='理论课时')
    exercise_hours = fields.Integer(string='实操课时')

    @api.depends('lesson_hours', 'exercise_hours')
    def _total_course_hours(self):
        for r in self:
            r.total_hours = r.lesson_hours + r.exercise_hours

    _sql_constraints = [
        (
            'name_unique',
            'UNIQUE(name)',
            '课程名称系统内不能重复'
        ),
    ]

    @api.onchange('exercise_hours')
    def _verify_hours_3x_or_4x(self):
        if self.exercise_hours % 3 != 0 and self.exercise_hours % 4 != 0:
            self.update({'exercise_hours': (self.exercise_hours // 3 + 1) * 3})
            return {
                'warning': {
                    'title': "实操课时取值错误",
                    'message': "实操课时只能是3或4的倍数"
                },
            }

    @api.onchange('exercise_hours', 'lesson_hours')
    def _verify_course_type(self):
        if self.type == 'i' and self.exercise_hours != 0:
            self.update({'exercise_hours': 0})
            return {
                'warning': {
                    'title': "当前为理论课程",
                    'message': "理论课程无实操课时"
                },
            }
        if self.type == 'e' and self.lesson_hours != 0:
            self.update({'lesson_hours': 0})
            return {
                'warning': {
                    'title': "当前为实操课程",
                    'message': "实操课时没有理论课时"
                },
            }

    @api.constrains('exercise_hours')
    def _check_hours_3x_or_4x(self):
        for r in self:
            if r.exercise_hours % 3 != 0 and r.exercise_hours % 4 != 0:
                raise exceptions.ValidationError('实操课时只能是3或4的倍数')

    # @api.multi
    # @api.constrains('manager_id')
    # def _manage_course_check(self):
    #     self.ensure_one()
    #     course_ids = self.env['feitas.course'].search(['manager_id', '=', self.manager_id)])
    #     if len(course_ids) > 3:
    #         raise exceptions.ValidationError('同一个用户不能负责3门以上的课程')
    #     sum_total_hours = sum_lesson_hours = 0
    #     for r in course_ids:
    #         sum_total_hours += r.total_hours
    #         sum_lesson_hours += r.lesson_hours
    #     if sum_total_hours > 200:
    #         raise exceptions.ValidationError('同一个用户负责总时长不能超过200小时')
    #     if sum_lesson_hours > 100:
    #         raise exceptions.ValidationError('同一个用户负责总理论课时时长不能超过100小时')
