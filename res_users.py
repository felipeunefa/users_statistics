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
from functools import partial
import logging
from lxml import etree
from lxml.builder import E

import openerp
from openerp import SUPERUSER_ID
from openerp import pooler, tools
import openerp.exceptions
from openerp.osv import fields,osv
from openerp.osv.orm import browse_record
from openerp.tools.translate import _
import time
from openerp.tools import DEFAULT_SERVER_DATETIME_FORMAT
import datetime
from openerp import SUPERUSER_ID


class res_users(osv.osv):
    _inherit = "res.users"

    # Overide authentification method
    def authenticate(self, db, login, password, user_agent_env):
        uid = self._login(db, login, password)
        cr = pooler.get_db(db).cursor()
        users_connection_obj = self.pool.get('users.connection')
        res_users_obj = self.pool.get('res.users')

        uid = self._login(db, login, password)

        if uid :
            user = res_users_obj.browse(cr, uid, uid)
            if user:
                    vals = {
                        'user_id' :             user.id,
                        # 'date_connection' :   time.strftime(format+" %H:%M:%S"),
                        'datetime_connection' : time.strftime(DEFAULT_SERVER_DATETIME_FORMAT),
                        'date_connection' :     time.strftime("%Y-%m-%d"),
                        'year' :                time.strftime("%Y"),
                        'week' :                datetime.datetime.today().isocalendar()[1],
                        'month' :               int(time.strftime("%m")),
                    }
                    connexion_id = users_connection_obj.create(cr, SUPERUSER_ID, vals, context=None)
                    cr.commit()

        return super(res_users, self).authenticate(db, login, password, user_agent_env)
