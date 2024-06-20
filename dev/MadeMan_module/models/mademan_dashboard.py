from odoo import models, fields, api

class MadeManDashboard(models.Model):
    _name = 'mademan.dashboard'
    _description = 'MadeMan Dashboard'

    total_appointments = fields.Integer(string='Total Appointments', compute='_compute_total_appointments')
    total_customers = fields.Integer(string='Total Customers', compute='_compute_total_customers')
    total_barbers = fields.Integer(string='Total Barbers', compute='_compute_total_barbers')

    @api.depends('total_appointments')
    def _compute_total_appointments(self):
        for record in self:
            record.total_appointments = self.env['mademan.appointment'].search_count([])

    @api.depends('total_customers')
    def _compute_total_customers(self):
        for record in self:
            record.total_customers = self.env['mademan.customer'].search_count([])

    @api.depends('total_barbers')
    def _compute_total_barbers(self):
        for record in self:
            record.total_barbers = self.env['mademan.barber'].search_count([])
