
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
        generar_Correo_Verificacion(form_profesor.vars.email_sec)

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

        redirect(URL(c='default',f='verifyEmail', vars=dict(usbid= request.vars.usbid,correo=request.vars.email_sec)))

    return response.render('profesor/registrar_profesor.html',
        message='Por favor actualiza tus datos para continuar',
        form_profesor=form_profesor)

# Falta especificar que el usario sea profesor.
def justificar_retiro_profesor():
    # Argumentos son: codigo, año, periodo(nombre)
    pasantia=None
    if len(request.args)==4:
        field =[dbSPE.pasantia.motivo_retiro_tutor_academico]
        form = SQLFORM.factory(
            *field,submit_button='Subir Carta',
            separator=': ',
            buttons=['submit'],
            type='text',
            col3 = {'motivo':T('Motivo justificativo')}
            )

        if form.process().accepted:
            pasantia = dbSPE((dbSPE.pasantia.codigo==request.args[0]) &
                (dbSPE.pasantia.anio==request.args[1]) &
                (dbSPE.pasantia.periodo==request.args[2]) &
                (dbSPE.pasantia.id_estudiante==request.args[3])
                )
            pasantia.update(motivo_retiro_tutor_academico = request.vars.motivo_retiro_tutor_academico)
            response.flash = 'Actualizado el motivo'
            redirect(URL('justificacion_retiro_profesor/'+request.args[0]+'/'+request.args[1]+'/'+request.args[2]+'/'+request.args[3]))

        elif form.errors:
            response.flash = 'Error'

    else:
        pasantias = dbSPE((dbSPE.pasantia.id_tutor_academico==auth.user.username) &
            (dbSPE.pasantia.motivo_retiro_estudiante!=None)
        )

        opciones = []
        periodos = {}
        for p in pasantias.select():
            periodo = dbSPE.periodo(p.periodo)
            periodos[periodo.nombre] = p.periodo
            datos_estudiante = dbSPE(dbSPE.usuario_estudiante.usbid_usuario==p.id_estudiante).select()[0]
            opciones.append('['+p.codigo+'] '+periodo.nombre+' '+str(p.anio)+' '+p.titulo+' '+datos_estudiante.nombre+' '+datos_estudiante.apellido+' '+datos_estudiante.usbid)

        form = SQLFORM.factory(
            Field('pasantia', requires = IS_IN_SET(opciones)),submit_button='Buscar')
        if form.process().accepted:
            # Datos: codigo, periodo(nombre), año
            datos = form.vars.pasantia.split()
            datos[0] = datos[0][1:-1]
            redirect(URL('justificar_retiro_profesor/'+datos[0]+'/'+datos[2]+'/'+str(periodos[datos[1]])+'/'+datos[6]))

        elif form.errors:
            response.flash = 'Error'

    return dict(form=form)

def justificacion_retiro_profesor():
    pasantia = dbSPE((dbSPE.pasantia.codigo==request.args[0]) &
                (dbSPE.pasantia.anio==request.args[1]) &
                (dbSPE.pasantia.periodo==request.args[2]) &
                (dbSPE.pasantia.id_estudiante==request.args[3])
                ).select()[0]
    estudiante = dbSPE(dbSPE.usuario_estudiante.usbid_usuario==request.args[3]).select()[0]
    return dict(pasantia=pasantia,estudiante=estudiante)
