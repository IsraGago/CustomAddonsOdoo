from odoo import fields, models, api
from odoo.exceptions import ValidationError

class aeronaves(models.Model):
    _name = 'viajes.aeronaves'
    _description = 'Aviones para volar'
    _rec_name='compania'
    
    nombre = fields.Char(string="Nombre", required=True)
    compania = fields.Char(string="Matricula",required=True)
    compra = fields.Date(string="Fecha Compra",required=True)
    km = fields.Integer(string='Numero de km actuales',required=True)
    hangar = fields.Selection([('0','Londres'),('1','Bruselas'),('2','Luton')],string="Hangar del avion",default=0)
    
  
