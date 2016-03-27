# -*- coding: utf-8 -*-

# Estudiante
dbSPE.define_table('carrera',
                Field('codigo', requires=IS_NOT_EMPTY(), label="Código"),
                Field('nombre', requires=IS_NOT_EMPTY(), label="Nombre"),
                Field('duracion', requires=[IS_NOT_EMPTY(), IS_IN_SET(['Larga','Corta'], error_message='Duración Inválida')], label="Duración", default='Larga'),
                Field('sede', requires=[IS_NOT_EMPTY(), IS_IN_SET(['Sartenejas','Litoral'], error_message='Sede Inválida')], label="Sede", default='Sartenejas'),
                Field('coordinacion', requires=IS_NOT_EMPTY(), label="Coordinación"),
                primarykey=['codigo'],
                format='%(codigo)s %(nombre)s'
                )
