# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import date
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError     


class School(models.Model):
    _name = 'school.student'

    name = fields.Many2one('res.partner', string='Student')
    address = fields.Char(string='Address')
    class_id = fields.Integer(string='Class')
    division = fields.Char(string='Division')
    dob = fields.Date(string='Date of Birth')
    age = fields.Integer(string='Age', compute = '_compute_age')
    admn_date = fields.Date(string = 'Admn Date', default=fields.date.today())
    admn_code = fields.Char(string = 'Admn Code', copy=False, readonly=False, index=True, default = lambda self: _('New'))




    @api.model
    def create(self,vals):
        """Function for creating sequnce"""
        if vals.get('admn_code', 'New') == 'New':
            vals['admn_code'] = self.env['ir.sequence'].next_by_code(
                'school.student.sequence') or 'New'
        result = super(School,self).create(vals)
        return result
    
    @api.onchange('name')
    def onchange_studnt(self):
        self.address = self.name.street

    @api.depends('dob')
    def _compute_age(self):
        self.age = False
        for i in self:
            i.age = relativedelta(date.today(),i.dob).years

    @api.constrains('dob')
    def validation_constrains(self):
        for i in self:
            today = fields.date.today()
            for i in self:
                if i.dob >today:
                    raise ValidationError("Date of Birth is not proper")
                elif (i.class_id > 12) or (i.class_id < 1):
                    raise ValidationError("Class should be from 1st to 12th")
                
    _sql_constraints = [('unique_admn','unique(admn_code)', 'This admn code is already exist')]
                
    # _sql_constraints = [('check_quotation_validity_days','CHECK(quotation_validity_days > 0)', 'Quotation validity is required and must be greater thsn 0')]