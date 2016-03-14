# -*- coding: utf-8 -*-

# Estudiante
dbSPE.define_table('pais',
                Field('id','id',required=True, requires=[IS_LENGTH(2)]),
                Field('nombre','string',required=True, requires=[IS_LENGTH(10)]),
                primarykey=['id'],
                format='%(nombre)s'
               )
