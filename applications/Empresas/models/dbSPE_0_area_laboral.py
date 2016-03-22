'''
    `id`            int(11)         NOT NULL AUTO_INCREMENT,
    `nombre`        varchar(254)    NOT NULL,
    `descripcion`   text,
'''

dbSPE.define_table('area_laboral',
                Field('nombre','string',required=True,ondelete='CASCADE',
                    notnull=True, unique=True,label='Area Laboral'),
                Field('descripcion','text', required=True, notnull=True,label=T('Descripcion del Area Laboral')),
                format='%(nombre)s')

dbSPE.area_laboral.nombre.requires=[IS_NOT_EMPTY(error_message='Campo Obligatorio')]
dbSPE.area_laboral.nombre.requires+=[IS_LENGTH(512)]
dbSPE.area_laboral.nombre.requires+=[IS_NOT_IN_DB(dbSPE, 'area_laboral.nombre',error_message=T('Area Laboral ya registrado'))]
