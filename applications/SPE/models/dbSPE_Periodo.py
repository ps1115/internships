# -*- coding: utf-8 -*-

"""
dbSPE.define_table("periodo"
                  ,Field('nombre',label="Nombre del Periodo", notnull=True, unique=True)
                  ,Field('fecha_inicio', label="Fecha de Inicio", type='date',requires=[IS_NOT_EMPTY(),IS_DATE(format='%Y/%m/%d')])
                  ,Field('fecha_fin', label="Fecha de Fin", type='date',requires=[IS_NOT_EMPTY(),IS_DATE(format='%Y/%m/%d')])
                  ,Field('periodo_activo', label="Situación", requires=IS_IN_SET({1:'activo',0:'no activo'})))
"""
