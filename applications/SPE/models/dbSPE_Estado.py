# -*- coding: utf-8 -*-

# Estudiante
dbSPE.define_table('estado',
                Field('id','id',required=True, requires=[IS_LENGTH(2)]),
                Field('nombre','string',required=True, requires=[IS_LENGTH(40)]),
                Field('id_pais','int',requires=[IS_LENGTH(4)]),
                primarykey=['id'],
                format='%(nombre)s'
               )
