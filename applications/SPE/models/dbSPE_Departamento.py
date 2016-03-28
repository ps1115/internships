# -*- coding: utf-8 -*-

# Departamento
dbSPE.define_table('departamento',
                Field('nombre','string',required=True, default='',label="Nombre del Departamento"),
                Field('id_division','reference division',required=True,label='División'),
                Field('email_dep','string',required=True,label='Correo Electrónico del Departamento'),
                Field('sede','string',required=True,label='Sede', default='Sartenejas'),
                format='%(nombre)s - %(sede)s'
               )

# Validadores
dbSPE.departamento.email_dep.requires+=[IS_LENGTH(100)]
dbSPE.departamento.email_dep.requires+=[IS_NOT_EMPTY(error_message='Campo Obligatorio')]

dbSPE.departamento.email_dep.requires=[IS_EMAIL(error_message=T('Este no es un correo valido'))]
dbSPE.departamento.email_dep.requires+=[IS_LENGTH(100)]
dbSPE.departamento.email_dep.requires+=[IS_NOT_EMPTY(error_message='Campo Obligatorio')]

dbSPE.departamento.email_dep.requires=IS_IN_SET(['Sartenejas','Litoral'])
