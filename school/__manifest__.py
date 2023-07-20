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
     'views/school.xml',
     
    ],

    'qweb': [
     'report/student_template.xml',
     'report/school_report.xml',
    ],

}  