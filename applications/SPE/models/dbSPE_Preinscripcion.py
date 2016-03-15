# -*- coding: utf-8 -*-

# Estudiante
dbSPE.define_table('preinscripcion',
                Field('id','id', requires=[IS_LENGTH(10)]),
                Field('id_periodo','integer',required=True, requires=[IS_LENGTH(10)]),
                Field('anio','integer',required=True,requires=[IS_LENGTH(4)]),
                Field('codigo','string',required=True, requires=[IS_LENGTH(4)]),
                Field('usbid','string', required=True, requires=[IS_LENGTH(254)]),
                Field('fecha_ingreso','datetime',required=True),
                Field('fecha_validacion','datetime'),
                Field('colocacion','boolean',default=False),
                Field('id_region','integer'),
                Field('id_estado',dbSPE.estado),
                Field('validada','boolean',default=False),
                Field('cod_seguridad','string', requires=[IS_LENGTH(10)]),
                primarykey=['id'],
                format='%(usbid)s  %(cod_seguridad)s'
               )
