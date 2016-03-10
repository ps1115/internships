# -*- coding: utf-8 -*-

'''
    `nombre`    varchar(40) NOT NULL,
    `id_zona`   int(11)     NOT NULL,
'''

dbSPE.define_table('estado',
                Field('log','string',required=True, requires=[IS_LENGTH(512),IS_NOT_EMPTY(error_message='Campo Obligatorio'),IS_NOT_IN_DB(dbSPE, 'empresa.log',error_message=T('Login No Disponible'))], ondelete='CASCADE', notnull=True, unique=True,label='Login'),
                Field('password','password', required=True, notnull=True,label=T('Contraseña'),requires=[IS_LENGTH(512),IS_NOT_EMPTY(error_message=T('Campo Obligatorio'))]) ,format='%(nombre)s %(log)s')
