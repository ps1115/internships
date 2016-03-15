# # -*- coding: utf-8 -*-

dbSPE.define_table('pasantia',
   Field('codigo'),
   Field('periodo'),
   Field('anio'),
   Field('fecha'),
   Field('cod_seguridad'),
   Field('titulo'),
   Field('area_proyecto'),
   Field('resumen_proyecto'),
   Field('confidencial'),
   Field('objetivos'),
   Field('calificacion_total'),
   Field('calificacion_tutor_academico'),
   Field('calificacion_tutor_industrial'),
   Field('fecha_acta_evaluacion'),
   Field('periodo_finaliza'),
   Field('anio_finaliza'),
   Field('tiene_mencion'),
   Field('observacion_mencion'),
   Field('fecha_validacion'),
   Field('status'),
   Field('id_tutor_industrial'),
   Field('id_jurado'),
   Field('id_estudiante'),
   Field('id_tutor_academico'),
   Field('retirar'),
   Field('obtencion_pasantia'),
   Field('motivo_retiro_tutor_industrial','text',label=T('Motivo')),
   Field('motivo_retiro_tutor_academico','text',label=T('Motivo')),
   Field('motivo_retiro_estudiante','text',label=T('Motivo')),
   primarykey=['codigo','id_estudiante','anio','periodo'],
   format = '%(codigo)s %(periodo)s'
   )

dbSPE.pasantia.motivo_retiro_tutor_industrial.requires+=[IS_NOT_EMPTY(error_message='Campo Obligatorio')]
dbSPE.pasantia.motivo_retiro_tutor_academico.requires+=[IS_NOT_EMPTY(error_message='Campo Obligatorio')]
dbSPE.pasantia.motivo_retiro_estudiante.requires+=[IS_NOT_EMPTY(error_message='Campo Obligatorio')]