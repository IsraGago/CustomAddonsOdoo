# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AlquilerReserva(models.Model):
    _name = "alquiler.reserva"
    _description = "Contrato de Alquiler de productos"
    
    name = fields.Char(string = 'Referencia',required = True,copy = False,readonly=True,default='Nuevo')
    partner_id = fields.Many2one('res.partner',string="Cliente",required = True)
    date_start = fields.Date(string='Fecha de Inicio',default = fields.Date.today,required = True)
    date_end = fields.Date(string="Fecha de Fin",required = True)
    
    alquiler_ids = fields.One2many('alquiler.linea','alquiler_id',string='Líneas de alquiler')
    
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('confirmed', 'Confirmado'),
        ('done', 'Finalizado'),
        ('cancel', 'Cancelado'),
    ], string='Estado', default='draft')
    
    total_cost = fields.Float(string='Coste Total', compute ='_compute_total_cost',store=True)
    @api.depends('alquiler_ids.price_unit', 'alquiler_ids.quantity', 'date_start', 'date_end')
    def _compute_total_cost(self):
        for rec in self:
            dias = 0
            if rec.date_start and rec.date_end:
                delta = rec.date_end - rec.date_start
                dias = delta.days if delta.days > 0 else 1 # Mínimo 1 día
            
            total_lineas = sum(line.price_unit * line.quantity for line in rec.alquiler_ids)
            rec.total_cost = total_lineas * dias

class AlquilerLinea(models.Model):
    _name = "alquiler.linea"
    _description = "Línea de alquiler"
    
    alquiler_id = fields.Many2one('alquiler.reserva',string='Reserva',required = True,ondelete='cascade')
    product_id = fields.Many2one('product.product',string='Producto',required = True,domain=[('is_rentable', '=', True)])
    quantity = fields.Integer(string='Cantidad',default=1,required = True)
       
    price_unit = fields.Float(
    related='product_id.rental_price', 
    string='Precio por día', 
    readonly=False,
    store=True
)
  
class ProductTemplate(models.Model):
    _inherit = 'product.template'
    is_rentable = fields.Boolean(string='Es alquilable', default=False)
    rental_price = fields.Float(string='Precio de alquiler por día', default=0.0)