# -*- coding: utf-8 -*-
from odoo import models, fields

class SelectCheckIn(models.Model):
    _name = 'select.checkin'
    _description = 'Select Checkin'

    # Usando selection, le opzioni sono una tupla (valore, etichetta)
    # Impostiamo il default come stringa vuota.
    guests = fields.Selection(
        selection=[('', ''), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')],
        string="Numero ospiti",
        default=''
    )
    children = fields.Selection(
        selection=[('', ''), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')],
        string="Numero bambini",
        default=''
    )
