# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Bienvenido a SPE!")
    return dict(message=T('Pagina modelo'))


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

def retirar_pasantia():
    return response.render('default/retirar_pasantia.html')


def crear_estudiante():
    form = SQLFORM(db.usuario_estudiante)
    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    
    return form



def crear_profesor():
    form = SQLFORM(db.usuario_profesor)
    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    
    return form


def crear_empresa():
    form = SQLFORM(db.empresa)
    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    
    return form


def crear_departamento():
    form = SQLFORM(db.departamento)
    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    
    return form


def crear_carrera():
    form = SQLFORM(db.carrera)
    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    
    return form


def estudiantes():
    grid = SQLFORM.grid(db.usuario_estudiante,user_signature=False)
    return grid

def carreras():
    grid = SQLFORM.grid(db.carrera,user_signature=False)
    return grid

def empresas():
    grid = SQLFORM.grid(db.empresa,user_signature=False)
    return grid

def profesores():
    grid = SQLFORM.grid(db.usuario_profesor,user_signature=False)
    return grid

def departamentos():
    grid = SQLFORM.grid(db.departamento,user_signature=False)
    return grid

def gestion_cct2():
    return dict()

def especificar_configuraciones():
    return dict()

def roles():
    grid = SQLFORM.grid(db.rol_sistema,user_signature=False)
    return grid

def montos():
    grid = SQLFORM.grid(db.calculo_pago,user_signature=False)
    return grid

def eventos():
    grid = SQLFORM.grid(db.evento,user_signature=False,
                        deletable=False,searchable=False,
                       csv=False)
    return grid

def sub_evento():
    grid = SQLFORM.grid(db.sub_evento,user_signature=False,
                        deletable=False,searchable=False,
                       csv=False)
    return grid

def semana_muerta():
    grid = SQLFORM.grid(db.semana_muerta,user_signature=False,
                        deletable=False,searchable=False,
                       csv=False)
    return grid
