# -*- coding: utf-8 -*-


import string
from odoo import models, fields, api


# class gestion_des_utilisateurs(models.Model):
#     _name = 'gestion_des_utilisateurs.gestion_des_utilisateurs'
#     _description = 'gestion_des_utilisateurs.gestion_des_utilisateurs'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class classe(models.Model):
    _name = 'gestion_des_utilisateurs.classe'
    _description = 'gestion_des_utilisateurs.classe'

    name = fields.Char(string="Classe", required=True)
    alternant_ids = fields.One2many('gestion_des_utilisateurs.alternants', 'classe_id', string='Alternant')
    description = fields.Text("Intitulé de la classe")
    
class alternants(models.Model):
    _name = 'gestion_des_utilisateurs.alternants'
    _description = 'gestion_des_utilisateurs.alternants'

    name = fields.Char(string="Nom", required=True)
    prenom = fields.Char(string="Prénom", required=True)
    email = fields.Char(string="Email", required=True)
    classe_id = fields.Many2one(
        'gestion_des_utilisateurs.classe', string='Classe', required=True)
    entreprise_id = fields.Many2one(
        'gestion_des_utilisateurs.entreprise', string='Entreprise')
    
class entreprise(models.Model):
    _name = 'gestion_des_utilisateurs.entreprise'
    _description = 'gestion_des_utilisateurs.entreprise'

    name = fields.Char(string="Entreprise", required=True)
    adresse = fields.Char(string="Adresse")
    alternant_ids = fields.One2many('gestion_des_utilisateurs.alternants', 'entreprise_id', string='Alternant')
    tuteur_ids = fields.One2many('gestion_des_utilisateurs.tuteurs', 'entreprise_id', string='Tuteur')


class tuteurs(models.Model):
    _name = 'gestion_des_utilisateurs.tuteurs'
    _description = 'gestion_des_utilisateurs.tuteurs'

    name = fields.Char(string="Nom", required=True)
    prenom = fields.Char(string="Prénom", required=True)
    email = fields.Char(string="Email", required=True)
    entreprise_id = fields.Many2one(
        'gestion_des_utilisateurs.entreprise', string='Entreprise')
