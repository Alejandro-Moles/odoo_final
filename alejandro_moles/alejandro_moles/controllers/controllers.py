# -*- coding: utf-8 -*-
# from odoo import http


# class AlejandroMoles(http.Controller):
#     @http.route('/alejandro_moles/alejandro_moles/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/alejandro_moles/alejandro_moles/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('alejandro_moles.listing', {
#             'root': '/alejandro_moles/alejandro_moles',
#             'objects': http.request.env['alejandro_moles.alejandro_moles'].search([]),
#         })

#     @http.route('/alejandro_moles/alejandro_moles/objects/<model("alejandro_moles.alejandro_moles"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('alejandro_moles.object', {
#             'object': obj
#         })
