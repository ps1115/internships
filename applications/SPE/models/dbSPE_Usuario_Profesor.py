# -*- coding: utf-8 -*-

# Estudiante
dbSPE.define_table('usuario_profesor',
                Field('usbid_usuario','string',required=True, requires=[IS_LENGTH(524),IS_NOT_EMPTY(error_message='Campo Obligatorio'),IS_NOT_IN_DB(dbSPE, 'estudiante.usbid_usuario',error_message=T('Login No Disponible'))], ondelete='CASCADE', notnull=True, unique=True,label='Login'),
                Field('dependencia','integer', requires=[IS_LENGTH(11)]),
                Field('dedicacion','integer', requires=[IS_LENGTH(11)]),
                Field('categoria','integer', requires=[IS_LENGTH(11)]),
                Field('email_sec','string',required=True, requires=[IS_LENGTH(254)]),
                Field('telef','string', requires=[IS_LENGTH(20),IS_MATCH('^\+[0-9]*$|^[0-9]*$',error_message=T('Solo se permiten numeros y el signo +'))]),
                Field('celular','string', requires=[IS_LENGTH(20),IS_MATCH('^\+[0-9]*$|^[0-9]*$',error_message=T('Solo se permiten numeros y el signo +'))]),
                Field('activo','boolean',default=False),
                primarykey=['usbid_usuario'],
                format='%(carnet)s'
               )
