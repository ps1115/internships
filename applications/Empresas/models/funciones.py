# Funciones disponibles en todo el codigo.

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

    dbSPE.correo_Por_Verificar.insert(correo = correo,codigo = codigoGenerado)

    enviar_Correo_Verificacion(correo,codigoGenerado)

def reenviar_Correo_Verificacion(correo):

    correoVerificarSet = dbSPE(dbSPE.correo_Por_Verificar.correo == request.vars.correo).select()

    codigoGenerado = correoVerificarSet[0].codigo

    enviar_Correo_Verificacion(correo,codigoGenerado)

def captcha_field(request=request):
    from gluon.tools import Recaptcha2
    w = lambda x,y: Recaptcha2(request,
                              '6Lcg5hoTAAAAADfqPDXf4htFpyjqkBGRID3KiLEP',
                              '6Lcg5hoTAAAAANYiBEtWC1NSG5nEMZcHMgC4_eIT')

    return Field('captcha', 'string', widget=w, default='ok')
