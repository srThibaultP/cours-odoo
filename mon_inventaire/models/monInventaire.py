# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Materiel(models.Model):
    _name = 'inventaire.materiel'
    _description = 'inventaire.materiel'

    name = fields.Char(string="nom du matériel", required=True)
    type = fields.Selection([('Switch','SWITCH'),('Routeur','ROUTEUR')])
    marque_id = fields.Many2one('inventaire.marque', string='Marque')
    description = fields.Text('Liste du matériel')

class Marque(models.Model):
    _name = 'inventaire.marque'
    _description = 'inventaire.marque'
    
    name = fields.Char(string="nom de la marque", required = True)
    materiel_ids = fields.One2many('inventaire.materiel','marque_id', string='Modèle associé')
    description = fields.Text()