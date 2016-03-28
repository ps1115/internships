# -*- coding: utf-8 -*-

# Plan de Trabajo
dbSPE.define_table('plan_de_trabajo',
                Field('id','id',requires=[IS_LENGTH(11)]),
                Field('id_estudiante','string',required=True, requires=[IS_LENGTH(8)]),
                Field('id_tutor_industrial','string', requires=[IS_LENGTH(254)]),
                Field('id_tutor_academico','string', requires=[IS_LENGTH(254)]),
                Field('codigo_pasantia','string', requires=[IS_LENGTH(8)]),
                primarykey=['id'],
                format='%(id)s  %(id_estudiante)s  %(id_tutor_industrial)s  %(id_tutor_academico)s  %(codigo_pasantia)s'
               )
