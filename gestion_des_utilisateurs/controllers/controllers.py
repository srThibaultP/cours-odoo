# -*- coding: utf-8 -*-
# from odoo import http


# class GestionDesUtilisateurs(http.Controller):
#     @http.route('/gestion_des_utilisateurs/gestion_des_utilisateurs/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion_des_utilisateurs/gestion_des_utilisateurs/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion_des_utilisateurs.listing', {
#             'root': '/gestion_des_utilisateurs/gestion_des_utilisateurs',
#             'objects': http.request.env['gestion_des_utilisateurs.gestion_des_utilisateurs'].search([]),
#         })

#     @http.route('/gestion_des_utilisateurs/gestion_des_utilisateurs/objects/<model("gestion_des_utilisateurs.gestion_des_utilisateurs"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion_des_utilisateurs.object', {
#             'object': obj
#         })
