# -*- coding: utf-8 -*-
from odoo import http

# class /mnt/extra-addons/odoo-customization(http.Controller):
#     @http.route('//mnt/extra-addons/odoo-customization//mnt/extra-addons/odoo-customization/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//mnt/extra-addons/odoo-customization//mnt/extra-addons/odoo-customization/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/mnt/extra-addons/odoo-customization.listing', {
#             'root': '//mnt/extra-addons/odoo-customization//mnt/extra-addons/odoo-customization',
#             'objects': http.request.env['/mnt/extra-addons/odoo-customization./mnt/extra-addons/odoo-customization'].search([]),
#         })

#     @http.route('//mnt/extra-addons/odoo-customization//mnt/extra-addons/odoo-customization/objects/<model("/mnt/extra-addons/odoo-customization./mnt/extra-addons/odoo-customization"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/mnt/extra-addons/odoo-customization.object', {
#             'object': obj
#         })