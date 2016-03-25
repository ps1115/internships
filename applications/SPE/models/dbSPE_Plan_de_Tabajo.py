# -*- coding: utf-8 -*-

# Plan de Trabajo
dbSPE.define_table('plan_de_trabajo',
                Field('id','integer',required=True),
                Field('id_estudiante','string',required=True, requires=[IS_LENGTH(8)]),
                Field('id_tutor_industrial','string',required=True, requires=[IS_LENGTH(254)]),
                Field('id_tutor_academico','string',required=True, requires=[IS_LENGTH(254)]),
                Field('log_empresa','string',required=True, requires=[IS_LENGTH(254)]),
                Field('codigo_pasantia','string',required=True, requires=[IS_LENGTH(8)]),
                primarykey=['id'],
                format='%(id)s  %(id_estudiante)s  %(id_tutor_industrial)s  %(id_tutor_academico)s  %(log_empresa)s  %(codigo_pasantia)s'
               )
