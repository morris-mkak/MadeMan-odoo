from odoo import models, fields

class MadeManVisit(models.Model):
    _name = 'mademan.visit'
    _description = 'Visits'

    name = fields.Char(string='Visit Name', required=True)
    date = fields.Date(string='Visit Date')
    customer_id = fields.Many2one('mademan.customer', string='Customer')
    service_ids = fields.Many2many('mademan.service', string='Services')
    charge_ids = fields.One2many('mademan.charge', 'visit_id', string='Charges')
    payment_ids = fields.One2many('mademan.payment', 'visit_id', string='Payments')
    completed = fields.Boolean(string='Completed', default=False)

    def complete_visit(self):
        """ Mark the visit as completed """
        self.completed = True
