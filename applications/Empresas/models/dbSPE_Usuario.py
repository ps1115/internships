# -*- coding: utf-8 -*-

# Estudiante
dbSPE.define_table('usuario',
                Field('usbid','string',required=True, requires=[IS_LENGTH(524),IS_NOT_EMPTY(error_message='Campo Obligatorio'),IS_NOT_IN_DB(dbSPE, 'usuario.usbid',error_message=T('Login No Disponible'))], ondelete='CASCADE', notnull=True, unique=True,label='Login'),
                Field('nombre','string',required=True, requires=[IS_LENGTH(254)]),
                Field('apellido','string',required=True, requires=[IS_LENGTH(254)]),
                Field('ci','string', requires=[IS_LENGTH(8)]),
                Field('tipo','string', requires=[IS_LENGTH(15)]),
                Field('foto','blob'),
                Field('llave','string', requires=[IS_LENGTH(20)]),
                primarykey=['usbid'],
                format='%(usbid)s %(nombre)s'
               )
