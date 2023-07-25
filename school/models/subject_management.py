from odoo import models, fields, api

class Subject(models.Model):

    _name = 'subject.management'
    _description = 'Subject Management'

    name = fields.Char('Subject Name', required=True)
    code = fields.Char('Subject Code', required=True)
    level = fields.Char('Level')
    assign_teacher = fields.Many2one('teacher.management', string='Assign Teacher')

    @api.onchange('assign_teacher')
    def post_assign_teacher(self):
        if self.id:
            # Get the list of subjects that the teacher is already assigned to.
            teacher_subjects = self.assign_teacher.subjects

            # If the subject is not already in the list of subjects, add it.
            if self.id not in teacher_subjects:
                teacher_subjects.append(self.id)

            # Update the teacher's subjects.
            self.assign_teacher.subjects = teacher_subjects



