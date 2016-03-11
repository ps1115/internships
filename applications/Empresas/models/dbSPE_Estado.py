# -*- coding: utf-8 -*-

'''
    `nombre`    varchar(40) NOT NULL,
    `id_zona`   int(11)     NOT NULL,
'''

dbSPE.define_table('pais',
                Field('nombre','string',required=True,ondelete='CASCADE',
                    notnull=True, unique=True,label='Pais'),format='%(nombre)s')

dbSPE.pais.nombre.requires=[IS_NOT_EMPTY(error_message='Campo Obligatorio')]
dbSPE.pais.nombre.requires+=[IS_LENGTH(512)]
dbSPE.pais.nombre.requires+=[IS_NOT_IN_DB(dbSPE, 'pais.nombre',error_message=T('Pais ya registrado'))]

dbSPE.define_table('estado',
                Field('nombre','string',required=True, ondelete='CASCADE', notnull=True, unique=True,label='Nombre'),
                Field('id_pais','reference pais', required=True, notnull=True,label=T('id_Pais')),format='%(nombre)s')

dbSPE.estado.nombre.requires=[IS_NOT_EMPTY(error_message='Campo Obligatorio')]
dbSPE.estado.nombre.requires+=[IS_LENGTH(512)]

dbSPE.estado.id_pais.requires=[IS_NOT_EMPTY(error_message='Campo Obligatorio')]
dbSPE.estado.id_pais.requires+=[IS_LENGTH(512)]
dbSPE.estado.id_pais.requires+=[IS_IN_DB(dbSPE,dbSPE.pais.id,'%(nombre)s')]
