# -*- coding: utf-8 -*-

# Estudiante
dbSPE.define_table('carrera',
                Field('codigo','string',required=True, requires=[IS_LENGTH(4),IS_NOT_EMPTY(error_message='Campo Obligatorio'),IS_NOT_IN_DB(dbSPE, 'carrera.codigo',error_message=T('Carrera no disponible'))], ondelete='CASCADE', notnull=True, unique=True,label='Carrera'),
                Field('nombre','string',required=True, requires=[IS_LENGTH(100)]),
                Field('duracion','string',required=True, requires=[IS_LENGTH(11)]),
                Field('sede','string', requires=[IS_LENGTH(20)]),
                Field('coordinacion','string', requires=[IS_LENGTH(100)]),
                Field('id','integer', requires=[IS_LENGTH(20)]),
                primarykey=['codigo'],
                format='%(codigo)s %(nombre)s'
               )
