{
    'name': 'Mpesa Payment Integration',
    'author':'moh doe',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Integration with Mpesa for payment processing',
    'description': """
        This module integrates Mpesa with the Odoo payment acquirers.
    """,
    'depends': ['base', 'account', 'payment','sale'],
    'data': [
        'views/payment_acquirer_views.xml',
        'data/payment_acquirer_data.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
