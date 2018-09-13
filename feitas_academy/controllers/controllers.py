# -*- coding: utf-8 -*-
from odoo import http

# class FeitasAcademy(http.Controller):
#     @http.route('/feitas_academy/feitas_academy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/feitas_academy/feitas_academy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('feitas_academy.listing', {
#             'root': '/feitas_academy/feitas_academy',
#             'objects': http.request.env['feitas_academy.feitas_academy'].search([]),
#         })

#     @http.route('/feitas_academy/feitas_academy/objects/<model("feitas_academy.feitas_academy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('feitas_academy.object', {
#             'object': obj
#         })