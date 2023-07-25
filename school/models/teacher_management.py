from odoo import fields, models

class Teacher(models.Model):
    _name = 'teacher.management'
    _description = 'Teacher Management'

    # teacher_id = fields.Integer(string='Teacher ID', required=True)
    teacher_full_name = fields.Char(string='Full Name', required=True)
    # last_name = fields.Char(string='Last Name', required=True)
    email = fields.Char(string='Email', required=True)
    phone = fields.Char(string='Phone')
    address = fields.Char(string='Address')
    birthday = fields.Date(string='Birthday')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    qualifications = fields.Text(string='Qualifications')
    subjects = fields.Many2one('subject.management', string='Subjects')
    experience = fields.Integer(string='Experience')
    availability = fields.Boolean(string='Availability')
    notes = fields.Text(string='Notes')

    # department = fields.Many2one('department.management', string='Department')
    # school = fields.Many2one('school.management', string='School')
    # salary = fields.Float(string='Salary')
    # contract_type = fields.Selection([('full_time', 'Full Time'), ('part_time', 'Part Time')], string='Contract Type')
    # image = fields.Binary(string='Image')

