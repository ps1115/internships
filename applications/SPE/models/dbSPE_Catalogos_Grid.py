# -*- coding: utf-8 -*-
import datetime

# dbSPE.define_table('usuario_estudiante',
#                 Field('usbid_usuario', requires=[IS_NOT_EMPTY(), IS_MATCH('[0-9][0-9]-[0-9]{5}','USBID Inválido')], unique=True, label="USBID"),
#                 Field('carrera', requires=[IS_NOT_EMPTY(), IS_IN_DB(dbSPE,'carrera.nombre', error_message='Carrera Inválida')], label="Carrera"),
#                 Field('cohorte', requires=IS_NOT_EMPTY(), type='integer', label="Cohorte"),
#                 Field('estudiante_sede', label="Sede",requires=IS_IN_SET(['Sartenejas','Litoral'],error_message='Elija una Sede'), default='Sartenejas'),
#                 Field('email_sec', label="Correo Eléctronico", requires=IS_EMAIL('Correo Electrónico Inválido')),
#                 Field('telf_hab', label="Teléfono de Habitación"),
#                 Field('telf_cel', label="Teléfono celular"),
#                 Field('direccion', label="Dirección de Habitación"),
#                 Field('sexo', label="Sexo", requires=IS_IN_SET(['M','F'], error_message="Indique su Sexo")))

# dbSPE.define_table('carrera',
#                 Field('codigo', requires=IS_NOT_EMPTY(), label="Código"),
#                 Field('nombre', requires=IS_NOT_EMPTY(), label="Nombre"),
#                 Field('duracion', requires=[IS_NOT_EMPTY(), IS_IN_SET(['Larga','Corta'], error_message='Duración Inválida')], label="Duración", default='Larga'),
#                 Field('sede', requires=[IS_NOT_EMPTY(), IS_IN_SET(['Sartenejas','Litoral'], error_message='Sede Inválida')], label="Sede", default='Sartenejas'),
#                 Field('coordinacion', requires=IS_NOT_EMPTY(), label="Coordinación"))

# Division
dbSPE.define_table('division',
                Field('nombre','string',required=True),
                format='%(nombre)s'
               )

dbSPE.division.nombre.requires+=[IS_LENGTH(100)]
dbSPE.division.nombre.requires+=[IS_NOT_EMPTY(error_message='Campo Obligatorio')]

dbSPE.define_table('departamento',
                Field('nombre', requires=IS_NOT_EMPTY(), default='', label="Nombre del departamento"),
                Field('id_division', represent=lambda x, row: (dbSPE(dbSPE.division.id==x)).select().first().nombre,requires=IS_IN_DB(dbSPE,'division.id', '%(nombre)s',error_message='División no existe'), notnull=True, label='Nombre de División'),
                Field('email_dep', requires=IS_EMAIL('Correo electrónico inválido'),label='Correo electrónico del departamento'),
                Field('sede', requires=IS_IN_SET(['Sartenejas','Litoral'],error_message='Sede inválida'), label='Sede', notnull=True))

# dbSPE.define_table('usuario_profesor',
#                 Field('usbid_usuario', requires=[IS_NOT_EMPTY(), IS_MATCH('[0-9][0-9]-[0-9]{5}','USBID Inválido')], label='USBID', unique=True),
#                 Field('dependencia', requires=IS_NOT_EMPTY(), label='Dependencia'),
#                 Field('dedicacion', requires=IS_NOT_EMPTY(), label='Dedicación'),
#                 Field('categoria', requires=IS_NOT_EMPTY(), label='Categoría'),
#                 Field('email_sec', requires=[IS_NOT_EMPTY(), IS_EMAIL(error_message='Correo Electrónico Inválido')], label='Correo Electrónico'),
#                 Field('telf', requires=IS_NOT_EMPTY(), label='Teléfono de Habitación'),
#                 Field('celular', requires=IS_NOT_EMPTY(), label='Teléfono Celular'),
#                 Field('activo', requires=[IS_NOT_EMPTY(), IS_IN_SET(['0','1'],error_message='Valor no Permitido')], default='1', label='Activo'))

"""
dbSPE.define_table("evento"
               ,Field("codigo", type="id", readable=False, writable=False)
               ,Field("nombre", label="Nombre del Evento", requires=IS_NOT_EMPTY(),unique=True)
               ,Field("fecha_inicio", label="Fecha de Inicio", type="date", requires=[IS_NOT_EMPTY(),IS_DATE(format='%Y/%m/%d')])
               ,Field("fecha_fin", label="Fecha de Finalización", type="date", requires=[IS_NOT_EMPTY(),IS_DATE(format='%Y/%m/%d')])
               ,Field("nombre_trimestre_actual", label="Nombre del Trimestre Actual", requires=IS_NOT_EMPTY()))


dbSPE.define_table("sub_evento"
               ,Field("codigo_sub_evento", type="id" ,readable=False, writable=False)
               ,Field("nombre_supra_evento", type="string",label="Nombre del Supra Evento",
                      requires=IS_IN_DB(dbSPE,'evento.nombre', error_message='Evento no Existe'))
               ,Field("nombre_sub_evento", label="Nombre del Sub Evento", requires=IS_NOT_EMPTY())
               ,Field("fecha_inicio", label="Fecha de Inicio", type="date", requires=[IS_NOT_EMPTY(),IS_DATE(format='%Y/%m/%d')])
               ,Field("fecha_fin", label="Fecha de Finalización", type="date", requires=[IS_NOT_EMPTY(),IS_DATE(format='%Y/%m/%d')]))
"""

dbSPE.define_table("periodo"
                  ,Field('nombre',label="Nombre del período", notnull=True, unique=True)
                  ,Field('fecha_inicio', label="Fecha de inicio", type='date',requires=[IS_NOT_EMPTY(),IS_DATE(format='%Y/%m/%d')])
                  ,Field('fecha_fin', label="Fecha de finalización", type='date',requires=[IS_NOT_EMPTY(),IS_DATE(format='%Y/%m/%d')])
                  ,Field('periodo_activo', represent=lambda x, row: (dict({1:"Activo",0:"No Activo"}))[x],label="Situación del período", requires=IS_IN_SET({1:'Activo',0:'No Activo'})))


dbSPE.define_table("semana_muerta"
               ,Field("codigo_periodo_afectado", represent=lambda x, row: (dbSPE(dbSPE.periodo.id==x)).select().first().nombre,label="Nombre de período", type="integer",  requires=IS_IN_DB(dbSPE,'periodo.id', '%(nombre)s',error_message='Período no existe'), notnull=True)
               ,Field("numero_semana", type="integer",label="Número de semanas afectadas", requires=IS_NOT_EMPTY())
               ,Field("fecha_ini", label="Fecha de inicio", type="date", requires=[IS_NOT_EMPTY(),IS_DATE(format='%Y/%m/%d')])
               ,Field("fecha_fini", label="Fecha de finalización", type="date", requires=[IS_NOT_EMPTY(),IS_DATE(format='%Y/%m/%d')]))
"""
dbSPE.define_table('usuario'
                  ,Field('usbid')
                  ,Field('nombre')
                  ,Field('apellido')
                  ,Field('ci')
                  ,Field('tipo')
                  ,Field('foto')
                  ,Field('llave'))
"""
dbSPE.define_table("rol_sistema"
               ,Field("usbid", label="USBID", requires=IS_IN_DB(dbSPE,'usuario.usbid', '%(nombre)s',error_message='USBID no existe.'), unique=True)
               ,Field("nombre", label="Nombre del usuario", requires=IS_NOT_EMPTY())
               ,Field("apellido", label="Apellido del usuario",requires=IS_NOT_EMPTY())
               ,Field("rol", label="Nombre del rol", requires=IS_NOT_EMPTY(), unique=True)
               ,Field("sede", label="Sede", requires=IS_IN_SET(['Sartenejas','Litoral'],error_message='Sede Inválida'),notnull=True, default="Sartenejas"))

dbSPE.define_table("calculo_pago"
               , Field("id_categoria",represent=lambda x, row: (dbSPE(dbSPE.categoria.id==x)).select().first().nombre,label="Categoría", requires=IS_IN_DB(dbSPE,'categoria.id', '%(nombre)s',error_message='Categoría no existe'),type="integer")
               , Field("id_tipo_pasantia",represent=lambda x, row: (dbSPE(dbSPE.tipo_pasantia.codigo==x)).select().first().nombre,label="Tipo de pasantía",requires=IS_IN_DB(dbSPE,'tipo_pasantia.codigo', '%(nombre)s',error_message='Tipo de pasantía no existe'), notnull=True)
               , Field("id_pais",represent=lambda x, row: (dbSPE(dbSPE.pais.id==x)).select().first().nombre,label="País",requires=IS_IN_DB(dbSPE,'pais.id', '%(nombre)s',error_message='País no existe'), notnull=True,type="reference pais.id")
               , Field("monto",requires=IS_NOT_EMPTY(),type="double", label="Monto de Pago")
               ,Field("fecha", label="Fecha", type="date",requires=[IS_NOT_EMPTY(),IS_DATE(format='%Y/%m/%d')]))
