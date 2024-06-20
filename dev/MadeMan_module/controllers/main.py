from odoo import http
from odoo.http import request


class MadeManHomepageController(http.Controller):

    @http.route('/mademan/homepage', auth='public', website=True)
    def homepage(self, **kwargs):
        homepage_record = request.env['mademan.homepage'].sudo().search([], limit=1)

        values = {
            'banner_title': homepage_record.banner_title if homepage_record else 'Welcome to MadeMan Barbershop',
            'banner_subtitle': homepage_record.banner_subtitle if homepage_record else 'Your one-stop solution for grooming and styling',
            'info_text': homepage_record.info_text if homepage_record else 'Book an appointment with our professional barbers and experience the best grooming services.'
        }
        return request.render('mademan.homepage', values)
