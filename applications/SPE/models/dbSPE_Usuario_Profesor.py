# -*- coding: utf-8 -*-
# Estudiante
dbSPE.define_table('usuario_profesor',
                Field('usbid_usuario','string', requires=[IS_NOT_EMPTY(), IS_MATCH('[0-9][0-9]-[0-9]{5}','USBID Inválido'),IS_NOT_IN_DB(dbSPE, 'usuario_profesor.usbid_usuario',error_message=T('Usuario ya existe'))], label='USBID', ondelete='CASCADE', notnull=True,unique=True),
                Field('dependencia','reference departamento', represent=lambda x, row: (dbSPE(dbSPE.departamento.id==x)).select().first().nombre,label='Dependencia'),
                Field('dedicacion','reference dedicacion',represent=lambda x, row: (dbSPE(dbSPE.dedicacion.id==x)).select().first().nombre,  label='Dedicación'),
                Field('categoria','reference categoria',represent=lambda x, row: (dbSPE(dbSPE.categoria.id==x)).select().first().nombre,  label='Categoría'),
                Field('email_sec', 'string',requires=[IS_NOT_EMPTY(), IS_EMAIL(error_message='Correo Electrónico Inválido')], label='Correo Electrónico'),
                Field('telf', 'string',requires=[IS_LENGTH(20)], label='Teléfono de Habitación'),
                Field('celular', 'string',requires=[IS_LENGTH(20)], label='Teléfono Celular'),
                Field('activo', 'integer',represent=lambda x, row: (dict({1:"Activo",0:"No Activo"}))[x],requires=IS_IN_SET({1:'activo',0:'no activo'}), default='1', label='Activo'),
                primarykey=['usbid_usuario'],
                format='%(usbid_usuario)s')

dbSPE.usuario_profesor.usbid_usuario.readable = True
dbSPE.usuario_profesor.usbid_usuario.writable = True

dbSPE.usuario_profesor.activo.readable = False
dbSPE.usuario_profesor.activo.writable = False

dbSPE.usuario_profesor.dependencia.requires=IS_IN_DB(dbSPE,dbSPE.departamento.id,'%(nombre)s - %(sede)s',zero=None)

dbSPE.usuario_profesor.dedicacion.requires=IS_IN_DB(dbSPE,dbSPE.dedicacion.id,'%(nombre)s',zero=None)

dbSPE.usuario_profesor.categoria.requires=IS_IN_DB(dbSPE,dbSPE.categoria.id,'%(nombre)s',zero=None)


dbSPE.usuario_profesor.telf.requires+=[IS_MATCH('^\+[0-9]*$|^[0-9]*$',error_message=T('Solo se permiten numeros y el signo +'))]
dbSPE.usuario_profesor.celular.requires+=[IS_MATCH('^\+[0-9]*$|^[0-9]*$',error_message=T('Solo se permiten numeros y el signo +'))]
