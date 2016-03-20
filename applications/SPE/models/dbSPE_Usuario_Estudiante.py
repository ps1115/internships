# -*- coding: utf-8 -*-

# Estudiante
dbSPE.define_table('usuario_estudiante',
                Field('usbid_usuario', requires=[IS_NOT_EMPTY(), IS_MATCH('[0-9][0-9]-[0-9]{5}','USBID Inválido')], unique=True, label="USBID"),
                Field('carrera', requires=[IS_NOT_EMPTY(),IS_IN_DB(dbSPE,dbSPE.carrera,'%(nombre)s',zero="Seleccione", error_message='Carrera Inválida')], label="Carrera"),
                Field('cohorte', requires=IS_NOT_EMPTY(), type='integer', label="Cohorte"),
                Field('estudiante_sede', label="Sede",requires=IS_IN_SET(['Sartenejas','Litoral'],error_message='Elija una Sede'), default='Sartenejas'),
                Field('email_sec', label="Correo Eléctronico", requires=IS_EMAIL('Correo Electrónico Inválido')),
                Field('telf_hab', label="Teléfono de Habitación"),
                Field('telf_cel', label="Teléfono celular"),
                Field('direccion', label="Dirección de Habitación"),
                Field('sexo', label="Sexo", requires=IS_IN_SET(['M','F'], error_message="Indique su Sexo")),
                primarykey=['usbid_usuario'],
                format='%(carnet)s'
                )
