# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

from usbutils import get_ldap_data, random_key

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("¡Bienvenido!")
    return dict(message=T('Sistema de Pasantías Empresariales'))


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

def login_cas():
    if not request.vars.getfirst('ticket'):
        #redirect(URL('error'))
        pass
    try:
        import urllib2
        #ssl._create_default_https_context = ssl._create_unverified_context
        url = "https://secure.dst.usb.ve/validate?ticket="+\
              request.vars.getfirst('ticket') +\
              "&service=http%3A%2F%2F127.0.0.1%3A8000%2FSPE%2Fdefault%2Flogin_cas"

        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        the_page = response.read()

    except Exception, e:
        print e
        redirect(URL('error'))

    if the_page[0:2] == "no":
        redirect(URL('index'))
    else:
        # session.casticket = request.vars.getfirst('ticket')
        data  = the_page.split()
        usbid = data[1]

        print usbid
        tablaUsuario  = dbSPE.usuario

        #Esto nos indica si el usuario ha ingresado alguna vez al sistema
        consulta = dbSPE(tablaUsuario.usbid==usbid)
        clave = 1234

        if consulta.isempty():
            #Si es primera vez que ingresa al sistema
            clave   = random_key()         #Se genera una clave automatica
            us      = get_ldap_data(usbid) #Se leen los datos del CAS
            print "================== Begin"
            print "type      " + str(type(us))
            print "user_data " + str(us)
            print clave
            print "Empty"
        else:
            print "hay algo aqui"
        # if consulta.isempty():
        #     clave   = random_key()
        #     us      = get_ldap_data(usbid)
        #     print "================== Begin"
        #     print "type      " + str(type(us))
        #     print "user_data " + str(us)
        #
        #     # print "insertando"
        #     a = db.auth_user.insert(
        #         first_name = us.get('first_name'),
        #         last_name  = us.get('last_name'),
        #         username   = usbid,
        #         password   = db.auth_user.password.validate(clave)[0],
        #         email      = us.get('email'),
        #         f_cedula     = us['cedula'],
        #         f_telefono   = us['phone'],
        #         f_tipo       = us['tipo'],
        #     )
        #
        #     user = db(db.auth_user.username==usbid).select()[0]
        #     print us
        #     db.t_universitario.insert(
        #         f_usbid   = usbid,
        #         f_key     = clave,
        #         f_usuario = user.id
        #     )
        #
        #     userUniv = db(db.t_universitario.f_usbid==usbid).select()[0]
        #
        #     if (us['tipo'] == "Pregrado") or (us['tipo'] == "Postgrado"):
        #        # Si es estudiante insertar en su tabla
        #         db.t_estudiante.insert(
        #             f_universitario = userUniv.id,
        #             f_carrera       = us['carrera'],
        #             f_sede          = "Sartenejas"
        #         )
        #     elif us['tipo'] == "Docente":
        #         # En caso de ser docente, agregar dpto.
        #         db.t_tutor_academico.insert(
        #             f_universitario = userUniv.id,
        #             f_departamento  = us['dpto'],
        #             f_sede          = "Sartenejas"
        #         )
        #
        # else:
        #     userUniv = db(db.t_universitario.f_usbid==usbid).select()[0]
        #     clave    = userUniv.f_key
        #
        #
        # # Al finalizar login o registro, redireccionamos a home

        auth.login_bare(usbid,clave)
        redirect('index')

    return None

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
