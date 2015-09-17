# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    Adapted by Noviat to
#     - enforce correct vat number
#     - support negative balance
#     - assign amount of tax code 71-72 correclty to grid 71 or 72
#     - support Noviat tax code scheme
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
import base64

from openerp.osv import fields, osv
from openerp.tools.translate import _
import time
import datetime
from babel.dates import format_date

class users_active(osv.osv):
    _description = 'users.active'
    _name = 'users.active'
    _columns = {
        'date' :        fields.datetime('Execution Date'),
        'month_str' :   fields.char('Month'),
        'year' :        fields.char('Year'),
        'week':         fields.char('Week', size=4, readonly=True),
        'month':        fields.integer('Month', size=4, readonly=True),
        'nb_users' :    fields.integer('Number of active users')
    }