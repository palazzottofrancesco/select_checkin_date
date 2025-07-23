# -*- coding: utf-8 -*-
from odoo import models, fields

class SelectCheckIn(models.Model):
    _name = 'select.checkin'
    _description = 'Select Checkin'

    guests = fields.Selection(
        selection=[('', ''), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')],
        string="Numero ospiti",
        default=''
    )
    children = fields.Selection(
        selection=[('', ''), ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')],
        string="Numero bambini",
        default=''
    )
