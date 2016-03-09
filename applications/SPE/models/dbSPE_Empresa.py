# -*- coding: utf-8 -*-

# Empresa
dbSPE.define_table('empresa',
                Field('loginID','string',required=True, requires=[IS_LENGTH(512),IS_NOT_EMPTY(error_message='Campo Obligatorio'),IS_NOT_IN_DB(dbSPE, 'empresa.loginID',error_message=T('Login No Disponible'))], ondelete='CASCADE', notnull=True, unique=True,label='Login'),
                Field('password','password', required=True, notnull=True,label=T('Contraseña'),requires=[IS_LENGTH(512),IS_NOT_EMPTY(error_message=T('Campo Obligatorio'))]),
                Field('pregunta_secreta','string',label=T('Pregunta Secreta'),requires=[IS_LENGTH(512),IS_NOT_EMPTY(error_message='Campo Obligatorio')]),
                Field('respuesta_pregunta_secreta','string',label=T('Respuesta A Pregunta Secreta'),requires=[IS_LENGTH(512),IS_NOT_EMPTY(error_message=T('Campo Obligatorio'))]),
                Field('nombre','string',required=True, notnull=True,label=T('Nombre De La Empresa'),requires=[IS_LENGTH(512),IS_NOT_EMPTY(error_message=T('Campo Obligatorio'))]),
                Field('direccion','text',label=T('Direccion De La Empresa')),
                Field('pag_web','string',label=T('Pagina Web')),
                Field('descripcion','text',label=T('Descripcion De La Empresa')),
                Field('telefono','string',label=T('Telefono'), requires=[IS_MATCH('^\+[0-9]*$|^[0-9]*$',error_message=T('Solo se permiten numeros y el signo +'))]),
                Field('contacto_RRHH','string',required=True,notnull=True,requires=[IS_EMAIL(error_message=T('Este no es un correo valido')),IS_NOT_EMPTY(error_message='Campo Obligatorio'),IS_LENGTH(512)],label=T('Contacto De Recursos Humanos')),
                Field('intentos','integer',default=0,label=T('Intentos')),
                Field('habilitado','integer',default=1,requires = [IS_INT_IN_RANGE(0, 2)],label='Habilitado'),
                Field('fechaCreacion','datetime',label=T('Fecha De Creacion')),
                Field('ultimaModificacion','datetime',label=T('Fecha De Ultima Modificacion')),
                format='%(nombre)s %(loginID)s',
                primarykey=['loginID']
               )
