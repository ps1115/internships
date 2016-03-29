# # -*- coding: utf-8 -*-

dbSPE.define_table('permiso',
   Field('codigo'),
   Field('fecha'),
   Field('codigo_seguridad'),
   Field('tipo_permiso'),
   Field('fecha_propuesta'),
   Field('justificacion'),
   Field('observacion_cctds'),
   Field('status'),
   Field('fechas_propuestas')
   )