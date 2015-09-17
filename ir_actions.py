# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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
import logging
import os
import re
from socket import gethostname
import time

from openerp import SUPERUSER_ID
from openerp import netsvc, tools
from openerp.osv import fields, osv
from openerp.report.report_sxw import report_sxw, report_rml
from openerp.tools.config import config
from openerp.tools.safe_eval import safe_eval as eval
from openerp.tools.translate import _

_logger = logging.getLogger(__name__)

class actions(osv.osv):
    _inherit = 'ir.actions.actions'

    def read(self, cr, uid, ids, fields=None, context=None, load='_classic_read'):
        fct_src = super(actions, self).read
        users_connection_obj = self.pool.get('users.connection')
        if isinstance(ids,list) and len(ids) == 1 and load == '_classic_read':
            print 'classic read'
            tmp = 0
            connection_today_ids = users_connection_obj.search(cr, 1, [('user_id','=',uid),('date_connection','=',time.strftime("%Y-%m-%d"))])
            if len(connection_today_ids) >1 :
            # One more connexion today => take the last
                position = len(connection_today_ids)-1
                tmp = 1
            elif len(connection_today_ids) == 1 :
            # Take first position
                position = 0
                tmp = 1
            if tmp == 1 :
                connection_today = users_connection_obj.browse(cr, 1, connection_today_ids[position])
                if connection_today :
                    vals = {
                       'nb_request' : connection_today.nb_request +1
                    }
                    users_connection_obj.write(cr, 1, connection_today.id, vals, context=None)

        return fct_src(cr, uid, ids, fields=fields, context=context, load=load)
