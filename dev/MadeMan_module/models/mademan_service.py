from odoo import models, fields

class MadeManService(models.Model):
    _name = 'mademan.service'
    _description = 'MadeMan Service'

    name = fields.Char(string='Service Name', required=True)
    price = fields.Float(string='Price')
