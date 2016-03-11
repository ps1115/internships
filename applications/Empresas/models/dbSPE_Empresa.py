# -*- coding: utf-8 -*-

# Empresa
dbSPE.define_table('empresa',
                Field('log','string',required=True, ondelete='CASCADE', notnull=True, unique=True,label='Login'),
                Field('password','password', required=True, notnull=True,label=T('Contraseña')),
                Field('pregunta_secreta','string',label=T('Pregunta Secreta')),
                Field('respuesta_pregunta_secreta','string',label=T('Respuesta A Pregunta Secreta')),
                Field('nombre','string',required=True, notnull=True,label=T('Nombre')),
                Field('id_pais','reference pais',label=T('Pais')),
                Field('id_estado','reference estado',label=T('Estado')),
                Field('direccion','text',label=T('Direccion De La Empresa')),
                Field('pag_web','string',label=T('Pagina Web')),
                Field('descripcion','text',label=T('Descripcion De La Empresa')),
                Field('telefono','string',label=T('Telefono')),
                Field('contacto_RRHH','string',required=True,notnull=True,label=T('Contacto De Recursos Humanos')),
                Field('intentos','integer',default=0,label=T('Intentos')),
                Field('habilitado','integer',default=1,label='Habilitado'),
                Field('fechaCreacion','datetime',label=T('Fecha De Creacion')),
                Field('ultimaModificacion','datetime',label=T('Fecha De Ultima Modificacion')),
                format='%(nombre)s %(log)s'
               )

# Validadores

dbSPE.empresa.log.requires=[IS_EMAIL(error_message=T('Este no es un correo valido'))]
dbSPE.empresa.log.requires+=[IS_LENGTH(512)]
dbSPE.empresa.log.requires+=[IS_NOT_EMPTY(error_message='Campo Obligatorio')]
dbSPE.empresa.log.requires+=[IS_NOT_IN_DB(dbSPE, 'empresa.log',error_message=T('Login No Disponible'))]


dbSPE.empresa.password.requires=[IS_LENGTH(512)]
dbSPE.empresa.password.requires+=[IS_NOT_EMPTY(error_message='Campo Obligatorio')]

dbSPE.empresa.pregunta_secreta.requires=[IS_LENGTH(512)]
dbSPE.empresa.pregunta_secreta.requires+=[IS_NOT_EMPTY(error_message='Campo Obligatorio')]

dbSPE.empresa.respuesta_pregunta_secreta.requires=[IS_LENGTH(512)]
dbSPE.empresa.respuesta_pregunta_secreta.requires+=[IS_NOT_EMPTY(error_message='Campo Obligatorio')]

dbSPE.empresa.nombre.requires=[IS_LENGTH(512)]
dbSPE.empresa.nombre.requires+=[IS_NOT_EMPTY(error_message=T('Campo Obligatorio'))]

dbSPE.empresa.id_estado.requires=IS_IN_DB(dbSPE,dbSPE.estado.id,'%(nombre)s',error_message=T('Elija Un Estado Valido'),zero=None)

dbSPE.empresa.id_pais.requires=IS_IN_DB(dbSPE,dbSPE.pais.id,'%(nombre)s',error_message=T('Elija Un Pais Valido'),zero=None)


dbSPE.empresa.pregunta_secreta.requires=[IS_LENGTH(512)]
dbSPE.empresa.pregunta_secreta.requires+=[IS_NOT_EMPTY(error_message='Campo Obligatorio')]

dbSPE.empresa.respuesta_pregunta_secreta.requires=[IS_LENGTH(512)]
dbSPE.empresa.respuesta_pregunta_secreta.requires+=[IS_NOT_EMPTY(error_message='Campo Obligatorio')]


dbSPE.empresa.contacto_RRHH.requires=[IS_LENGTH(512)]
dbSPE.empresa.contacto_RRHH.requires+=[IS_EMAIL(error_message=T('Este no es un correo valido'))]
dbSPE.empresa.contacto_RRHH.requires+=[IS_NOT_EMPTY(error_message='Campo Obligatorio')]


dbSPE.empresa.habilitado.requires=[IS_INT_IN_RANGE(0, 2)]

dbSPE.empresa.telefono.requires=[IS_LENGTH(512)]
dbSPE.empresa.telefono.requires+=[IS_MATCH('^\+[0-9]*$|^[0-9]*$',error_message=T('Solo se permiten numeros y el signo +'))]
