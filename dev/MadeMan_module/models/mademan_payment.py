from odoo import models, fields

class MadeManPayment(models.Model):
    _name = 'mademan.payment'
    _description = 'Payments'

    visit_id = fields.Many2one('mademan.visit', string='Visit')
    amount = fields.Float(string='Amount')
    payment_date = fields.Date(string='Payment Date')
