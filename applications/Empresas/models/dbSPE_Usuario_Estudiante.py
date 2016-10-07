# -*- coding: utf-8 -*-

# Estudiante
dbSPE.define_table('usuario_estudiante',
                Field('usbid_usuario','string',required=True, requires=[IS_LENGTH(524),IS_NOT_EMPTY(error_message='Campo Obligatorio'),IS_NOT_IN_DB(dbSPE, 'estudiante.usbid_usuario',error_message=T('Login No Disponible'))], ondelete='CASCADE', notnull=True, unique=True,label='Login'),
                Field('carnet','string',required=True, requires=[IS_LENGTH(8)]),
                Field('cohorte','string', requires=[IS_LENGTH(2)]),
                Field('carrera','string', requires=[IS_LENGTH(4)]),
                Field('estudiante_sede','string', requires=[IS_LENGTH(11)]),
                Field('email_sec','string',required=True, requires=[IS_LENGTH(254)]),
                Field('telf_hab','string', requires=[IS_LENGTH(20),IS_MATCH('^\+[0-9]*$|^[0-9]*$',error_message=T('Solo se permiten numeros y el signo +'))]),
                Field('telf_cel','string', requires=[IS_LENGTH(20),IS_MATCH('^\+[0-9]*$|^[0-9]*$',error_message=T('Solo se permiten numeros y el signo +'))]),
                Field('direccion','text'),
                Field('estudiante_sede','string', requires=[IS_LENGTH(1)]),
                primarykey=['usbid_usuario'],
                format='%(carnet)s'
               )
