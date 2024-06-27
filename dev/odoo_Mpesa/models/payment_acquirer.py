from odoo import models,fields

class PaymentAcquirer(models.Model):
    _inherit = 'payment.acquirer'

    mpesa_api_key = fields.Char(string='Mpesa API Key')
    mpesa_api_secret = fields.Char(string='Mpesa API Secret')
    mpesa_shortcode = fields.Char(string='Mpesa Shortcode')
    mpesa_passkey = fields.Char(string='Mpesa Passkey')


    provider = fields.Selection(
        selection_add=[('mpesa', 'Mpesa')],
        ondelete={'mpesa': 'set default'}
    )