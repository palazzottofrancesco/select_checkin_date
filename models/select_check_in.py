# -*- coding: utf-8 -*-

from odoo import models, fields
from datetime import timedelta

class SelectCheckIn(models.Model):
    _name = 'select.checkin'
    _description = 'Hotel Reservation'

    name = fields.Char()
    check_in = fields.Date()
    check_out = fields.Date()
    guests = fields.Integer()
    children = fields.Integer()
