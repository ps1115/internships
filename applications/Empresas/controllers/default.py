# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################


def index():

    response.flash = "Bienvenida Empresa"
    # return dict(message='Área de Empresas')
    return dict(form=login(),message="Empresas")

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

def login():

    formulario_login = SQLFORM.factory(
                            Field('login', label=T('Usuario o Correo Electronico'), required=True,
                                    requires=[IS_MATCH('^[a-zA-Z0-9.@_\\-]',error_message=T('Usuario o correo invalido.'))]),
                            Field('password', 'password',required=True,label=T('Contraseña')),
                           captcha_field(),
                           formstyle='bootstrap3_stacked'
                           )


    if formulario_login.process(onvalidation=validar_credenciales).accepted:
        # Buscamos el id de la empresa
        correoVerificarSet = dbSPE(dbSPE.correo_Por_Verificar.correo == request.vars.login).select()
        if correoVerificarSet:
            redirect(URL(c='default',f='verifyEmail',vars=dict(correo=request.vars.login, contrasena= request.vars.password)))
        else:
            auth.login_bare(request.vars.login,request.vars.password)
            redirect(URL(c='default',f='home'))
    else:
        response.flash = T("Usuario o Contraseña invalida.")
    return formulario_login

def verifyEmail():
    form = SQLFORM.factory(
        Field('codigo', label=T('Codigo De Verificacion'), required=True,
                requires=IS_NOT_EMPTY(error_message=T('Este campo es necesario'))),
                formstyle='bootstrap3_stacked'
                           )

    if form.process().accepted:
        # Buscamos el id de la empresa
        correoVerificarSet = dbSPE(dbSPE.correo_Por_Verificar.correo == request.vars.correo).select()
        if correoVerificarSet[0].codigo != request.vars.codigo:
            response.flash = T("Codigo incorrecto")
        else:
            dbSPE(dbSPE.correo_Por_Verificar.correo == request.vars.correo).delete()
            auth.login_bare(request.vars.correo,request.vars.contrasena)
            redirect(URL(c='default',f='home'))
    return form


def validar_credenciales(form):
    #Si es empresa, busco en la tabla por login
    login_empresa1  = dbSPE(dbSPE.empresa.log  == form.vars.login)
    #Si es tutor industrial, busco en la tabla por email
    login_tutor_ind = dbSPE(dbSPE.tutor_industrial.email  ==form.vars.login)

    #Solo puedo encontrar alguno de los dos, verifico el password
    if not login_empresa1.isempty():
        datosUsuario = login_empresa1.select()[0]
        if datosUsuario.password != form.vars.password:
            form.errors = "Usuario o contraseña invalida"
    elif not login_tutor_ind.isempty():
        datosUsuario = login_tutor_ind.select()[0]
        if datosUsuario.password != form.vars.password:
            form.errors = "Usuario o contraseña invalida"

def logout():
    url = (URL(c='default',f='index'))
    auth.logout(next=url)

def home():
    response.flash = T("Inicio Exitoso")
    return response.render('default/home.html')

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
