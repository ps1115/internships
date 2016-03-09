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

def registrar_profesor():
    return response.render('default/registrar_profesor.html')

def registrar_empresa():

    form = SQLFORM.factory(
                           Field(('Login'), rname='login',requires=IS_NOT_EMPTY(T('Campo Obligatorio'))),
                           Field(('Contrasena'),rname='contrasena' ,requires=IS_NOT_EMPTY(T('Campo Obligatorio'))),
                           Field(('Comfirmar Contrasena'),rname='Comfirmar_contrasena', requires=IS_NOT_EMPTY(T('Campo Obligatorio'))),
                           Field(('Pregunta Secreta'), requires=IS_NOT_EMPTY(T('Campo Obligatorio'))),
                           Field(('Respuesta A Pregunta Secreta'), requires=IS_NOT_EMPTY(T('Campo Obligatorio'))),
                           Field(('Nombre'), requires=IS_NOT_EMPTY(T('Campo Obligatorio'))),
                           Field(('Direccion'), requires=IS_NOT_EMPTY()),
                           Field(('Pagina Web'), requires=IS_NOT_EMPTY()),
                           Field(('Descripcion'), requires=IS_NOT_EMPTY()),
                           Field(('Telefono'), requires=IS_NOT_EMPTY()),
                           Field(('Contacto RRHH'), requires=[IS_NOT_EMPTY(error_message=T('Campo Obligatorio')),IS_EMAIL(error_message=T('Correo Invalido'))])
                          )
    # Aqui ira el proceso de crear a la empresa
    if form.process().accepted:
        pass
    return response.render('default/registrar_empresa.html',message=T("Registrar Empresa"),form=form)

def registrar_tutor_industrial():
    return response.render('default/registrar_tutor_industrial.html')
