# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo import exceptions
from odoo.exceptions import ValidationError


import logging
_logger = logging.getLogger(__name__)


class luckymobile(models.Model):
    _inherit = 'crm.lead'
    
    x_attachment_text = fields.Text(string="Description", required=False)
    x_Vertical = fields.Text(string="Industry", required=False)
    img_base64 = fields.Binary(string="Photo", compute='get_default_img',store=False)
    x_lat = fields.Char(string='Latitude')
    x_long = fields.Char(string='Longitude')
    x_accuracy = fields.Char(string='Accuracy')
    X_administrative_area_level_1 = fields.Text(string="administrative_area_level_1", required=False)
    X_administrative_area_level_2 = fields.Text(string="administrative_area_level_2", required=False)
    X_administrative_area_level_3 = fields.Text(string="administrative_area_level_3", required=False)
    X_administrative_area_level_4 = fields.Text(string="administrative_area_level_4", required=False)
    X_administrative_area_level_5 = fields.Text(string="administrative_area_level_5", required=False)
    X_archipelago = fields.Text(string="archipelago", required=False)
    X_colloquial_area = fields.Text(string="colloquial_area", required=False)
    X_continent = fields.Text(string="continent", required=False)
    X_country = fields.Text(string="country", required=False)
    X_establishment = fields.Text(string="establishment", required=False)
    X_finance = fields.Text(string="finance", required=False)
    X_floor = fields.Text(string="floor", required=False)
    X_food = fields.Text(string="food", required=False)
    X_general_contractor = fields.Text(string="general_contractor", required=False)
    X_geocode = fields.Text(string="geocode", required=False)
    X_health = fields.Text(string="health", required=False)
    X_intersection = fields.Text(string="intersection", required=False)
    X_locality = fields.Text(string="locality", required=False)
    X_natural_feature = fields.Text(string="natural_feature", required=False)
    X_neighborhood = fields.Text(string="neighborhood", required=False)
    X_place_of_worship = fields.Text(string="place_of_worship", required=False)
    X_point_of_interest = fields.Text(string="point_of_interest", required=False)
    X_political = fields.Text(string="political", required=False)
    X_post_box = fields.Text(string="post_box", required=False)
    X_postal_code = fields.Text(string="postal_code", required=False)
    X_postal_code_prefix = fields.Text(string="postal_code_prefix", required=False)
    X_postal_code_suffix = fields.Text(string="postal_code_suffix", required=False)
    X_postal_town = fields.Text(string="postal_town", required=False)
    X_premise = fields.Text(string="premise", required=False)
    X_room = fields.Text(string="room", required=False)
    X_route = fields.Text(string="route", required=False)
    X_street_address = fields.Text(string="street_address", required=False)
    X_street_number = fields.Text(string="street_number", required=False)
    X_sublocality = fields.Text(string="sublocality", required=False)
    X_sublocality_level_1 = fields.Text(string="sublocality_level_1", required=False)
    X_sublocality_level_2 = fields.Text(string="sublocality_level_2", required=False)
    X_sublocality_level_3 = fields.Text(string="sublocality_level_3", required=False)
    X_sublocality_level_4 = fields.Text(string="sublocality_level_4", required=False)
    X_sublocality_level_5 = fields.Text(string="sublocality_level_5", required=False)
    X_subpremise = fields.Text(string="subpremise", required=False)
    X_town_square = fields.Text(string="town_square", required=False)
    X_formatted_address = fields.Text(string="formatted_address", required=False)


    def get_default_img(self):
        #_logger.info('desc_text maged ! "%s"' % (self.desc_text.replace('data:image/png;base64,','')))
        if self.x_attachment_text:
            if "data:image/png;base64" in self.x_attachment_text and 'jsonrpc' not in self.x_attachment_text:
                self.img_base64 = self.x_attachment_text.replace('data:image/png;base64,','')
            else:
                self.img_base64 = None