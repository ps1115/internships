# # -*- coding: utf-8 -*-

dbSPE.define_table('solicita_permiso',
   Field('usbid_estudiante'),
   Field('codigo_permiso'),
   primarykey=['usbid_estudiante', 'codigo_permiso']
   )