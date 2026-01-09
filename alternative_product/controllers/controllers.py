# -*- coding: utf-8 -*-
# from odoo import http


# class AlternativeProduct(http.Controller):
#     @http.route('/alternative_product/alternative_product', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/alternative_product/alternative_product/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('alternative_product.listing', {
#             'root': '/alternative_product/alternative_product',
#             'objects': http.request.env['alternative_product.alternative_product'].search([]),
#         })

#     @http.route('/alternative_product/alternative_product/objects/<model("alternative_product.alternative_product"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('alternative_product.object', {
#             'object': obj
#         })

