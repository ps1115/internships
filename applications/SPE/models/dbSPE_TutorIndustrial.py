# -*- coding: utf-8 -*-

'''
CREATE TABLE IF NOT EXISTS `tutor_industrial` (
  `email` varchar(254) NOT NULL,
  `nombre` varchar(254) DEFAULT NULL,
  `apellido` varchar(254) DEFAULT NULL,
  `ci` varchar(8) DEFAULT NULL,
  `password` varchar(254) DEFAULT NULL,
  `empresa` varchar(254) DEFAULT NULL,
  `profesion` varchar(50) NOT NULL,
  `cargo` varchar(50) NOT NULL,
  `departamento` varchar(50) NOT NULL,
  `id_estado` int(2) DEFAULT NULL,
  `telefono` varchar(20) NOT NULL,
  PRIMARY KEY (`email`),
  KEY `fk_tutor_industrial_id_estado_estado_nombre` (`id_estado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''

'''
# Tutor Industrial
dbSPE.define_table('tutorIndustrial',
                   Field('email','string',required=True, requires=[
            IS_EMAIL(error_message=T('Este no es un correo valido')),
            IS_LENGTH(512),
            IS_NOT_EMPTY(error_message='Campo Obligatorio'),
            IS_NOT_IN_DB(dbSPE, 'tutorIndustrial.email',error_message=T('Correo No Disponible'))], 
                         ondelete='CASCADE', notnull=True, unique=True,label='Correo Electronico'),
                Field('password','password', required=True, notnull=True,label=T('Contraseña'),requires=[
            IS_LENGTH(512),
            IS_NOT_EMPTY(error_message=T('Campo Obligatorio'))
        ]),
                Field('pregunta_secreta','string',label=T('Pregunta Secreta'),requires=[
            IS_LENGTH(512),
            IS_NOT_EMPTY(error_message='Campo Obligatorio')
        ]),
                Field('respuesta_pregunta_secreta','string',label=T('Respuesta A Pregunta Secreta'),requires=[IS_LENGTH(512),IS_NOT_EMPTY(error_message=T('Campo Obligatorio'))]),
                Field('nombre','string',required=True, notnull=True,label=T('Nombre De La Empresa'),requires=[IS_LENGTH(512),IS_NOT_EMPTY(error_message=T('Campo Obligatorio'))]),
                Field('direccion','text',label=T('Direccion De La Empresa')),
                Field('pag_web','string',label=T('Pagina Web')),
                Field('descripcion','text',label=T('Descripcion De La Empresa')),
                Field('telefono','string',label=T('Telefono'), requires=[IS_MATCH('^\+[0-9]*$|^[0-9]*$',error_message=T('Solo se permiten numeros y el signo +'))]),
                Field('contacto_RRHH','string',required=True,notnull=True,requires=[IS_EMAIL(error_message=T('Este no es un correo valido')),IS_NOT_EMPTY(error_message='Campo Obligatorio'),IS_LENGTH(512)],label=T('Contacto De Recursos Humanos')),
                Field('intentos','integer',default=0,label=T('Intentos')),
                Field('habilitado','integer',default=1,requires = [IS_INT_IN_RANGE(0, 2)],label='Habilitado'),
                Field('fechaCreacion','datetime',label=T('Fecha De Creacion')),
                Field('ultimaModificacion','datetime',label=T('Fecha De Ultima Modificacion')),
                format='%(nombre)s %(loginID)s',
                primarykey=['loginID']
               )
               
               '''
