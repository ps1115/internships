# -*- coding: utf-8 -*-

def registrar_profesor():

    import ast
    #Aqui estan las variables obtenidas por el CAS
    usuario =  ast.literal_eval(request.vars['usuario'])

    #Llenamos el formulario con el default
    dbSPE.usuario_profesor.usbid_usuario.default  = request.vars.usbid

    # Agregamos el resto de los campos
    fields = [
        dbSPE.usuario_profesor.usbid_usuario,
        dbSPE.usuario_profesor.dependencia,
        dbSPE.usuario_profesor.dedicacion,
        dbSPE.usuario_profesor.categoria,
        dbSPE.usuario_profesor.email_sec,
        dbSPE.usuario_profesor.telf,
        dbSPE.usuario_profesor.celular
        ]
    # Generamos el SQLFORM utilizando los campos
    form_profesor = SQLFORM.factory(
    captcha_field(),
    *fields,
    formstyle='bootstrap3_stacked',
    separator=': ',
    submit_button="Actualizar Datos",
    buttons=['submit'],
    col3 = {'usbid_usuario':T(''),
            'dependencia':T(''),
            'dedicacion':T(''),
            'categoria':T(''),
            'email_sec':T('Correo Secundario'),
            'telf':T('Numero de telefono fijo'),
            'celular':T('Numero de telefono movil'),
            'activo':T('Estado del profesor')}
    )

    if form_profesor.process().accepted:
        enviar_Correo_Verificacion(form_profesor.vars.email_sec)

        # Registramos la empresa
        dbSPE.usuario_profesor.insert(
                            usbid_usuario = request.vars.usbid,
                            dependencia = request.vars.dependencia,
                            dedicacion = request.vars.dedicacion,
                            categoria = request.vars.categoria,
                            email_sec = request.vars.email_sec,
                            telf = request.vars.telf,
                            celular = request.vars.celular,
                            activo = 1)

        redirect(URL(c='default',f='verifyEmail'))

    return response.render('profesor/registrar_profesor.html',
        message='Por favor actualiza tus datos para continuar',
        form_profesor=form_profesor)

def justificar_retiro_profesor():
    # Este query debe ser remplazado por el correcto
    # Buscar las pasantias segun el id del usuario(estudiante)
    pasantias = dbSPE(dbSPE.pasantia.periodo == 77)
    pasantia = pasantias.select()[0]

    form = SQLFORM.factory(
        Field('pasantia',
            requires=IS_IN_SET(pasantias.select(
                dbSPE.pasantia.codigo, dbSPE.pasantia.periodo,
                dbSPE.pasantia.anio
                ))))

    if form.process().accepted:
        # Esto esta para dar la idea del flujo, pero debe
        # ser remplazado por el formulario correcto
        field =[dbSPE.pasantia.motivo_retiro_tutor_academico]
        form = SQLFORM.factory(
        *field,submit_button='Subir Carta',
        separator=': ',
        buttons=['submit'],
        col3 = {'motivo':T('Motivo justificativo')}
        )

        if form.process().accepted:
            (dbSPE.pasantia.codigo == 'PS1110').update(motivo_retiro_tutor_academico = request.vars.motivo)
            response.flash = 'form accepted'
        elif form.errors:
            response.flash = 'form has errors'
        else:
            response.flash = 'please fill out the form'

    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form)

#def justificar_retiro_profesor():
#    return response.render('profesor/justificar_retiro_profesor.html')
