# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo import exceptions
from odoo.exceptions import ValidationError
from math import sin, cos, sqrt, atan2, radians
import json
import datetime
import string
import random

import logging
_logger = logging.getLogger(__name__)


class activities (models.Model):
    _name = 'x_activity'
    _order = 'create_date desc'
    x_name = fields.Char(string="Name", required=False, index=True, track_visibility=False)
    x_status = fields.Selection(string="Status", index=True, selection=[("New","New"),("Done","Done"),("Cancelled","Cancelled")], required=True , default="New")
    x_lead = fields.Many2one(comodel_name="crm.lead",domain="[]", index=True, string="Lead/Opportuniy", required=False)
    x_partner = fields.Many2one(comodel_name="res.partner",domain="[]", index=True, string="Customer", required=False)
    x_assgined_to = fields.Many2one(comodel_name="res.users",domain="[]", index=True, string="Assgined to", required=True)
    x_lat = fields.Char(string="Location Lat")
    x_long = fields.Char(string="Location Long")
    x_accuracy = fields.Char(string="Accuracy")
    x_lead_lat = fields.Char(string="Lead Lat",related='x_lead.x_lat')
    x_lead_long = fields.Char(string="Lead Long",related='x_lead.x_long')
    x_distance_between = fields.Char(string="x_distance_between")
    isfake = fields.Boolean(string='isFake?',compute='_isfake',store=True)
 

    @api.depends('x_lead_lat', 'x_lead_long','x_lat','x_long')
    def _isfake(self):
        for record in self:
           
            

            # approximate radius of earth in km
            R = 6373.0

            lat1 = radians(float(record.x_lat))
            lon1 = radians(float(record.x_long))
            lat2 = radians(float(record.x_lead_lat))
            lon2 = radians(float(record.x_lead_long))

            dlon = lon2 - lon1
            dlat = lat2 - lat1

            a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))

            distance = R * c
            record.x_distance_between=distance
            if distance >1:
                record.isfake =True
            else:
                record.isfake =False

    






