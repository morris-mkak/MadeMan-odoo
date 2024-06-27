# -*- coding: utf-8 -*-
{
    'name': "MadeMan_module",
    'author': "Moh Doe",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base','contacts','website'],
    'demo': [
        'demo/demo.xml',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/mademan_actions.xml',
        'views/mademan_menus.xml',
        'views/mademan_barber_views.xml',
        'views/mademan_customer_views.xml',
        'views/mademan_service_views.xml',
        'views/mademan_appointment_views.xml',
        'views/dashboard_views.xml',
        'views/homepage_templates.xml',
        'views/mademan_visit_views.xml',
        'views/mademan_charge_views.xml',
        'views/mademan_payment_views.xml',
        'views/mademan_visit_completion_views.xml',
        'views/mademan_homepage_views.xml',

        # 'views/appointment_calendar.xml',
        # 'reports/report_appointment.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}