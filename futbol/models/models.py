# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Equipo(models.Model):
    _name = 'futbol.equipos'
    _description = 'Tabla para los equipos'

    nombre = fields.Char("Nombre",required=True)
    ciudad = fields.Char("Ciudad",required=True)
    entrenador_id = fields.Many2one('futbol.entrenadores',string="Entrenador")

class Entrenador(models.Model):
    _name = 'futbol.entrenadores'
    _description = 'Tabla para los entrenadores'

    nombre = fields.Char("Nombre",required=True)
    edad = fields.Integer("Edad",required=True)
    equipo_id = fields.Many2one('futbol.equipos',string="Equipo")
    fecha_alta = fields.Date(string="Fecha de Alta", required=True,default=fields.Date.context_today)



