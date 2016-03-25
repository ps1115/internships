# -*- coding: utf-8 -*-

# Fase
dbSPE.define_table('fase',
                Field('codigo','integer',required=True),
                Field('id_periodo','integer'),
                Field('id_estudiante','string',required=True, requires=[IS_LENGTH(254)]),
                Field('codigo_pasantia','string',required=True, requires=[IS_LENGTH(8)]),
                Field('nombre_fase','string',required=True, requires=[IS_LENGTH(100)]),
                Field('objetivos_especificos','text',required=True),
                primarykey=['codigo'],
                format='%(codigo)s  %(id_periodo)s  %(id_estudiante)s  %(codigo_pasantia)s  %(nombre_fase)s  %(objetivos_especificos)s'
               )

