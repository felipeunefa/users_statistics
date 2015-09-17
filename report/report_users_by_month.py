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
import time
from report import report_sxw
from osv import osv




class report_parser(report_sxw.rml_parse):

    def __init__(self, cr, uid, name, context):
        super(report_parser, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'time': time,
            'cr':cr,
            'uid': uid,
            'general_info': self.general_info,
            'tab_year': self.tab_year
            })

    def tab_year(self, obj):
        cr = self.localcontext.get('cr')
        uid = self.localcontext.get('uid')
        users_active_obj = self.pool.get('users.active')
        all_active_users_ids = users_active_obj.search(cr, uid,[])
        all_active_users = users_active_obj.browse(cr, uid, all_active_users_ids)
        tab_year = []
        for active_user in all_active_users :
            if active_user.year in tab_year :
                print 'continue'
            else :
                tab_year.append(active_user.year)

        return tab_year



    def general_info(self, obj):
        cr = self.localcontext.get('cr')
        uid = self.localcontext.get('uid')
        context = self.localcontext
        db = cr.dbname
        obj_user = self.pool.get('res.users')
        users_active_obj = self.pool.get('users.active')
        res_lang_obj = self.pool.get('res.lang')

        user = obj_user.browse(cr, uid, uid, context=context)
        obj_company = obj_user.browse(cr, uid, uid, context=context).company_id
        company_name = obj_company.partner_id.name

        lang_ids = res_lang_obj.search(cr, uid, [('code','=',context.get('lang'))])
        if len(lang_ids) == 1 :
            lang = res_lang_obj.browse(cr, uid, lang_ids[0])
            format = lang.date_format

        data = {
            'company_name' : str(company_name),
            'user' : user,
            'database' : db,
            'date_print' : time.strftime(format),
        }
        return data



report_sxw.report_sxw('report.users.active',
                       'users.active',
                       'addons/users_statistics/report/users_by_month.mako',
                       parser=report_parser)