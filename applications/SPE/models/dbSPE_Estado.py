# -*- coding: utf-8 -*-

'''
    `nombre`    varchar(40) NOT NULL,
    `id_zona`   int(11)     NOT NULL,
'''

dbSPE.define_table('zona',
                Field('nombre','string',required=True,
                      requires=[
            IS_LENGTH(512),
            IS_NOT_EMPTY(error_message='Campo Obligatorio'),
            IS_NOT_IN_DB(dbSPE, 'zona.nombre',error_message=T('Pais ya registrado'))
        ],
                      ondelete='CASCADE', notnull=True, unique=True,label='Pais'),
                format='%(nombre)s')

dbSPE.define_table('estado',
                Field('nombre','string',required=True, requires=[IS_LENGTH(512),IS_NOT_EMPTY(error_message='Campo Obligatorio'),IS_NOT_IN_DB(dbSPE, 'empresa.log',error_message=T('Login No Disponible'))], ondelete='CASCADE', notnull=True, unique=True,label='Nombre'),
                Field('id_zona','reference zona', required=True, notnull=True,label=T('id_Pais'),requires=[IS_LENGTH(512),IS_NOT_EMPTY(error_message=T('Campo Obligatorio')),IS_IN_DB(dbSPE,dbSPE.zona.id,'%(nombre)s')]) ,format='%(nombre)s')
