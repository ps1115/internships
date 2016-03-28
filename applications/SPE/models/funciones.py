# Funciones disponibles en todo el codigo.

def captcha_field(request=request):
    from gluon.tools import Recaptcha2
    w = lambda x,y: Recaptcha2(request,
                              '6Lcg5hoTAAAAADfqPDXf4htFpyjqkBGRID3KiLEP',
                              '6Lcg5hoTAAAAANYiBEtWC1NSG5nEMZcHMgC4_eIT')

    return Field('captcha', 'string', widget=w, default='ok')


def tiene_foto(usbid):
    import requests

    query =  dbSPE(dbSPE.usuario.usbid==usbid)
    foto  = query.select()[0].foto
    path = 'http://127.0.0.1:8000/SPE/static/profile_pictures/' + str(foto)
    r = requests.head(path)
    print(r.status_code == requests.codes.ok)
    return dict(check=(r.status_code == requests.codes.ok),path=foto)

def validar_foto(form):
    if form.vars.image is not None:
        print "hello world"
        form.vars.image.imagename = str(auth.user.username) + ".jpg"

def guardar_imagen(image, imagename=None,path=None):
    import os
    import shutil
    path = "applications/SPE/static/profile_pictures"
    if not os.path.exists(path):
         os.makedirs(path)
    print imagename
    pathimagename = os.path.join(path, imagename)
    dest_file = open(pathimagename, 'wb')
    try:
            shutil.copyfileobj(image, dest_file)
    finally:
            dest_file.close()
    return imagename

def enviar_Correo_Verificacion(correo):
    import string
    import random
    from random import randint

    resultado = False

    size = randint(4,11)
    i = 0
    codigoGenerado = ''

    for i in range(0,size):
                codigoGenerado += random.choice(string.lowercase + string.uppercase + string.digits)

    dbSPE.correo_Por_Verificar.insert(correo = correo,codigo = codigoGenerado)

    if mail:
        if mail.send(to=[correo],
            subject=T('Activacion'),
            message= T('Codigo De Activacion ') + codigoGenerado):
                response.flash = T('email sent sucessfully.')
                resultado = True
        else:
            response.flash = T('fail to send email sorry!')
    else:
        response.flash = T('Unable to send the email : email parameters not defined')
    return resultado

def reenviar_Correo_Verificacion(correo):

    correoVerificarSet = dbSPE(dbSPE.correo_Por_Verificar.correo == request.vars.correo).select()

    codigoGenerado = correoVerificarSet[0].codigo

    if mail:
        if mail.send(to=[request.vars.correo],
            subject=T('Activacion'),
            message= 'Codigo De Activacion ' + codigoGenerado):
                response.flash = 'email sent sucessfully.'
                resultado = True
        else:
            response.flash = 'fail to send email sorry!'
    else:
        response.flash = 'Unable to send the email : email parameters not defined'


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
