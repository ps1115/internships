# -*- coding: utf-8 -*-

# Categoria
dbSPE.define_table('categoria',
                Field('nombre','string',required=True, requires=[IS_LENGTH(20)]),
                format='%(nombre)s'
               )

dbSPE.categoria.nombre.requires+=[IS_LENGTH(100)]
dbSPE.categoria.nombre.requires+=[IS_NOT_EMPTY(error_message='Campo Obligatorio')]
