from odoo import models, fields

class MadeManVisitCompletion(models.Model):
    _name = 'mademan.visit_completion'
    _description = 'Visit Completion'

    name = fields.Char(string='Name', required=True)
    visit_id = fields.Many2one('mademan.visit', string='Visit')
    completed = fields.Boolean(string='Completed', default=False)

    def mark_completed(self):
        self.completed = True
