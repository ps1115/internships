# -*- coding: utf-8 -*-

# Dedicacion
dbSPE.define_table('dedicacion',
                Field('nombre','string',required=True),
                format='%(nombre)s'
               )

dbSPE.dedicacion.nombre.requires+=[IS_LENGTH(100)]
dbSPE.dedicacion.nombre.requires+=[IS_NOT_EMPTY(error_message='Campo Obligatorio')]
