from odoo import models, fields

class MadeManHomepage(models.Model):
    _name = 'mademan.homepage'
    _description = 'MadeMan Homepage'

    banner_title = fields.Char(string='Banner Title', required=True)
    banner_subtitle = fields.Char(string='Banner Subtitle')
    info_text = fields.Text(string='Info Text')

