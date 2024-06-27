from odoo import http
from odoo.http import request

class MpesaController(http.Controller):

    @http.route('/payment/mpesa/notify', type='json', auth='public', csrf=False)
    def mpesa_notify(self, **post):
        _logger.info(f"Mpesa notification received: {post}")
        payment_data = {
            'transaction_id': post.get('transaction_id'),
            'amount': float(post.get('amount')),
            'sale_order': post.get('reference')
        }
        payment_model = request.env['mpesa.payment']
        if payment_model.process_payment(payment_data):
            return {'status': 'success'}
        else:
            return {'status': 'error'}
