# -*- coding: utf-8 -*-
from odoo import models, fields, api


# class alternative_product(models.Model):
#     _name = 'alternative_product.alternative_product'
#     _description = 'alternative_product.alternative_product'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class ProductOrder(models.Model):
   _inherit = 'product.template'
   # select alternative products if original products not available
   alternative_products = fields.Many2many('product.product', 'name' , string='Alternative Products')

# if product already selected in someother alternative products
# then show that product in ths product alternative we don't need to select manually
# fill field automatically when that product selected somewhere in alternative product
   def autofill_product(self):
      print("alishba")
      return "alishba"
