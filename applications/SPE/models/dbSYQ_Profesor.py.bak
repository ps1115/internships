# -*- coding: utf-8 -*-

# Empresa
dbSYQ.define_table('contacto',
   Field('nombre'),
   Field('telefono'))

dbSYQ.define_table('pasantia1',
                  Field('codigo','string', required=True,label=T('Codigo_Pasantia'), requires=[IS_LENGTH(8),IS_NOT_EMPTY(error_message='Campo Obligatorio')]),
                  Field('periodo','int', required=True,label=T('Carnet_Estudiante'), requires=[IS_LENGTH(10),IS_NOT_EMPTY(error_message='Campo Obligatorio')]),
                  Field('motivo_retiro_tutor_academico','text', required=True, notnull=True,label=T('Motivo'),requires= IS_NOT_EMPTY(error_message=T('Campo Obligatorio'))),
                  primarykey=['periodo']
                 )
