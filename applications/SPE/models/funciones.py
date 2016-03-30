# Funciones disponibles en todo el codigo.

def captcha_field(request=request):
    from gluon.tools import Recaptcha2
    w = lambda x,y: Recaptcha2(request,
                              '6LeFHBwTAAAAAAgmUVpEbEz0NpYaJBIYYw709HIZ',
                              '6LeFHBwTAAAAANvgDFc2Dy257hQ8nux3ZgvdgS8Q')

    return Field('captcha', 'string', widget=w, default='ok')


def tiene_foto(usbid):
    import requests

    query =  dbSPE(dbSPE.usuario.usbid==usbid)
    foto  = query.select()[0].foto
    path = 'http://127.0.0.1:8000/SPE/static/profile_pictures/' + str(foto)
    r = requests.head(path)
    return dict(check=(r.status_code == requests.codes.ok),path=foto)

def validar_foto(form):
    if form.vars.image is not None:
        form.vars.image.imagename = str(auth.user.username) + ".jpg"

def guardar_imagen(image, imagename=None,path=None):
    import os
    import shutil
    path = "applications/SPE/static/profile_pictures"
    if not os.path.exists(path):
         os.makedirs(path)
    pathimagename = os.path.join(path, imagename)
    dest_file = open(pathimagename, 'wb')
    try:
            shutil.copyfileobj(image, dest_file)
    finally:
            dest_file.close()
    return imagename

def enviar_Correo_Verificacion(correo,codigoGenerado):

    if mail:
        mensaje1 = T("Su registro en el SPE ha sido exitoso, pero para poder utilizar" +
        " las funcionalidades del sistema debemos verificar que su la dirección " +
        "de correo electrónico suministrada es la correcta\n\n")
        mensaje2 = T("Cuando intente iniciar sesion en el sistema se le solicitara " +
        "el siguiente codigo:\n\n")
        mensaje3 = T('  Codigo De Activación ') + "'" + codigoGenerado + "' \n\n"
        mensaje4 = T("Una vez introducido el codigo su cuenta sera activada y podra " +
        "disfrutar nuestros servicios\n\n")
        mensaje5 = T("Este correo se ha enviado de manera automatica por el " +
        "Sistema Empresarial de Pasantias de la Universidad Simón Bolívar.\n\n")
        if mail.send(to=[correo],
            subject=T('Activacion'),
            message= (mensaje1 + mensaje2 + mensaje3 + mensaje4 + mensaje5)):
                response.flash = T('email sent sucessfully.')
                resultado = True
        else:
            response.flash = T('fail to send email sorry!')
    else:
        response.flash = T('Unable to send the email : email parameters not defined')
    return resultado

def generar_Correo_Verificacion(correo):
    import string
    import random
    from random import randint

    resultado = False

    size = randint(4,11)
    i = 0
    codigoGenerado = ''

    for i in range(0,size):
                codigoGenerado += random.choice(string.lowercase + string.uppercase + string.digits)

    dbSPE.correo_por_verificar.insert(correo = correo,codigo = codigoGenerado)

    enviar_Correo_Verificacion(correo,codigoGenerado)

def reenviar_Correo_Verificacion(correo):

    correoVerificarSet = dbSPE(dbSPE.correo_por_verificar.correo == request.vars.correo).select()

    codigoGenerado = correoVerificarSet[0].codigo

    enviar_Correo_Verificacion(correo,codigoGenerado)


def obtener_correo(usbid):
    usuario = dbSPE(dbSPE.usuario.usbid == usbid).select()[0]
    if usuario.tipo == "Docente":
        #Buscamos el email del profesor
        datosUsuario = dbSPE(dbSPE.usuario_profesor.usbid_usuario == usbid).select()[0]
    elif usuario.tipo == "Administrativo":
        pass
    elif usuario.tipo in ["Pregrado","Postgrado"]:
        #Buscamos el email del estudiante
        datosUsuario = dbSPE(dbSPE.usuario_estudiante.usbid_usuario == usbid).select()[0]
    elif usuario.tipo in ["Empleado","Organizacion","Egresado"]:
        pass

    return datosUsuario.email_sec
