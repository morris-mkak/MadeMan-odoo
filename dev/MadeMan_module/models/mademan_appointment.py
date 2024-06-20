from odoo import models, fields

class MadeManAppointment(models.Model):
    _name = 'mademan.appointment'
    _description = 'MadeMan Appointment'

    date = fields.Datetime(string='Appointment Date', required=True)
    customer_id = fields.Many2one('mademan.customer', string='Customer', required=True)
    barber_id = fields.Many2one('mademan.barber', string='Barber', required=True)
    service_id = fields.Many2one('mademan.service', string='Service', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft')
