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

from openerp.osv import fields, osv
from openerp.tools.translate import _
import time
import datetime
from babel.dates import format_date
from openerp.tools import DEFAULT_SERVER_DATETIME_FORMAT
from openerp import SUPERUSER_ID



class users_connection(osv.osv):
    _description = 'users_connection'
    _name= 'users.connection'

    def do_run_scheduler(self, cr, uid, automatic=False, use_new_cursor=False, context=None):
        res_users_obj = self.pool.get('res.users')
        users_active_obj = self.pool.get('users.active')
        res_lang_obj = self.pool.get('res.lang')
        #Solo tener en cuenta usuarios que esten activos Y que aciven su cuenta.
        users_ids = res_users_obj.search(cr, uid,[('active','=',True),('login_date','!=',False)])
        nb_active_users = len(users_ids)

        # Lang of user : need format
        user = res_users_obj.browse(cr, uid, uid)
        lang_ids = res_lang_obj.search(cr, uid, [('code','=',user.lang)])
        if len(lang_ids) == 1 :
            lang = res_lang_obj.browse(cr, uid, lang_ids[0])
        # Current month
        date_tmp = datetime.datetime.today()
        month_str = format_date(date_tmp,"MMMM",locale=lang.code)
        month_str = month_str[0].upper()+month_str[1:]

        week = date_tmp.isocalendar()[1]
        month = int(time.strftime("%m"))
        if nb_active_users :

            vals = {
                'date' : time.strftime(DEFAULT_SERVER_DATETIME_FORMAT),
                'month_str' : month_str,
                'year' : time.strftime("%Y"),
                'month' : month,
                'nb_users' : nb_active_users,
                'week' : week
            }
            nb_active_users_id = users_active_obj.create(cr, SUPERUSER_ID, vals, context=None)
            cr.commit()

        return True


    _columns = {
        'user_id' :                     fields.many2one('res.users', 'User'),
        'datetime_connection' :         fields.datetime("Connection Date with time"),
        'date_connection' :             fields.date("Connection Date"),
        'nb_request' :                  fields.integer("Number of OpenERP requests"),
        'year':                         fields.char('Year', size=4, readonly=True),
        'week':                         fields.char('Week', size=4, readonly=True),
        'month':                        fields.integer('Month', size=4, readonly=True),

    }
    _defaults = {
        # 'date_connection': lambda *a:  fields.datetime.now(),
    }
