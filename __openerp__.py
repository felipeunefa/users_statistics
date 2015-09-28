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
{
    "name" : "Users Statistics Module",
    "version" : "0.1",
    "author" : "Eezee-It",
    "category" : "Reporting",
    "website": "http://www.eezee-it.com",
    "description": """
Users Statistics
==================
This module allows to display statistics about users of the system.

    * All connections with the number of OpenERP request during this connection.

    * Each month a scheduler is launched to compute the number of active users in this database.

    * You can print a report file of active users by month.



**Path to access :** Reporting/Users Statistics

    """,
    "depends" : ["base","report_webkit"],
    "init" : [],
    "demo" : [],
    "data" : [
        'security/users_stat_groups.xml',
        'security/ir.model.access.csv',
        # ========== VIEW ==========
        'view/user_connection_view.xml',
        'view/users_active_view.xml',
        'view/scheduler_user_active.xml',
        'view/users_last_access_view.xml',
        # ========== REPORT ==========
        "report/data.xml",
        "report/report_users_by_month.xml",
        ],
    "active": False,
    "installable": True,
    'images':['images/users_stat_01.PNG','images/users_stat_01.PNG'],
}
