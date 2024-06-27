from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class MpesaPayment(models.Model):
    _name = 'mpesa.payment'
    _description = 'Mpesa Payment'

    name = fields.Char(string='Transaction ID', required=True)
    amount = fields.Float(string='Amount', required=True)
    partner_id = fields.Many2one('res.partner', string='Customer', required=True)
    sale_order_id = fields.Many2one('sale.order', string='Sale Order', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),
        ('error', 'Error')
    ], string='Status', default='draft')

    @api.model
    def process_payment(self, data):
        sale_order = self.env['sale.order'].search([('name', '=', data['sale_order'])], limit=1)
        if sale_order:
            payment = self.create({
                'name': data['transaction_id'],
                'amount': data['amount'],
                'partner_id': sale_order.partner_id.id,
                'sale_order_id': sale_order.id,
                'state': 'done'
            })
            sale_order.action_confirm()
            sale_order._create_invoices()
            _logger.info(f"Payment processed: {payment.name}")
            return True
        else:
            _logger.error(f"Sale Order not found: {data['sale_order']}")
            return False
