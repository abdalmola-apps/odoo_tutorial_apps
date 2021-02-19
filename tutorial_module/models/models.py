# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Tutorial(models.Model):
    _name = 'tutorial.module'
    _description = 'Tutorial Module'

    name = fields.Char()