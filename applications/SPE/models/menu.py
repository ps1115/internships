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
    (SPAN(' ', _class='fa fa-home fa-lg'), False, URL(c='default', f='index'))
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
        (SPAN(' Cerrar Sesión', _class='fa fa-sign-out'), False, URL('default','logout'))
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
<<<<<<< HEAD

    # Entradas del menu si el usuario esta autenticado
    if auth.is_logged_in():
        if auth.user.user_Type == 'Pregrado' or auth.user.user_Type == 'Postgrado':
            response.menu += [('Estudiante',False,"#",[
                ('Agregar Preinscripcion',False,URL('estudiante','agregar_preinscripcion')),
                ('Llenar Curriculum',False,URL('estudiante','llenar_curriculum')),
                ('Plan de Trabajo',False,URL('estudiante','plan_trabajo')),
                ('Retirar Pasantía',False,URL('estudiante','retirar_pasantia')),
                ('Solicitar permiso de inscripción extemporánea',False,"#"),
                ('Solicitar permiso de evaluación extemporánea',False,"#")
                ])]
        elif auth.user.user_Type == 'Docente':
            response.menu += [
            ('Profesor',False,"#",[
                ('Registrarse',False,URL('default','registrar_profesor')),
                ('Evaluar Pasantía',False,"#"),
                ('Retiro Pasantia',False,URL('profesor','justificar_retiro_profesor'))
                ])
                ]
        elif auth.user.user_Type == 'Administrativo':
            response.menu += [('Administrador',False,"#",[
                ('Gestionar Catálogos',False,URL('catalogos_grid','gestion_cct2'))
                ])]
        else:
            pass
    else:
        response.menu += [ #Coloque esto porque el cas no me funciona
            (T('Iniciar Sesion'),False,'#',[
                (T('Miembro USB'),False,"https://secure.dst.usb.ve/login?service=http%3A%2F%2F127.0.0.1%3A8000%2FSPE%2Fdefault%2Flogin_cas"),
                (T('Empresa'),False,URL(a='Empresas',c='default',f='index'))
                ]),
            ('Administrador',False,"#",[
                ('Gestionar Catálogos',False,URL('catalogos_grid','gestion_cct2'))
                ]),
            ('Coordinador',False,"#",[
                ('Especificar Configuraciones',False,URL('catalogos_grid','especificar_configuraciones'))
                ])
=======
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
            ('Solicitar permiso de inscripción extemporánea',False,URL('estudiante', 'permiso_inscripcion')),
            ('Solicitar permiso de evaluación extemporánea',False,URL('estudiante', 'permiso_evaluacion'))
            ]),
        ('Profesor',False,"#",[
            ('Registrarse',False,URL('default','registrar_profesor')),
            ('Consultar pasantías',False,"#"),
            ('Evaluar Pasantía',False,"#"),
            ('Justificar Retiro Pasante',False,URL('profesor','justificar_retiro_profesor'))
            ]),
        ('Administrador',False,"#",[
            ('Gestionar Catálogos',False,URL('catalogos_grid','gestion_cct2'))
            ]),
        ('Coordinador',False,"#",[
            ('Especificar Configuraciones',False,URL('catalogos_grid','especificar_configuraciones'))
            ])
>>>>>>> syq
        ]

if DEVELOPMENT_MENU: _()

if "auth" in locals(): auth.wikimenu()
