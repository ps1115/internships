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
def retirar_pasantia():
    formulario1=FORM(INPUT(_name='Nombre'))
    formulario2=FORM(INPUT(_name='Carnet'))
    formulario3=FORM(INPUT(_name='Fecha'))
    formulario4=FORM(TEXTAREA(_name='Motivo'))
    return dict(formulario1=formulario1,formulario2=formulario2,formulario3=formulario3,formulario4=formulario4)

def permiso_inscripcion_extratemporaneo():
    return response.render('default/permiso_inscripcion_extratemporaneo.html')

def permiso_inscripcion_extratemporaneo():
    formulario1=FORM(INPUT(_name='Nombre'))
    formulario2=FORM(INPUT(_name='Carnet'))
    formulario3=FORM(INPUT(_name='Fecha'))
    formulario4=FORM(TEXTAREA(_name='Motivo'))
    return dict(formulario1=formulario1,formulario2=formulario2,formulario3=formulario3,formulario4=formulario4)

def permiso_evaluacion_extratemporaneo():
    return response.render('default/permiso_evaluacion_extratemporaneo.html')

def permiso_evaluacion_extratemporaneo():
    formulario1=FORM(INPUT(_name='Nombre'))
    formulario2=FORM(INPUT(_name='Carnet'))
    formulario3=FORM(INPUT(_name='Fecha'))
    formulario4=FORM(TEXTAREA(_name='Motivo'))
    return dict(formulario1=formulario1,formulario2=formulario2,formulario3=formulario3,formulario4=formulario4)

def cc():
    formulario1=FORM(INPUT(_name='Nombre'))
    formulario2=FORM(INPUT(_name='Carnet'))
    formulario3=FORM(INPUT(_name='Fecha'))
    formulario4=FORM(TEXTAREA(_name='Motivo'))
    return dict(formulario1=formulario1,formulario2=formulario2,formulario3=formulario3,formulario4=formulario4)

def justificar_retiro_profesor():
    return response.render('default/justificar_retiro_profesor.html')

def justificar_retiro_profesor():
    formulario1=FORM(INPUT(_name='Nombre'))
    formulario2=FORM(INPUT(_name='Carnet'))
    formulario3=FORM(INPUT(_name='Fecha'))
    formulario4=FORM(TEXTAREA(_name='Motivo'))
    return dict(formulario1=formulario1,formulario2=formulario2,formulario3=formulario3,formulario4=formulario4)

def justificar_retiro_empresa():
    return response.render('default/justificar_retiro_empresa.html')

def justificar_retiro_empresa():
    formulario1=FORM(INPUT(_name='Nombre'))
    formulario2=FORM(INPUT(_name='Carnet'))
    formulario3=FORM(INPUT(_name='Fecha'))
    formulario4=FORM(TEXTAREA(_name='Motivo'))
    return dict(formulario1=formulario1,formulario2=formulario2,formulario3=formulario3,formulario4=formulario4)

def permiso_inscripcion_extratemporaneo():
    grid=SQLFORM(db.contact, user_signature=False)
    return locals()
