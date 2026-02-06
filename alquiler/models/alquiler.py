from odoo import models, fields, api
from odoo.exceptions import ValidationError

class AlquilerProducto(models.Model):
    _name = 'alquiler.producto'
    _description = 'Registro de Alquiler de Productos'
    _order = 'fecha_inicio desc'

    name = fields.Char(string="Referencia", required=True, copy=False, readonly=True, default='Nuevo')
    cliente_id = fields.Many2one('res.partner', string="Cliente", required=True)
    producto_id = fields.Many2one('product.product', string="Producto", required=True)
    
    fecha_inicio = fields.Datetime(string="Fecha de Inicio", default=fields.Datetime.now, required=True)
    fecha_fin = fields.Datetime(string="Fecha de Fin")
    
    estado = fields.Selection([
        ('borrador', 'Borrador'),
        ('proceso', 'En Alquiler'),
        ('devuelto', 'Devuelto'),
        ('cancelado', 'Cancelado')
    ], string="Estado", default='borrador', tracking=True)

    notas = fields.Text(string="Notas de entrega")

    @api.constrains('fecha_inicio', 'fecha_fin')
    def _check_fechas(self):
        for record in self:
            if record.fecha_fin and record.fecha_fin < record.fecha_inicio:
                raise ValidationError("La fecha de fin no puede ser anterior a la fecha de inicio.")

    @api.model
    def create(self, vals):
        if vals.get('name', 'Nuevo') == 'Nuevo':
            vals['name'] = self.env['ir.sequence'].next_by_code('alquiler.producto') or 'Nuevo'
        return super(AlquilerProducto, self).create(vals)