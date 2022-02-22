from odoo import models, fields, api

class Session(models.Model):
    _name = 'open_academy.session'
    _description = "OpenAcademy Sessions"

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6,2), help= "Duration in days")
    seats = fields.Integer(string="Number of seats")