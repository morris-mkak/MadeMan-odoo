from odoo import models, fields

class MadeManCharge(models.Model):
    _name = 'mademan.charge'
    _description = 'Charges'

    visit_id = fields.Many2one('mademan.visit', string='Visit')
    amount = fields.Float(string='Amount')
    description = fields.Text(string='Description')
