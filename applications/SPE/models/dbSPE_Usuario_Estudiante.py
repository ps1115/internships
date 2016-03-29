# -*- coding: utf-8 -*-

# Estudiante
dbSPE.define_table('usuario_estudiante',
                Field('usbid_usuario','string',required=True, requires=[IS_LENGTH(524),IS_NOT_EMPTY(error_message='Campo Obligatorio'),IS_NOT_IN_DB(dbSPE, 'usuario_estudiante.usbid_usuario',error_message=T('Usuario ya existe'))], ondelete='CASCADE', notnull=True, unique=True,label='Nombre de Usuario'),
                Field('carnet','string',required=True, requires=[IS_LENGTH(8),IS_MATCH('[0-9]{2}-[0-9]{5}',error_message=T('Solo se permiten numeros y el signo +'))], label="Carnet", unique=True),
                Field('cohorte', requires=[IS_LENGTH(2),IS_NOT_EMPTY(error_message='Ingrese cohorte')], label="Cohorte"),
                Field('carrera','string',represent=lambda x, row: (dbSPE(dbSPE.carrera.codigo==x)).select().first().nombre, requires=IS_IN_DB(dbSPE,'carrera.codigo', '%(nombre)s',error_message='Carrera no Existe'),label="Carrera"),
                Field('estudiante_sede','string', requires=IS_IN_SET(["Sartenejas","Litoral"]), label="Sede"),
                Field('email_sec','string',required=True, requires=[IS_LENGTH(254),IS_EMAIL('Correo Electrónico Inválido')],label="Correo Electrónico"),
                Field('telf_hab','string', requires=[IS_LENGTH(20),IS_MATCH('^\+[0-9]*$|^[0-9]*$',error_message=T('Solo se permiten numeros y el signo +'))],label="Teléfono de Habitación"),
                Field('telf_cel','string', requires=[IS_LENGTH(20),IS_MATCH('^\+[0-9]*$|^[0-9]*$',error_message=T('Solo se permiten numeros y el signo +'))], label="Teléfono Celular"),
                Field('direccion','text', label="Dirección de Habitación"),
                Field('sexo','string', requires=IS_IN_SET(['M','F']), label="Sexo"),
                primarykey=['usbid_usuario'],
                format='%(carnet)s'
                )
