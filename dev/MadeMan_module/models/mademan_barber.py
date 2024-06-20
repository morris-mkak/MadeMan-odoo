from odoo import models, fields

class MadeManBarber(models.Model):
    _name = 'mademan.barber'
    _description = 'MadeMan Barber'

    name = fields.Char(string='Name', required=True)
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    appointments = fields.One2many('mademan.appointment', 'barber_id', string='Appointments')
