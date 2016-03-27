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

            #Ingresamos al usuario en la tabla de Autenticacion
            # de la base de datos de Web2Py
            result = db.auth_user.insert(
                first_name = usuario.get('first_name'),
                last_name  = usuario.get('last_name'),
                username   = usbid,
                password   = db.auth_user.password.validate(clave)[0],
                email      = usuario.get('email'),
                user_Type  = usuario.get('tipo')
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
            clave        = datosUsuario.llave

            auth.login_bare(usbid,clave)

            #Si el usuario no ha actualizado sus datos
            if verificar_datos(usuario,usbid).isempty():
                redirect(URL(c='default',f='registrar', vars=dict(usuario=usuario)))
            elif correo_no_verificado(usbid):
                redirect(URL(c='default',f='verifyEmail'))
            else:
                #Deberiamos redireccionar a un "home" dependiendo del tipo de usuario
                redirect('index')

    return None

def logout():
    url = 'http://secure.dst.usb.ve/logout'
    auth.logout(next=url)

def verificar_datos(usuario,usbid):

    consulta = None

    if usuario['tipo'] == "Docente":
        consulta = dbSPE(dbSPE.usuario_profesor.usbid_usuario==usbid)
    elif usuario['tipo'] == "Administrativo":
        pass
    elif usuario['tipo'] in ["Pregrado","Postgrado"]:
        consulta = dbSPE(dbSPE.usuario_estudiante.usbid_usuario==usbid)
    elif usuario['tipo'] in ["Empleado","Organizacion","Egresado"]:
        pass

    return consulta

def registrar():

    import ast
    #Aqui estan las variables obtenidas por el CAS
    usuario =  ast.literal_eval(request.vars['usuario'])

    if usuario['tipo'] == "Docente":
        #Enviar al registro del profesor
        pass
    elif usuario['tipo'] == "Administrativo":
        pass
    elif usuario['tipo'] in ["Pregrado","Postgrado"]:
        redirect(URL(c='estudiante',f='registrar_estudiante', vars=dict(usuario=usuario)))
    elif usuario['tipo'] in ["Empleado","Organizacion","Egresado"]:
        pass

    return dict(message=usuario)

#Comprueba si el usuario no ha verificado su correo
def correo_no_verificado(usbid):

    correoUsuario = obtener_correo(usbid)
    buscarCorreo  = dbSPE(dbSPE.correo_Por_Verificar.correo==correoUsuario)

    return not(buscarCorreo.isempty())

#Reenvia la verificacion del correo
def resendVerificationEmail():

    correo_usuario = obtener_correo(auth.user.username)
    correoVerificarSet = dbSPE(dbSPE.correo_Por_Verificar.correo == correo_usuario).select()

    codigoGenerado = correoVerificarSet[0].codigo

    if mail:
        if mail.send(to=[correo_usuario],
            subject=T('Activacion'),
            message= 'Codigo De Activacion ' + codigoGenerado):
                response.flash = 'email sent sucessfully.'
                resultado = True
        else:
            response.flash = 'fail to send email sorry!'
    else:
        response.flash = 'Unable to send the email : email parameters not defined'
    return response.render('default/codigoReenviado.html',message=T("Verificacion de Correo"),vars=dict(correo=correo_usuario))

#Verifica el correo
def verifyEmail():
    form = SQLFORM.factory(
        Field('codigo', label=T('Codigo De Verificacion'), required=True,
                requires=IS_NOT_EMPTY(error_message=T('Este campo es necesario'))),
                formstyle='bootstrap3_stacked'
                           )
    form.add_button(T('Send Email Again'), URL(c='default',f='resendVerificationEmail',vars=dict(correo=request.vars.correo)))

    correo_usuario = obtener_correo(auth.user.username)

    if form.process().accepted:
        # Buscamos el id de la empresa
        correoVerificarSet = dbSPE(dbSPE.correo_Por_Verificar.correo == correo_usuario).select()[0]
        if correoVerificarSet.codigo != request.vars.codigo:
            response.flash = T("Codigo incorrecto")
        else:
            dbSPE(dbSPE.correo_Por_Verificar.correo == correo_usuario).delete()
            #auth.login_bare(request.vars.correo,contrasena)
            redirect(URL(c='default',f='index'))

    return response.render('default/codigoVerificacion.html',message=T("Verificacion de Correo"),form=form,vars=dict(correo=correo_usuario))


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

def registrar_profesor():
    return response.render('default/registrar_profesor.html')
