# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo import exceptions
from odoo.exceptions import ValidationError

import logging
_logger = logging.getLogger(__name__)


class centers (models.Model):
    _name = 'x_centers'

    name = fields.Char(string='name',
                       index=True,
                       track_visibility='onchange',

                       )

    x_lat = fields.Float(
        string='x_lat',
        index=True,

    )
    x_long = fields.Float(
        string='x_long',

        index=True

    )

    

    

