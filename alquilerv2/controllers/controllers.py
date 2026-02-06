# -*- coding: utf-8 -*-
# from odoo import http


# class Alquilerv2(http.Controller):
#     @http.route('/alquilerv2/alquilerv2', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/alquilerv2/alquilerv2/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('alquilerv2.listing', {
#             'root': '/alquilerv2/alquilerv2',
#             'objects': http.request.env['alquilerv2.alquilerv2'].search([]),
#         })

#     @http.route('/alquilerv2/alquilerv2/objects/<model("alquilerv2.alquilerv2"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('alquilerv2.object', {
#             'object': obj
#         })

