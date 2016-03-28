# -*- coding: utf-8 -*-

# Fase
dbSPE.define_table('fase',
                Field('codigo','id'),
                Field('id_plan_de_trab','string',required=True, requires=[IS_LENGTH(254)]),
                Field('codigo_pasantia','string', requires=[IS_LENGTH(8)]),
                Field('nombre_fase','string',required=True, requires=[IS_LENGTH(100)]),
                Field('objetivos_especificos','text',required=True),
                primarykey=['codigo'],
                format='%(codigo)s  %(id_plan_de_trab)s  %(codigo_pasantia)s  %(nombre_fase)s  %(objetivos_especificos)s'
               )

