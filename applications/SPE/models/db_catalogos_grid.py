# -*- coding: utf-8 -*-

db = DAL('sqlite://storage.sqlite')

import datetime

db.define_table('usuario_estudiante', 
                Field('usbid_usuario', requires=[IS_NOT_EMPTY(), IS_MATCH('[0-9][0-9]-[0-9]{5}','USBID Inválido')], unique=True, label="USBID"),
                Field('carrera', requires=[IS_NOT_EMPTY(), IS_IN_DB(db,'carrera.nombre', error_message='Carrera Inválida')], label="Carrera"),
                Field('cohorte', requires=IS_NOT_EMPTY(), type='integer', label="Cohorte"),
                Field('estudiante_sede', label="Sede",requires=IS_IN_SET(['Sartenejas','Litoral'],error_message='Elija una Sede'), default='Sartenejas'),
                Field('email_sec', label="Correo Eléctronico", requires=IS_EMAIL('Correo Electrónico Inválido')),
                Field('telf_hab', label="Teléfono de Habitación"),
                Field('telf_cel', label="Teléfono celular"),
                Field('direccion', label="Dirección de Habitación"),
                Field('sexo', label="Sexo", requires=IS_IN_SET(['M','F'], error_message="Indique su Sexo")))

db.define_table('carrera', 
                Field('codigo', requires=IS_NOT_EMPTY(), label="Código"), 
                Field('nombre', requires=IS_NOT_EMPTY(), label="Nombre"),
                Field('duracion', requires=[IS_NOT_EMPTY(), IS_IN_SET(['Larga','Corta'], error_message='Duración Inválida')], label="Duración", default='Larga'),
                Field('sede', requires=[IS_NOT_EMPTY(), IS_IN_SET(['Sartenejas','Litoral'], error_message='Sede Inválida')], label="Sede", default='Sartenejas'),
                Field('coordinacion', requires=IS_NOT_EMPTY(), label="Coordinación"))

db.define_table('departamento', 
                Field('nombre', requires=IS_NOT_EMPTY(), default='', label="Nombre del Departamento"),
                Field('id_division', requires=IS_NOT_EMPTY(), default='0', label='Identificador de División'),
                Field('email_dep', requires=IS_EMAIL('Correo Electrónico Inválido'),label='Correo Electrónico del Departamento'),
                Field('sede', requires=[IS_NOT_EMPTY(), IS_IN_SET(['Sartenejas','Litoral'],error_message='Sede Inválida')], label='Sede', default='Sartenejas'))

db.define_table('usuario_profesor', 
                Field('usbid_usuario', requires=[IS_NOT_EMPTY(), IS_MATCH('[0-9][0-9]-[0-9]{5}','USBID Inválido')], label='USBID', unique=True), 
                Field('dependencia', requires=IS_NOT_EMPTY(), label='Dependencia'),
                Field('dedicacion', requires=IS_NOT_EMPTY(), label='Dedicación'),
                Field('categoria', requires=IS_NOT_EMPTY(), label='Categoría'),
                Field('email_sec', requires=[IS_NOT_EMPTY(), IS_EMAIL(error_message='Correo Electrónico Inválido')], label='Correo Electrónico'),
                Field('telf', requires=IS_NOT_EMPTY(), label='Teléfono de Habitación'),
                Field('celular', requires=IS_NOT_EMPTY(), label='Teléfono Celular'),
                Field('activo', requires=[IS_NOT_EMPTY(), IS_IN_SET(['0','1'],error_message='Valor no Permitido')], default='1', label='Activo'))

db.define_table('empresa', 
                Field('log', requires=IS_NOT_EMPTY(), label='Usuario', unique=True), 
                Field('password', requires=IS_NOT_EMPTY(), label='Clave', type='password'),
                Field('pregunta_secreta', requires=IS_NOT_EMPTY(), label='Pregunta Secreta'),
                Field('respuesta_pregunta_secreta', requires=IS_NOT_EMPTY(), label='Respuesta a Pregunta Secreta'),
                Field('nombre', requires=IS_NOT_EMPTY(), label='Nombre de la Empresa'),
                Field('direccion', requires=IS_NOT_EMPTY(), label='Dirección de la Empresa'),
                Field('pag_web', requires=[IS_NOT_EMPTY(),IS_URL(error_message='URL Inválida')], label='Sitio Web de la Empresa'),
                Field('descripcion', requires=IS_NOT_EMPTY(), label='Descripción de la Empresa'),
                Field('telefono', requires=IS_NOT_EMPTY(), label='Teléfono de Contacto de la Empresa'),
                Field('contacto_RRHH', requires=IS_NOT_EMPTY(), label='Teléfono de la Sección de Recursos Humanos'),
                Field('intentos', type='integer', default='0',readable=False, writable=False, requires=IS_NOT_EMPTY()),
                Field('habilitado', type='integer', default='1',readable=False, writable=False, requires=IS_NOT_EMPTY()),
                Field('fechaCreacion', type='datetime',requires=[IS_NOT_EMPTY(),IS_DATETIME(format='%Y-%m-%d %H:%M:%S')], readable=False, writable=False, default=datetime.datetime.now()),
                Field('ultimaModificacion', type='datetime',requires=[IS_NOT_EMPTY(),IS_DATETIME(format='%Y-%m-%d %H:%M:%S')], readable=False, writable=False, default=datetime.datetime.now()))



db.define_table("evento"
               ,Field("codigo", type="integer", readable=False, writable=False)
               ,Field("nombre", label="Nombre del Evento", requires=IS_NOT_EMPTY(),unique=True)
               ,Field("fecha_inicio", label="Fecha de Inicio", type="date", requires=[IS_NOT_EMPTY(),IS_DATE(format='%Y/%m/%d')])
               ,Field("fecha_fin", label="Fecha de Finalización", type="date", requires=[IS_NOT_EMPTY(),IS_DATE(format='%Y/%m/%d')])
               ,Field("nombre_trimestre_actual", label="Nombre del Trimestre Actual", requires=IS_NOT_EMPTY()))


db.define_table("sub_evento"
               ,Field("codigo_supra_evento", type="integer", readable=False, writable=False)
               ,Field("codigo_sub_evento", type="integer",readable=False, writable=False)
               # Hay que agregar nombre_supra_evento al sql
               ,Field("nombre_supra_evento", type="string",label="Nombre del Supra Evento", 
                      requires=IS_IN_DB(db,'evento.nombre', error_message='Evento no Existe'))
               ,Field("nombre_sub_evento", label="Nombre del Sub Evento", requires=IS_NOT_EMPTY())
               ,Field("fecha_inicio", label="Fecha de Inicio", type="date", requires=[IS_NOT_EMPTY(),IS_DATE(format='%Y/%m/%d')])
               ,Field("fecha_fin", label="Fecha de Finalización", type="date", requires=[IS_NOT_EMPTY(),IS_DATE(format='%Y/%m/%d')]))

db.define_table("semana_muerta"
               ,Field("codigo_supra_evento_afectado", type="integer",writable=False, readable=False)
               ,Field("codigo_sub_evento_afectado", type="integer",writable=False, readable=False)
               ,Field("nombre_supra_evento_afectado", label="Nombre de Evento", type="string",  requires=IS_IN_DB(db,'sub_evento.nombre_supra_evento', error_message='Evento no Existe'))
               ,Field("nombre_sub_evento_afectado", label="Nombre de Sub Evento", type="string",  requires=IS_IN_DB(db,'sub_evento.nombre_sub_evento', error_message='Evento no Existe'))
               ,Field("numero_semana", type="integer",label="Numero de Semana", requires=IS_NOT_EMPTY())
               ,Field("fecha_ini", label="Fecha de Inicio", type="date", requires=[IS_NOT_EMPTY(),IS_DATE(format='%Y/%m/%d')])
               ,Field("fecha_fini", label="Fecha de Finalización", type="date", requires=[IS_NOT_EMPTY(),IS_DATE(format='%Y/%m/%d')]))


db.define_table("rol_sistema"
               ,Field("usbid", label="USBID", requires=[IS_NOT_EMPTY(),IS_MATCH('[0-9][0-9]-[0-9]{5}','USBID Inválido')], unique=True)
               ,Field("nombre", label="Nombre del Usuario", requires=IS_NOT_EMPTY())
               ,Field("apellido", label="Apellido del Usuario",requires=IS_NOT_EMPTY())
               ,Field("rol", label="Nombre del Rol", requires=IS_NOT_EMPTY(), unique=True)
               ,Field("sede", label="Sede", requires=[IS_NOT_EMPTY(), IS_IN_SET(['Sartenejas','Litoral'],error_message='Sede Inválida')], default="Sartenejas"))

db.define_table("calculo_pago"
               , Field("id_categoria",label="Categoría", requires=IS_NOT_EMPTY(),type="integer")
               , Field("id_tipo_pasantia",label="Tipo de Pasantía",requires=IS_NOT_EMPTY())
               , Field("id_pais",label="País",requires=IS_NOT_EMPTY(),type="integer")
               , Field("monto",requires=IS_NOT_EMPTY(),type="double", label="Monto de Pago")
               ,Field("fecha", label="Fecha", type="date",requires=[IS_NOT_EMPTY(),IS_DATE(format='%Y/%m/%d')]))
