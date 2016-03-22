# -*- coding: utf-8 -*-

# Curriculum
dbSPE.define_table('curriculum',
                Field('usbid','string',required=True, requires=[IS_LENGTH(254)]),
                Field('electiva','string', requires=[IS_LENGTH(100)]),
                Field('cursos','string',requires=[IS_LENGTH(150)]),
                Field('conocimientos','string',requires=[IS_LENGTH(100)]),
                Field('idiomas','string',requires=[IS_LENGTH(60)]),
                Field('aficiones','string',requires=[IS_LENGTH(150)]),
                primarykey=['usbid'],
                format='%(usbid)s  %(electiva)s  %(cursos)s  %(conocimientos)s  %(idiomas)s  %(aficiones)s'
               )
