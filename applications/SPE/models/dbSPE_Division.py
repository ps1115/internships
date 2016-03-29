# -*- coding: utf-8 -*-
'''
# Division
dbSPE.define_table('division',
                Field('nombre','string',required=True),
                format='%(nombre)s'
               )

dbSPE.division.nombre.requires+=[IS_LENGTH(100)]
dbSPE.division.nombre.requires+=[IS_NOT_EMPTY(error_message='Campo Obligatorio')]
'''
