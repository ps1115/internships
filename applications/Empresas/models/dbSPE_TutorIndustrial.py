# -*- coding: utf-8 -*-

# Tutor Industrial
dbSPE.define_table('tutor_industrial',
                    Field('email','string',required=True,ondelete='CASCADE', label='Correo Electronico'),
                    Field('nombre','string',label=T('Nombre')),
                    Field('apellido','string',label=T('Apellido'),),
                    Field('ci','string',label=T('Cedula de Identidad')),
                    Field('password','password', required=True, notnull=True,label=T('Contraseña')),
                    Field('pregunta_secreta','string',label=T('Pregunta Secreta')),
                    Field('respuesta_pregunta_secreta','string',label=T('Respuesta A Pregunta Secreta'),requires=[IS_LENGTH(512),IS_NOT_EMPTY(error_message=T('Campo Obligatorio'))]),
                    Field('id_empresa','reference empresa',required=True, notnull=True,label=T('Empresa')),
                    Field('profesion','string',label=T('Profesion')),
                    Field('cargo','string',label=T('Cargo')),
                    Field('departamento','string',label=T('Departamento')),
                    Field('direccion','text',label=T('Direccion Del tutor')),
                    Field('id_pais','reference pais',label=T('Pais')),
                    Field('id_estado','reference estado',label=T('Estado')),
                    Field('telefono','string',label=T('Telefono')),
                    format='%(email)s %(nombre)s %(apellido)s')

# Validadores

dbSPE.tutor_industrial.email.requires=[IS_EMAIL(error_message=T('Este no es un correo valido'))]
dbSPE.tutor_industrial.email.requires+=[IS_LENGTH(512)]
dbSPE.tutor_industrial.email.requires+=[IS_NOT_EMPTY(error_message='Campo Obligatorio')]

dbSPE.tutor_industrial.nombre.requires=[IS_LENGTH(512)]
dbSPE.tutor_industrial.nombre.requires+=[IS_NOT_EMPTY(error_message='Campo Obligatorio')]

dbSPE.tutor_industrial.apellido.requires=[IS_LENGTH(512)]
dbSPE.tutor_industrial.apellido.requires+=[IS_NOT_EMPTY(error_message='Campo Obligatorio')]

dbSPE.tutor_industrial.ci.requires=[IS_LENGTH(512)]
dbSPE.tutor_industrial.ci.requires+=[IS_NOT_EMPTY(error_message='Campo Obligatorio')]

dbSPE.tutor_industrial.password.requires=[IS_LENGTH(512)]
dbSPE.tutor_industrial.password.requires+=[IS_NOT_EMPTY(error_message=T('Campo Obligatorio'))]

dbSPE.tutor_industrial.pregunta_secreta.requires=[IS_LENGTH(512)]
dbSPE.tutor_industrial.pregunta_secreta.requires+=[IS_NOT_EMPTY(error_message='Campo Obligatorio')]

dbSPE.tutor_industrial.respuesta_pregunta_secreta.requires=[IS_LENGTH(512)]
dbSPE.tutor_industrial.respuesta_pregunta_secreta.requires+=[IS_NOT_EMPTY(error_message='Campo Obligatorio')]

dbSPE.tutor_industrial.id_empresa.requires=IS_IN_DB(dbSPE,dbSPE.empresa.id,'%(log)s - %(nombre)s',error_message=T('Elija Una Empresa Valida'),zero=None)

dbSPE.tutor_industrial.id_estado.requires=IS_IN_DB(dbSPE,dbSPE.estado.id,'%(nombre)s',error_message=T('Elija Un Estado Valido'),zero=None)

dbSPE.tutor_industrial.id_pais.requires=IS_IN_DB(dbSPE,dbSPE.pais.id,'%(nombre)s',error_message=T('Elija Un Pais Valido'),zero=None)

dbSPE.tutor_industrial.telefono.requires=[IS_LENGTH(512)]
dbSPE.tutor_industrial.telefono.requires+=[IS_MATCH('^\+[0-9]*$|^[0-9]*$',error_message=T('Solo se permiten numeros y el signo +'))]
