from odoo import models, fields

class MadeManCustomer(models.Model):
    _name = 'mademan.customer'
    _description = 'MadeMan Customer'

    name = fields.Char(string='Name', required=True)
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    appointments = fields.One2many('mademan.appointment', 'customer_id', string='Appointments')
