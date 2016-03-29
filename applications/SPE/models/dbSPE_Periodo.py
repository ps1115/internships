# -*- coding: utf-8 -*-

# Estudiante
'''
dbSPE.define_table('periodo',
                Field('id','id',required=True, requires=[IS_LENGTH(10),IS_NOT_EMPTY(error_message='Campo Obligatorio'),IS_NOT_IN_DB(dbSPE, 'carrera.codigo',error_message=T('Carrera no disponible'))], ondelete='CASCADE', notnull=True, unique=True,label='Carrera'),
                Field('nombre','string',required=True, requires=[IS_LENGTH(100)]),
                Field('fecha_inicio', 'datetime',required=True),
                Field('fecha_fin', 'datetime',required=True),
                Field('periodo_activo', 'integer',required=True),
                primarykey=['id'],
                format='%(nombre)s'
               )
'''
