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

        usuario = get_ldap_data(usbid) #Se leen los datos del CAS
        tablaUsuario  = dbSPE.usuario

        #Esto nos indica si el usuario ha ingresado alguna vez al sistema
        #buscandolo en la tabla de usuario.
        primeravez = dbSPE(tablaUsuario.usbid==usbid)

        if primeravez.isempty():
            #Si es primera vez que ingresa al sistema
            clave   = random_key()         #Se genera una clave automatica
            print "================== Begin"
            print "type      " + str(type(usuario))
            print "user_data " + str(usuario)
            print clave
            print "Empty"

            #Ingresamos al usuario en la tabla de Autenticacion
            # de la base de datos de Web2Py
            result = db.auth_user.insert(
                first_name = usuario.get('first_name'),
                last_name  = usuario.get('last_name'),
                username   = usbid,
                password   = db.auth_user.password.validate(clave)[0],
                email      = usuario.get('email')
            )

            #Ingresamos a la base de datos de Usuario
            resutl = tablaUsuario.insert(
                usbid    = usbid,
                nombre   = usuario.get('first_name'),
                apellido = usuario.get('last_name'),
                ci       = usuario.get('cedula'),
                tipo     = usuario.get('tipo'),
                llave    = clave
            )

            auth.login_bare(usbid,clave)
            redirect(URL(c='default',f='registrar', vars=dict(usuario=usuario)))

        else:
            #Como el usuario ya esta registrado, buscamos sus datos y lo logueamos.
            datosUsuario = dbSPE(tablaUsuario.usbid==usbid).select()[0]
            clave    = datosUsuario.llave

            auth.login_bare(usbid,clave)

            #Si el usuario no ha actualizado sus datos
            if verificar_datos(usuario).isempty():
                redirect(URL(c='default',f='registrar', vars=dict(usuario=usuario)))
            else:
                #Deberiamos redireccionar a un "home" dependiendo del tipo de usuario
                redirect('index')

    return None

def logout():
    url = (URL(c='default',f='index'))
    auth.logout(next=url)

def verificar_datos(usuario):

    consulta = None
    usbid = usuario.get('usbid')

    if usuario['tipo'] == "Docente":
        consulta = dbSPE(dbSPE.usuario_profesor.usbid_usuario==usbid)
    elif usuario['tipo'] == "Administrativo":
        pass
    elif usuario['tipo'] in ["Pregrado","Postgrado"]:
        consulta = dbSPE(dbSPE.usuario_estudiante.usbid_usuario==usbid)
    elif usuario['tipo'] in ["Empleado","Organizacion","Egresado"]:
        pass

    print "consulta " + str(consulta)
    return consulta

def registrar():
        #Aqui estan las variables obtenidas por el CAS
        usuario = request.vars['usuario']
        print(auth.is_logged_in())

        #temporal
        return dict(message=T(usuario))

        if usuario['tipo'] == "Docente":
            #Codigo para registrar docente
            pass
        elif usuario['tipo'] == "Administrativo":
            pass
        elif usuario['tipo'] in ["Pregrado","Postgrado"]:
            #Codigo para registar usuario
            pass
        elif usuario['tipo'] in ["Empleado","Organizacion","Egresado"]:
            pass

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
