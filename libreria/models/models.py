# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class libreria(models.Model):
    _name = 'libreria.libreria'
    _description = 'libreria.libreria'

    name = fields.Char(string="Nombre", required=True)
    codigo = fields.Integer(string="Código", required=True,default=0)
    rate = fields.Float(string="Rate",required=True)
    descripcion = fields.Text(string="Descripción")
    fecha_fundacion = fields.Date(string='Fecha de fundación', required=True, default=fields.Date.context_today)
    direccion = fields.Char(string="Dirección", required=True)
    
    @api.constrains('rate')
    def _check_fechas(self):
        for registro in self:
            if registro.rate:
                if registro.rate < 0 or registro.rate > 5:
                    raise ValidationError(('¡Error! el rate de la librería no puede ser negativo o mayor que cinco.'))


