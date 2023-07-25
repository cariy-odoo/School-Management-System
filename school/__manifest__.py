{
    'name': 'School Management',
    'summary': "School Manage App",
    'author':"aadil",
    'license': 'GPL-3',
    'website': 'https://www.odoo.com/',

    'depends' : ['base'],
    'application': True,

    'data':[
     'security/ir.model.access.csv',
     'views/student_management.xml',
     "views/teacher_management.xml",
     "views/subject_management.xml",
     
    ],

    'qweb': [
     'report/student_template.xml',
     'report/school_report.xml',
    ],

}  