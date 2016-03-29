# -*- coding: utf-8 -*-

# Actividad
dbSPE.define_table('coordinacion',
                Field('nombre','string',required=True),
                Field('usbid','string',required=True),
                Field('sede','string',required=True, requires=[IS_LENGTH(20)]),
                format='%(sede)s - %(nombre)s'
               )

dbSPE.coordinacion.usbid.requires+=[IS_NOT_IN_DB(dbSPE, 'coordinacion.usbid',error_message=T('Universidad ya registrado'))]
