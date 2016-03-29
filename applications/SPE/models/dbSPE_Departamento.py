# -*- coding: utf-8 -*-
'''
# Departamento
dbSPE.define_table('departamento',
                Field('nombre','string', requires=IS_NOT_EMPTY(), default='', label="Nombre del Departamento"),
                Field('id_division','reference division', represent=lambda x, row: (dbSPE(dbSPE.division.id==x)).select().first().nombre,requires=IS_IN_DB(dbSPE,'division.id', '%(nombre)s',error_message='Division no Existe'), notnull=True, label='Nombre de División'),
                Field('email_dep','string',label='Correo Electrónico del Departamento'),
                Field('sede','string', requires=IS_IN_SET(['Sartenejas','Litoral'],error_message='Sede Inválida'), label='Sede', notnull=True))


# Validadores
dbSPE.departamento.email_dep.requires=[IS_EMAIL(error_message=T('Este no es un correo valido'))]
dbSPE.departamento.email_dep.requires+=[IS_LENGTH(100)]
dbSPE.departamento.email_dep.requires+=[IS_NOT_EMPTY(error_message='Campo Obligatorio')]
'''
