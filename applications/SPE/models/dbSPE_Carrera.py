# -*- coding: utf-8 -*-

# Estudiante
dbSPE.define_table('carrera',
                Field('codigo','string',required=True, ondelete='CASCADE', notnull=True, unique=True,label='Código'),
                Field('nombre','string',required=True,unique=True, requires=[IS_LENGTH(100)], label='Nombre'),
                Field('duracion','string',required=True, requires=IS_IN_SET(['Larga','Corta']), label="Duración", notnull=True),
                Field('sede','string', requires=IS_IN_SET(['Sartenejas','Litoral'],zero=None), label="Sede", notnull=True),
                Field('coordinacion', label="Coordinación", required=True),
                primarykey=['codigo'],
                format='%(codigo)s %(nombre)s'
               )

dbSPE.carrera.coordinacion.requires=IS_IN_DB(dbSPE,dbSPE.coordinacion.id,'%(sede)s - %(nombre)s',zero=None)
dbSPE.carrera.codigo.requires = [IS_LENGTH(4)
        ,IS_NOT_EMPTY(error_message='Campo Obligatorio')
        ,IS_NOT_IN_DB(dbSPE, 'carrera.codigo',error_message=T('Carrera ya existe'))
        ,IS_MATCH('[0-9]{4}',error_message=T('Solo se permiten numeros de cuatro digitos'))]
