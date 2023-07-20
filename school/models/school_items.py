from odoo import models,fields,api


class SchoolItem(models.Model):
    _name = 'school_items'
    _rec_name = 'class_id'


student_id = fields.Many2many('school.student',string='Student')
class_id = fields.Many2one('class.student', string='Class')
division = fields.Char(string='Division',related='student_id.division')
admn_date = fields.Date(string='Admn Date', related='student_id.admn_date')
product_ids = fields.Many2many('product.product',string='Items')

@api.onchange('class_id')
def onchange_class(self):
    student = self.env['school.student'].search([('class_id','=',self.class_id.id)])
    print("student",student)
    val = self.env['school.student'].browser(self.class_id)
    print('val',val)
    self.student_id = student