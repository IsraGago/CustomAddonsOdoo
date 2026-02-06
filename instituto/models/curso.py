from odoo import models, fields, api

class curso(models.Model):

    _name = "instituto.curso" #Nombre de la tabla en postegres
    _description =  "Tabla para la aplicación instituto"

    nombre = fields.Char('Titulo',required=True)
    description = fields.Text('Descripcion',required=True)
    is_done = fields.Boolean('Done?')
    active = fields.Boolean('Active?', default=True)
   
   
 
