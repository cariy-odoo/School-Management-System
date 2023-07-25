# from odoo import models,fields,api


# class SchoolItem(models.Model):
#     _name = 'school.items'


# student_id = fields.Many2one('res.users', string='student', default=lambda self: self.env.user)
# class_id = fields.Many2one('school.student',string='Class')
# division = fields.Char(string='Division')
# admn_date = fields.Date(string='Admn Date')
# product_ids = fields.Many2many('product.product',string='Items')

# @api.onchange('class_id')
# def onchange_class(self):
#     student = self.env['school.student'].search([('class_id','=',self.class_id.id)])
#     print("student",student)
#     val = self.env['school.student'].browser(self.class_id)
#     print('val',val)
#     self.student_id = student