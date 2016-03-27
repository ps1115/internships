# -*- coding: utf-8 -*-

# Estudiante
dbSPE.define_table('usuario_profesor',
                Field('usbid_usuario', requires=[IS_NOT_EMPTY(), IS_MATCH('[0-9][0-9]-[0-9]{5}','USBID Inválido')], label='USBID', unique=True),
                Field('dependencia', requires=[IS_NOT_EMPTY()], label='Dependencia'),
                Field('dedicacion', requires=[IS_NOT_EMPTY()], label='Dedicación'),
                Field('categoria', requires=[IS_NOT_EMPTY()], label='Categoría'),
                Field('email_sec', requires=[IS_NOT_EMPTY(), IS_EMAIL(error_message='Correo Electrónico Inválido')], label='Correo Electrónico'),
                Field('telf', requires=[IS_NOT_EMPTY()], label='Teléfono de Habitación'),
                Field('celular', requires=[IS_NOT_EMPTY()], label='Teléfono Celular'),
                Field('activo', requires=[IS_NOT_EMPTY(), IS_IN_SET(['0','1'],error_message='Valor no Permitido')], default='1', label='Activo'),
                primarykey=['usbid_usuario'],
                format='%(carnet)s'
                )

dbSPE.usuario_profesor.usbid_usuario.readable = True
dbSPE.usuario_profesor.usbid_usuario.writable = False

dbSPE.usuario_profesor.usbid_usuario.activo = True
dbSPE.usuario_profesor.usbid_usuario.activo = False

dbSPE.usuario_profesor.telf.requires+=[IS_MATCH('^\+[0-9]*$|^[0-9]*$',error_message=T('Solo se permiten numeros y el signo +'))]
dbSPE.usuario_profesor.celular.requires+=[IS_MATCH('^\+[0-9]*$|^[0-9]*$',error_message=T('Solo se permiten numeros y el signo +'))]
