'''
    `id`        int(11)         NOT NULL AUTO_INCREMENT,
    `nombre`    varchar(254)    NOT NULL,
    `id_pais`   int(11)         NOT NULL,
'''

dbSPE.define_table('universidad',
                Field('nombre','string',required=True,ondelete='CASCADE',
                    notnull=True, unique=True,label='Universidad'),
                Field('id_pais','reference pais', required=True, notnull=True,label=T('Pais')),
                format='%(nombre)s')

dbSPE.universidad.nombre.requires=[IS_NOT_EMPTY(error_message='Campo Obligatorio')]
dbSPE.universidad.nombre.requires+=[IS_LENGTH(512)]
dbSPE.universidad.nombre.requires+=[IS_NOT_IN_DB(dbSPE, 'universidad.nombre',error_message=T('Universidad ya registrado'))]

dbSPE.universidad.id_pais.requires=IS_IN_DB(dbSPE,dbSPE.pais.id,'%(nombre)s')
