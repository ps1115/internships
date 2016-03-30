# -*- coding: utf-8 -*-

'''

	id INT(11) NOT NULL AUTO_INCREMENT,
	correo VARCHAR(80) NOT NULL,
	codigo VARCHAR(45) NOT NULL,
'''

dbSPE.define_table('correo_por_verificar',
                Field('correo','string',required=True,ondelete='CASCADE',
                    notnull=True, unique=True,label='Pais'),
                Field('codigo','string',required=True,ondelete='CASCADE',
                    notnull=True, unique=True,label='Pais'),format='%(correo)s - %(codigo)s')

dbSPE.correo_por_verificar.correo.requires=[IS_EMAIL(error_message=T('Este no es un correo valido'))]
