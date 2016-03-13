# -*- coding: utf-8 -*-

# Estudiante
dbSPE.define_table('tipo_pasantia',
                Field('codigo','string',required=True, requires=[IS_LENGTH(8),IS_NOT_EMPTY(error_message='Campo Obligatorio'),IS_NOT_IN_DB(dbSPE, 'carrera.codigo',error_message=T('Carrera no disponible'))], ondelete='CASCADE', notnull=True, unique=True,label='Carrera'),
                Field('nombre','string',required=True, requires=[IS_LENGTH(100)]),
                primarykey=['codigo'],
                format='%(codigo)s %(nombre)s'
               )
