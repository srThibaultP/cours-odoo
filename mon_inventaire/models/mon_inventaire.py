#-*- coding: utf-8 -*-

from odoo import models, fields, api


class Materiel(models.Model):
    _name = 'mon_inventaire.materiel'
    _description = 'mon_inventaire.materiel'

    name = fields.Char(string="Nom du matériel", required = True)
    type = fields.Selection([('Switch', 'SWITCH'),('Routeur', 'ROUTEUR')])
    marque_id = fields.Many2one('mon_inventaire.marque', string='Marque')
    responsable_id = fields.Many2one('mon_inventaire.responsable', string='Responsable')
    responsable_id_full_name = fields.Char(related='responsable_id.full_name', string='Responsable')
    description = fields.Text('Liste du matériel')

class Marque(models.Model):
    _name = 'mon_inventaire.marque'
    _description = 'mon_inventaire.marque'
    
    name = fields.Char(string="Nom de la marque", required = True)
    materiel_ids = fields.One2many('mon_inventaire.materiel', 'marque_id', string='Modèle associé')
    description = fields.Text()
    
class Responsable(models.Model):
    _name = 'mon_inventaire.responsable'
    _description = 'mon_inventaire.responsable'
    
    name = fields.Char(string="Nom", required = True)
    prenom = fields.Char(string="Prénom", required = True)
    full_name = fields.Char(compute='_compute_full_name', string='Nom complet')
    telephone = fields.Char(string="Téléphone", required = True)
    email = fields.Char(string="Email", required = True)
    materiel_ids = fields.One2many('mon_inventaire.materiel', 'responsable_id', string='Matériel associé')

    @api.depends('name', 'prenom')
    def _compute_full_name(self):
        for rec in self:
            rec.full_name = rec.name + ' ' + rec.prenom
