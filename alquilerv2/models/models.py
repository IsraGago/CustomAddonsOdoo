from odoo import models, fields,api
from odoo.exceptions import ValidationError

class Alquiler(models.Model):
    _name = 'alquilerv2.alquiler'
    _description = 'Registro de Alquiler'

    nombre = fields.Char(string='Referencia', required=True)
    cliente_id = fields.Many2one('res.partner', string='Cliente', required=True)
    fecha_inicio = fields.Date(string='Fecha Inicio', required=True)
    fecha_fin = fields.Date(string='Fecha Fin', required=True)
    
    # Relación con las líneas: apunta al modelo hijo y al campo que lo vincula
    lista_lineas = fields.One2many('alquilerv2.linea', 'alquiler_id', string='Productos')

class Linea(models.Model):
    _name = 'alquilerv2.linea'
    _description = 'Linea de Alquiler'

    # Campo que vincula la línea con el Alquiler padre
    alquiler_id = fields.Many2one('alquilerv2.alquiler', string='Alquiler')
    
    producto_id = fields.Many2one('product.product', string='Producto', required=True)
    cantidad = fields.Float(string='Cantidad', required=True,default=1.0)
    precio = fields.Float(string='Precio por día', required=True)
    subtotal = fields.Float(string='Subtotal', compute='_calcular_subtotal')

    @api.depends('cantidad', 'precio')
    def _calcular_subtotal(self):
        for registro in self:
            registro.subtotal = registro.cantidad * registro.precio * ((registro.alquiler_id.fecha_fin - registro.alquiler_id.fecha_inicio).days + 1)

    @api.constrains('fecha_inicio', 'fecha_fin')
    def _check_fechas(self):
        for registro in self:
            if registro.fecha_inicio and registro.fecha_fin:
                if registro.fecha_inicio > registro.fecha_fin:
                    raise ValidationError(_('¡Error! La fecha de inicio no puede ser posterior a la fecha de fin.'))

class Producto(models.Model):
    _inherit = 'product.template'

    es_alquilable = fields.Boolean(string='Es alquilable')