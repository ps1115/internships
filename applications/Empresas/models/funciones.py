# Funciones disponibles en todo el codigo.

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
