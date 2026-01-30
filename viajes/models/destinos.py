from odoo import fields, models

class destinos(models.Model):
    _name = "viajes.destinos"
    _description = "Información sobre las rutas"

    matricula = fields.Many2one('viajes.aeronaves',ondelete='cascade',string="Matricula")
    origen = fields.Char(string="Origen", required=True)
    destino = fields.Char(string="Destino", required=True)
    fechavuelo = fields.Date(string="Fecha Vuelo", required=True)
