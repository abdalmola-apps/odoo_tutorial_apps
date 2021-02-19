# -*- coding: utf-8 -*-
# from odoo import http


# class TutorialModule(http.Controller):
#     @http.route('/tutorial_module/tutorial_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tutorial_module/tutorial_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tutorial_module.listing', {
#             'root': '/tutorial_module/tutorial_module',
#             'objects': http.request.env['tutorial_module.tutorial_module'].search([]),
#         })

#     @http.route('/tutorial_module/tutorial_module/objects/<model("tutorial_module.tutorial_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tutorial_module.object', {
#             'object': obj
#         })
