# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2011 OpenERP S.A (<http://www.openerp.com>).
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

from osv import  osv,fields
from openerp import tools

class UserLastAccess(osv.Model):
	"""
		Descripcion Utilizada o Uso Objeto de Negocios
	"""
	_name='users.last_access'
	_description='Last Access of Users'
	_auto = False

	_columns = {
		'name' : fields.char('Usuario'),
		'perfil' : fields.char('Perfil'),
		'ultimo_acceso' : fields.char('Ultimo Acceso'),
		'f_login' : fields.date('Fecha Ultimo Acceso'),
		'dias' : fields.integer('Dias sin acceder')
	}

	def init(self, cr):
		
		""" Vista Usuarios Afiliados
			@param cr: the current row, from the database cursor,
		"""
		tools.drop_view_if_exists(cr, 'users_last_access')
		cr.execute("""
			create or replace view users_last_access as (
				SELECT users.id as "id" , partner.name  as "name",
				  (SELECT espec.name from delphos_salud_especialidad  espec, delphos_terceros_medico_especi medic_esp , delphos_terceros_medico med
				  WHERE medic_esp.especialidad_id = espec.id AND   medic_esp.doctor_id = med.id AND medic_esp.principal = true and med.user_id = users.id
				    LIMIT 1) as "perfil",
				  CASE
				    WHEN  DATE_PART('day', now() AT TIME ZONE 'UTC-5' - users.login_date)::INTEGER > 365
				    THEN 'Hace más de un año'
				    WHEN  DATE_PART('day', now() AT TIME ZONE 'UTC-5' - users.login_date AT TIME ZONE 'UTC-5')::INTEGER < 1
				    THEN  (SELECT 'Hace ' || EXTRACT( HOUR FROM now() - MAX(con.datetime_connection  AT TIME ZONE 'UTC-0')) || ' Horas, '  ||  EXTRACT( MINUTE FROM now() - MAX(con.datetime_connection  AT TIME ZONE 'UTC-0')) || ' Minutos' FROM users_connection con WHERE con.user_id = users.id )
				    ELSE
				    'Hace ' ||DATE_PART('day', now() AT TIME ZONE 'UTC-5' - users.login_date) || ' Días'
				  END AS "ultimo_acceso",
				  users.login_date as "f_login",
				  DATE_PART('day', now() AT TIME ZONE 'UTC-5' - users.login_date)::INTEGER as "dias"
				FROM res_users users , res_partner partner WHERE users.partner_id = partner.id AND users.active = true AND users.login_date IS NOT NULL
				  AND users.id NOT IN(25,23,26)
				ORDER BY "dias"
			)""")


UserLastAccess()
