# -*- coding: utf-8 -*-

# Tutor Industrial
dbSPE.define_table('tutor_industrial',
                   Field('email','string',required=True, requires=[
            IS_EMAIL(error_message=T('Este no es un correo valido')),
            IS_LENGTH(512),
            IS_NOT_EMPTY(error_message='Campo Obligatorio')],
                         ondelete='CASCADE', label='Correo Electronico'),
                   Field('nombre','string',label=T('Nombre'),requires=[
            IS_LENGTH(512),IS_NOT_EMPTY(error_message='Campo Obligatorio')]),
                   Field('apellido','string',label=T('Apellido'),requires=[
            IS_LENGTH(512),IS_NOT_EMPTY(error_message='Campo Obligatorio')]),
                   Field('ci','string',label=T('Cedula de Identidad'),requires=[
            IS_LENGTH(512),IS_NOT_EMPTY(error_message='Campo Obligatorio')]),
                Field('password','password', required=True, notnull=True,label=T('Contraseña'),requires=[
            IS_LENGTH(512),
            IS_NOT_EMPTY(error_message=T('Campo Obligatorio'))
        ]),
                Field('pregunta_secreta','string',label=T('Pregunta Secreta'),requires=[
            IS_LENGTH(512),
            IS_NOT_EMPTY(error_message='Campo Obligatorio')
        ]),
                Field('respuesta_pregunta_secreta','string',label=T('Respuesta A Pregunta Secreta'),requires=[IS_LENGTH(512),IS_NOT_EMPTY(error_message=T('Campo Obligatorio'))]),
                Field('id_empresa','reference empresa',required=True, notnull=True,label=T('Login De La Empresa'),requires=[
            IS_LENGTH(512),
            IS_NOT_EMPTY(error_message=T('Campo Obligatorio')),
            IS_IN_DB(dbSPE,dbSPE.empresa.id,'%(log)s')
                      ],writable = False,readable=False),
                Field('profesion','string',label=T('Profesion que ejerce')),
                Field('departamento','string',label=T('Departamento Donde Trabaja')),
                Field('direccion','text',label=T('Descripcion De La Empresa')),
                Field('id_estado','integer',label=T('Estado')),
                Field('telefono','string',label=T('Telefono'), requires=[IS_MATCH('^\+[0-9]*$|^[0-9]*$',error_message=T('Solo se permiten numeros y el signo +'))]),
                format='%(email)s %(nombre)s %(apellido)s')
