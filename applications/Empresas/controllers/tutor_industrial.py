# -*- coding: utf-8 -*-

# Proceso de registro en el cual un tutor solicita un registro a una empresa
def solicitar_registro_tutor():
    dbSPE.tutor_industrial.email.requires += [IS_NOT_IN_DB(dbSPE, 'empresa.log',error_message=T('Correo No Disponible'))]
    # Agregamos los campos en el orden deseado, comenzamos con el login y el password
    fields =[
       dbSPE.tutor_industrial.email,
        dbSPE.tutor_industrial.nombre,
        dbSPE.tutor_industrial.apellido,
        dbSPE.tutor_industrial.ci,
        dbSPE.tutor_industrial.password
    ]
    # Agregamos un campo extra de comfirm password el cual debera tener el mismo valor que el password para ser aceptado
    fields += [Field('comfirm_Password','password', label=T('Comfirm Password'),
                     requires = [IS_EXPR('value==%s' % repr(request.vars.password),error_message=T('Las contraseñas no coinciden'))])]
    # Agregamos el resto de los campos
    fields +=[
        dbSPE.tutor_industrial.id_empresa,
        dbSPE.tutor_industrial.pregunta_secreta,
        dbSPE.tutor_industrial.respuesta_pregunta_secreta,
        dbSPE.tutor_industrial.profesion,
        dbSPE.tutor_industrial.cargo,
        dbSPE.tutor_industrial.departamento,
        dbSPE.tutor_industrial.id_pais,
        dbSPE.tutor_industrial.id_estado,
        dbSPE.tutor_industrial.id_universidad,
        dbSPE.tutor_industrial.direccion,
        dbSPE.tutor_industrial.telefono
    ]
    # Generamos el SQLFORM utilizando los campos
    form = SQLFORM.factory(
    captcha_field(),
    *fields,
    submit_button='Submit',
    separator=': ',
    buttons=['submit'],
    col3 = {'email':T('Identificación de acceso unica asignada a la empresa'),
            'nombre':T('Nombre comercial de la empresa'),
            'apellido':T('Nombre comercial de la empresa'),
            'ci':T('Nombre comercial de la empresa'),
            'password':T('Contraseña para acceder al sistema'),
            'comfirm_Password':T('Repita su contraseña'),
            'pregunta_secreta':T('Si necesita obtener de nuevo su contraseña se le hara esta pregunta'),
            'respuesta_pregunta_secreta':T('Respuesta a su pregunta secreta'),
            'id_empresa':T('Empresa en la que trabaja'),
            'profesion':T('Profesion del tutor industrial'),
            'cargo':T('Cargo que ocupa en la empresa'),
            'departamento':T('Departamento de la empresa en la que trabaja'),
            'direccion':T('Direccion del tutor industrial'),
            'id_pais':T('Pais en el que se encuentra domiciliado el tutor industrial'),
            'id_estado':T('Estado en el que se encuentra domiciliado el tutor industrial'),
            'id_universidad':T('Universidad de la cual egreso el tutor'),
            'telefono':T('Numerico telefonico del tutor industrial')
           })
    # Caso 1: El form se lleno de manera correcta asi que registramos al tutor y procedemos a la pagina de exito
    if form.process().accepted:

        # Registramos la empresa
        dbSPE.tutor_industrial.insert(
            email = request.vars.email,
            nombre = request.vars.nombre,
            apellido = request.vars.apellido,
            ci = request.vars.ci,
            password = request.vars.password,
            pregunta_secreta = request.vars.pregunta_secreta,
            respuesta_pregunta_secreta = request.vars.respuesta_pregunta_secreta,
            id_empresa = request.vars.id_empresa,
            profesion = request.vars.profesion,
            cargo = request.vars.cargo,
            departamento = request.vars.departamento,
            direccion = request.vars.direccion,
            id_estado = request.vars.id_estado,
            id_pais = request.vars.id_pais,
            id_universidad = request.vars.id_universidad,
            telefono = request.vars.telefono)

        #Insertamos en la tabla user de Web2py
        result = db.auth_user.insert(
            first_name = request.vars.nombre,
            last_name  = request.vars.apellido,
            username   = request.vars.email,
            password   = db.auth_user.password.validate(request.vars.password)[0],
            email      = request.vars.email,
            user_Type  = 'tutor_industrial'
        )

        generar_Correo_Verificacion(request.vars.email)

        empresaSet = dbSPE(dbSPE.empresa.id == request.vars.id_empresa).select()
        empresa = empresaSet[0].nombre

        paisSet = dbSPE(dbSPE.pais.id == request.vars.id_pais).select()
        pais = paisSet[0].nombre

        estadoSet = dbSPE(dbSPE.estado.id == request.vars.id_estado).select()
        estado = estadoSet[0].nombre

        universidadSet = dbSPE(dbSPE.universidad.id == request.vars.id_universidad).select()
        universidad = universidadSet[0].nombre

        # Mensaje de exito
        response.flash = T("Registro Exitoso")
        # Nos dirigimos a la pagina de exito
        return response.render('tutor_industrial/registrarTutorIndustrial/registro_tutor_industrial_exitoso.html',message=T("Registrarse como Tutor Industrial"),
                               result=T("El registro de su tutor ha sido exitoso!"),
                               email = request.vars.email,
                               nombre = request.vars.nombre,
                               apellido = request.vars.apellido,
                               ci = request.vars.ci,
                               empresa = empresa, # Cableado mientras se resuelven problemas
                               profesion = request.vars.profesion,
                               cargo = request.vars.cargo,
                               departamento = request.vars.departamento,
                               direccion = request.vars.direccion,
                               estado = estado, #Estara asi hasta que se implemente la tabla estado
                               pais = pais, #Estara asi hasta que se implemente la tabla estado
                               universidad = universidad,
                               telefono = request.vars.telefono)
    # Caso 2: El form no se lleno de manera correcta asi que recargamos la pagina
    else:
        return response.render('tutor_industrial/registrarTutorIndustrial/registrar_tutor_industrial.html',message=T("Registrarse como Tutor Industrial"),form=form)

# -*- coding: utf-8 -*-

def justificar_retiro_empresa():
    # Argumentos son: codigo, año, periodo(nombre)
    pasantia=None
    if len(request.args)==4:
        pasantia = dbSPE((dbSPE.pasantia.codigo==request.args[0]) &
                (dbSPE.pasantia.anio==request.args[1]) &
                (dbSPE.pasantia.periodo==request.args[2]) &
                (dbSPE.pasantia.id_estudiante==request.args[3])
                ).select()[0]
        field =[dbSPE.pasantia.motivo_retiro_tutor_industrial]
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
            pasantia.update(motivo_retiro_tutor_industrial = request.vars.motivo_retiro_tutor_industrial)
            response.flash = 'Actualizado el motivo'
            redirect(URL('justificacion_retiro_empresa/'+request.args[0]+'/'+request.args[1]+'/'+request.args[2]+'/'+request.args[3]))

        elif form.errors:
            response.flash = 'Error'

    else:
        pasantias = dbSPE((dbSPE.pasantia.id_tutor_industrial==auth.user.username) &
            (dbSPE.pasantia.motivo_retiro_estudiante!=None)
        )

        opciones = []
        periodos = {}
        pasantias2 = {}
        for p in pasantias.select():
            periodo = dbSPE.periodo(p.periodo)
            periodos[periodo.nombre] = p.periodo
            datos_estudiante = dbSPE(dbSPE.usuario.usbid==p.id_estudiante).select()[0]
            opciones.append('['+p.codigo+'] '+periodo.nombre+' '+str(p.anio)+' '+p.titulo+' '+datos_estudiante.nombre+' '+datos_estudiante.apellido+' '+datos_estudiante.usbid)
            pasantias2[opciones[-1]] = p

        form = SQLFORM.factory(
            Field('pasantia', requires = IS_IN_SET(opciones)),submit_button='Buscar')
        if form.process().accepted:
            # Datos: codigo, periodo(nombre), año
            # datos = form.vars.pasantia.split()
            # datos[0] = datos[0][1:-1]
            pasantia = pasantias2[form.vars.pasantia]
            redirect(URL('justificar_retiro_empresa/'+str(pasantia.codigo)+'/'+str(pasantia.anio)+'/'+str(pasantia.periodo)+'/'+str(pasantia.id_estudiante)))

        elif form.errors:
            response.flash = 'Error'

    return dict(form=form,pasantia=pasantia)

def justificacion_retiro_empresa():
    pasantia = dbSPE((dbSPE.pasantia.codigo==request.args[0]) &
                (dbSPE.pasantia.anio==request.args[1]) &
                (dbSPE.pasantia.periodo==request.args[2]) &
                (dbSPE.pasantia.id_estudiante==request.args[3])
                ).select()[0]
    estudiante = dbSPE(dbSPE.usuario.usbid==request.args[3]).select()[0]
    return dict(pasantia=pasantia,estudiante=estudiante)