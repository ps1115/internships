# -*- coding: utf-8 -*-
dbSPE = DAL('mysql://root:root@localhost:3306/pasantiasnuevo', pool_size=0,migrate=False)

dbSPE.define_table('empresa',
                Field('loginID','string',required=True, requires=[IS_LENGTH(512),IS_NOT_EMPTY(error_message='Campo Obligatorio')], ondelete='CASCADE', notnull=True, unique=True,label='Login'),
                Field('password','password', required=True, notnull=True,label='Contrasena',requires=[IS_LENGTH(512),IS_NOT_EMPTY(error_message='Campo Obligatorio')]),
                Field('pregunta_secreta','text',label='Pregunta Secreta',requires=[IS_LENGTH(65536),IS_NOT_EMPTY(error_message='Campo Obligatorio')]),
                Field('respuesta_pregunta_secreta','text',label='Respuesta A Pregunta Secreta',requires=[IS_LENGTH(65536),IS_NOT_EMPTY(error_message='Campo Obligatorio')]),
                Field('nombre','string',required=True, notnull=True,label='Nombre De La Empresa',requires=[IS_LENGTH(65536),IS_NOT_EMPTY(error_message='Campo Obligatorio')]),
                Field('direccion','text',label='Direccion De La Empresa'),
                Field('pag_web','string',label='Pagina Web'),
                Field('descripcion','text',label='Descripcion De La Empresa'),
                Field('telefono','string',label='Telefono'),
                Field('contacto_RRHH','string',required=True,notnull=True,requires=[IS_EMAIL(error_message=T('Este no es un correo valido')),IS_NOT_EMPTY(error_message='Campo Obligatorio'),IS_LENGTH(512)],label='Contacto De Recursos Humanos'),
                Field('intentos','integer',default=0,label='Intentos'),
                Field('habilitado','integer',default=1,requires = [IS_INT_IN_RANGE(0, 1)],label='Habilitado'),
                Field('fechaCreacion','datetime',label='Fecha De Creacion'),
                Field('ultimaModificacion','datetime',label='Fecha De Ultima Modificacion'),
                format='%(nombre)s %(loginID)s',
                primarykey=['loginID']
               )
