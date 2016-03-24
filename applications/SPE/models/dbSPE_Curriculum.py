# -*- coding: utf-8 -*-

# Curriculum
dbSPE.define_table('curriculum',
                Field('usbid','string',required=True, requires=[IS_LENGTH(254)]),
                Field('electiva','string'),
                Field('cursos','string'),
                Field('conocimientos','string'),
                Field('idiomas','string'),
                Field('aficiones','string'),
                primarykey=['usbid'],
                format='%(usbid)s  %(electiva)s  %(cursos)s  %(conocimientos)s  %(idiomas)s  %(aficiones)s'
               )
