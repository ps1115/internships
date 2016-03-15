# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A(B('web',SPAN(2),'py'),XML('&trade;&nbsp;'),
                  _class="navbar-brand",_href="http://www.web2py.com/",
                  _id="web2py-logo")
response.title = request.application.replace('_',' ').title()
response.subtitle = ''

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Your Name <you@example.com>'
response.meta.description = 'a cool new app'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('Inicio'), False, URL('default', 'index'), [])
]

DEVELOPMENT_MENU = True

#########################################################################
## Menu personalizado para la autenticacion
#########################################################################

if auth.is_logged_in():
    texto_principal = "Bienvenido " + auth.user.first_name
else:
    texto_principal = "Bienvenido"

menu_autenticado = [
    (texto_principal,False, '#',[
        ("Cerrar Sesion",False,URL('default','logout'))
    ])
]

#########################################################################
## provide shortcuts for development. remove in production
#########################################################################

def _():
    # shortcuts
    app = request.application
    ctr = request.controller
    # useful links to internal and external resources
    response.menu += [
        (T('Iniciar Sesion'),False,'#',[
            (T('Miembro USB'),False,"#"),
            (T('Empresa'),False,'#')
            ]),
        ('Estudiante',False,"#",[
            ('Agregar Preinscripcion',False,URL('estudiante','agregar_preinscripcion')),
            ('Llenar Curriculum',False,URL('estudiante','llenar_curriculum')),
            ('Plan de Trabajo',False,URL('estudiante','plan_trabajo')),
            ('Retirar Pasantía',False,URL('estudiante','retirar_pasantia')),
            ('Solicitar permiso de inscripción extemporánea',False,"#"),
            ('Solicitar permiso de evaluación extemporánea',False,"#")
            ]),
        ('Profesor',False,"#",[
            ('Registrarse',False,URL('default','registrar_profesor')),
            ('Consultar pasantías',False,"#"),
            ('Evaluar Pasantía',False,"#")
            ]),
        ('Administrador',False,"#",[
            ('Gestionar Catálogos',False,URL('catalogos_grid','gestion_cct2'))
            ]),
        ('Coordinador',False,"#",[
            ('Especificar Configuraciones',False,URL('catalogos_grid','especificar_configuraciones'))
            ])
        ]

if DEVELOPMENT_MENU: _()

if "auth" in locals(): auth.wikimenu()
