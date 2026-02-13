from odoo import fields, models, api
from odoo.exceptions import ValidationError

class aeronaves(models.Model):
    _name = 'viajes.aeronaves'
    _description = 'Aviones para volar'
    
    nombre = fields.Char(string="Nombre", required=True)
    matricula = fields.Char(string="Matricula",required=True)
    fecha_compra = fields.Date(string="Fecha de compra",required=True)
    km = fields.Integer(string='Kilómetros actuales',required=True)
    hangar = fields.Selection([('0','Londres'),('1','Bruselas'),('2','Luton')],string="Hangar",default=0)
    
  
