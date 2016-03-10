# -*- coding: utf-8 -*-

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

## app configuration made easy. Look inside private/appconfig.ini
from gluon.contrib.appconfig import AppConfig
## once in production, remove reload=True to gain full speed
myconf = AppConfig(reload=True)


if not request.env.web2py_runtime_gae:
    ## if NOT running on Google App Engine use SQLite or other DB
    db = DAL(myconf.take('db.uri'), pool_size=myconf.take('db.pool_size', cast=int), check_reserved=['all'])
else:
    ## connect to Google BigTable (optional 'google:datastore://namespace')
    db = DAL('google:datastore+ndb')
    ## store sessions and tickets there
    session.connect(request, response, db=db)
    ## or store session in Memcache, Redis, etc.
    ## from gluon.contrib.memdb import MEMDB
    ## from google.appengine.api.memcache import Client
    ## session.connect(request, response, db = MEMDB(Client()))

## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []
## choose a style for forms
response.formstyle = myconf.take('forms.formstyle')  # or 'bootstrap3_stacked' or 'bootstrap2' or other
response.form_label_separator = myconf.take('forms.separator')


## (optional) optimize handling of static files
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'
## (optional) static assets folder versioning
# response.static_version = '0.0.0'
#########################################################################
## Here is sample code if you need for
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - old style crud actions
## (more options discussed in gluon/tools.py)
#########################################################################

from gluon.tools import Auth, Service, PluginManager

auth = Auth(db)
service = Service()
plugins = PluginManager()

## create all tables needed by auth if not custom tables
auth.define_tables(username=False, signature=False)

## configure email
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else myconf.take('smtp.server')
mail.settings.sender = myconf.take('smtp.sender')
mail.settings.login = myconf.take('smtp.login')

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

#########################################################################
## Define your tables below (or better in another model file) for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################

## after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)


###### GESTION COORDINADOR con sqlite ########

db = DAL('sqlite://storage.sqlite')

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
                Field('login', requires=IS_NOT_EMPTY(), label='Usuario', unique=True), 
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
                Field('fechaCreacion', type='datetime',requires=IS_NOT_EMPTY(), readable=False, writable=False, default='0000-00-00 00:00:00'),
                Field('ultimaModificacion', type='datetime',requires=IS_NOT_EMPTY(), readable=False, writable=False, default='0000-00-00 00:00:00'))



db.define_table("evento"
               ,Field("codigo", label="Código", type="integer", readable=False, writable=False,  requires=IS_NOT_EMPTY())
               ,Field("nombre", label="Nombre del Evento", requires=IS_NOT_EMPTY(),unique=True)
               ,Field("fecha_inicio", label="Fecha de Inicio", type="date", requires=[IS_NOT_EMPTY(),IS_DATE(format='%d/%m/%Y')])
               ,Field("fecha_fin", label="Fecha de Finalización", type="date", requires=[IS_NOT_EMPTY(),IS_DATE(format='%d/%m/%Y')])
               ,Field("nombre_trimestre_actual", label="Nombre del Trimestre Actual", requires=IS_NOT_EMPTY()))


db.define_table("sub_evento"
               ,Field("codigo_supra_evento", type="integer",label="Código Supra Evento", readable=False, writable=False,  requires=IS_NOT_EMPTY())
               ,Field("codigo_sub_evento", label="Código Sub Evento", type="integer", readable=False, writable=False,  requires=IS_NOT_EMPTY())
               ,Field("nombre_supra_evento", type="string",label="Nombre del Supra Evento", 
                      requires=IS_IN_DB(db,'evento.nombre', error_message='Evento no Existe'))
               ,Field("nombre_sub_evento", label="Nombre del Sub Evento", requires=IS_NOT_EMPTY())
               ,Field("fecha_inicio", label="Fecha de Inicio", type="date", requires=[IS_NOT_EMPTY(),IS_DATE(format='%d/%m/%Y')])
               ,Field("fecha_fin", label="Fecha de Finalización", type="date", requires=[IS_NOT_EMPTY(),IS_DATE(format='%d/%m/%Y')]))

db.define_table("semana_muerta"
               ,Field("nombre_supra_evento_afectado", label="Nombre de Evento", type="string",  requires=IS_IN_DB(db,'sub_evento.nombre_supra_evento', error_message='Evento no Existe'))
               ,Field("nombre_sub_evento_afectado", label="Nombre de Sub Evento", type="string",  requires=IS_IN_DB(db,'sub_evento.nombre_sub_evento', error_message='Evento no Existe'))
               ,Field("numero_semana", type="integer",label="Numero de Semana", requires=IS_NOT_EMPTY())
               ,Field("fecha_ini", label="Fecha de Inicio", type="date", requires=[IS_NOT_EMPTY()])
               ,Field("fecha_fini", label="Fecha de Finalización", type="date", requires=[IS_NOT_EMPTY(),IS_DATE(format='%d/%m/%Y')]))


db.define_table("rol_sistema"
               ,Field("usbid", label="USBID", requires=[IS_NOT_EMPTY()], unique=True)
               ,Field("nombre", label="Nombre del Usuario", requires=IS_NOT_EMPTY())
               ,Field("apellido", label="Apellido del Usuario",requires=IS_NOT_EMPTY())
               ,Field("rol", label="Nombre del Rol", requires=IS_NOT_EMPTY(), unique=True)
               ,Field("sede", label="Sede", requires=[IS_NOT_EMPTY(), IS_IN_SET(['Sartenejas','Litoral'],error_message='Sede Inválida')], default="Sartenejas")
               ,Field("longitudCarnet", type="integer",label="Longitud del Carnet" ,requires=IS_NOT_EMPTY()))


db.define_table("calculo_pago"
               , Field("id_categoria", requires=IS_NOT_EMPTY(),type="integer")
               , Field("id_tipo_pasantia",requires=IS_NOT_EMPTY())
               , Field("id_zona",requires=IS_NOT_EMPTY(),type="integer")
               , Field("monto",requires=IS_NOT_EMPTY(),type="double", label="Monto de Pago"))

###### FIN GESTION COORDINADOR #####
