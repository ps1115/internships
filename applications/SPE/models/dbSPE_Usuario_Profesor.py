# -*- coding: utf-8 -*-
dbSPE.define_table('dedicacion', Field('nombre'))
dbSPE.define_table('categoria', Field('nombre'))
# Estudiante
dbSPE.define_table('usuario_profesor',
                Field('usbid_usuario','string',required=True, requires=[IS_LENGTH(524),IS_NOT_EMPTY(error_message='Campo Obligatorio'),IS_NOT_IN_DB(dbSPE, 'usuario_profesor.usbid_usuario',error_message=T('Usuario ya existe'))], ondelete='CASCADE', notnull=True, unique=True,label='USBID de Usuario'),
                Field('dependencia','integer',represent=lambda x, row: (dbSPE(dbSPE.departamento.id==x)).select().first().nombre, requires=IS_IN_DB(dbSPE,'departamento.id', '%(nombre)s',error_message='Departamento no existe'),label="Dependencia"),
                Field('dedicacion','integer',represent=lambda x, row: (dbSPE(dbSPE.dedicacion.id==x)).select().first().nombre, requires=IS_IN_DB(dbSPE,'dedicacion.id', '%(nombre)s',error_message='Dedicación no existe'),label="Dedicación"),
                Field('categoria','integer', represent=lambda x, row: (dbSPE(dbSPE.categoria.id==x)).select().first().nombre,requires=IS_IN_DB(dbSPE,'categoria.id', '%(nombre)s',error_message='Categoria no existe'),label="Categoría"),
                Field('email_sec','string',required=True, requires=[IS_LENGTH(254)],label="Correo Electrónico Secundario"),
                Field('telf','string', requires=[IS_LENGTH(20),IS_MATCH('^\+[0-9]*$|^[0-9]*$',error_message=T('Solo se permiten numeros y el signo +'))],label="Teléfono de Habitación"),
                Field('celular','string', requires=[IS_LENGTH(20),IS_MATCH('^\+[0-9]*$|^[0-9]*$',error_message=T('Solo se permiten numeros y el signo +'))], label="Teléfono Celular"),
                Field('activo','integer',represent=lambda x, row: (dict({1:"Activo",0:"No Activo"}))[x],requires=IS_IN_SET({1:'activo',0:'no activo'}),default=False, label="Situación"),
                primarykey=['usbid_usuario'],
                format='%(carnet)s'
               )
