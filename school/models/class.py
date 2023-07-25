from odoo import models,fields,api,_

class Class(models.Model):
    _name = "school.class"
    _description = 'classes of student'
    _log_access=False
    _order = "name"

    # name = fields.Char(string =)
    # sequence=fields.Integer("Sequence",default=1)
    # name = fields.Char("Property Type", required=True)
    # property_ids = fields.One2many('estate.property','property_type_id')
    # offer_ids=fields.One2many('estate.property.offer','property_type_id')
    # offer_count =fields.Integer(compute="_compute_offer_count")
    
