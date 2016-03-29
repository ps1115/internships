# -*- coding: utf-8 -*-

# Actividad
dbSPE.define_table('actividad',
                Field('id','id', requires=[IS_LENGTH(11)]),
                Field('codigo_fase','integer'),
                Field('descripcion','text',required=True),
                Field('tiempo_estimado','string',required=True, requires=[IS_LENGTH(20)]),
                Field('id_plan_de_trab','integer',required=True),
                primarykey=['id'],
                format='%(id)s  %(codigo_fase)s  %(descripcion)s  %(tiempo_estimado)s  %(id_plan_de_trab)s'
               )

