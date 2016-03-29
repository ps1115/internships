# -*- coding: utf-8 -*-

# Proceso de registro de empresa por medio de la opcion Empresa -> Registrarse, en el Index
def registrar_empresa():
    dbSPE.empresa.log.requires += [IS_NOT_IN_DB(dbSPE, 'tutor_industrial.email',error_message=T('Login No Disponible'))]
    # Agregamos los campos en el orden deseado, comenzamos con el login y el password
    fields = [dbSPE.empresa.log,dbSPE.empresa.password]
    # Agregamos un campo extra de comfirm password el cual debera tener el mismo valor que el password para ser aceptado
    fields += [Field('comfirm_Password','password', label=T('Comfirm Password'),
                     requires = [IS_EXPR('value==%s' % repr(request.vars.password),error_message=T('Las contraseñas no coinciden'))])]
    # Agregamos el resto de los campos
    fields += [
        dbSPE.empresa.pregunta_secreta,
        dbSPE.empresa.respuesta_pregunta_secreta,
        dbSPE.empresa.nombre,
        dbSPE.empresa.id_pais,
        dbSPE.empresa.id_estado,
        dbSPE.empresa.id_area_laboral,
        dbSPE.empresa.direccion,
        dbSPE.empresa.pag_web,
        dbSPE.empresa.descripcion,
        dbSPE.empresa.telefono,
        dbSPE.empresa.contacto_RRHH
        ]
    # Generamos el SQLFORM utilizando los campos
    form = SQLFORM.factory(
    captcha_field(),
    *fields,
    submit_button='Submit',
    separator=': ',
    buttons=['submit'],
    col3 = {'log':T('Identificación de acceso unica asignada a la empresa'),
            'password':T('Contraseña para acceder al sistema'),
            'comfirm_Password':T('Repita su contraseña'),
            'pregunta_secreta':T('Si necesita obtener de nuevo su contraseña se le hara esta pregunta'),
            'respuesta_pregunta_secreta':T('Respuesta a su pregunta secreta'),
            'nombre':T('Nombre comercial de la empresa'),
            'id_pais':T('Pais en el que se encuentra la empresa'),
            'id_estado':T('Estado del pais en el que se encuentra'),
            'id_area_laboral':T('Area Laboral de la Empresa'),
            'direccion':T('Direccion de las instalaciones de la empresa'),
            'pag_web':T('Pagina Web de la empresa'),
            'descripcion':T('Descripcion breve de la empresa, su vision y sus funciones'),
            'telefono':T('Numero telefonico de contacto de la empresa'),
            'contacto_RRHH':T('Correo de contacto del departamento de recursos humanos de la empresa')}
    )

    # Caso 1: El form se lleno de manera correcta asi que registramos la empresa y procedemos a la pagina de exito
    if form.process().accepted:
        # Registramos la empresa
        dbSPE.empresa.insert(log = request.vars.log,
                             password = request.vars.password,
                             pregunta_secreta = request.vars.pregunta_secreta,
                             respuesta_pregunta_secreta = request.vars.respuesta_pregunta_secreta,
                             nombre = request.vars.nombre,
                             id_pais = request.vars.id_pais,
                             id_estado = request.vars.id_estado,
                             id_area_laboral = request.vars.id_area_laboral,
                             direccion = request.vars.direccion,
                             pag_web = request.vars.pag_web,
                             descripcion = request.vars.descripcion,
                             telefono = request.vars.telefono,
                             contacto_RRHH = request.vars.contacto_RRHH)

        #Insertamos en la tabla User de Web2py, para el login

        auth.get_or_create_user({
            "username":request.vars.log,
            "first_name":request.vars.nombre,
            "password":db.auth_user.password.validate(request.vars.password)[0],
            "email":request.vars.contacto_RRHH,
            "user_Type":'empresa'})

        generar_Correo_Verificacion(request.vars.log)

        paisSet = dbSPE(dbSPE.pais.id == request.vars.id_pais).select()
        pais = paisSet[0].nombre

        estadoSet = dbSPE(dbSPE.estado.id == request.vars.id_estado).select()
        estado = estadoSet[0].nombre

        arealaboralSet = dbSPE(dbSPE.area_laboral.id == request.vars.id_area_laboral).select()
        area_laboral = arealaboralSet[0].nombre

        # Mensaje de exito
        response.flash = T("Registro Exitoso")
        # Nos dirigimos a la pagina de exito
        return response.render('empresa/registrarEmpresa/registro_empresa_exitoso.html',message=T("Registrar Empresa"),
                               result=T("El registro de su empresa ha sido exitoso!"),
                               log=request.vars.log,
                               nombre=request.vars.nombre,
                               direccion=request.vars.direccion,
                               pais = pais,
                               estado = estado,
                               area_laboral = area_laboral,
                               pag_web=request.vars.pag_web,
                               descripcion=request.vars.descripcion,
                               telefono=request.vars.telefono,
                               contacto_RRHH=request.vars.contacto_RRHH,
                               pregunta_secreta=request.vars.pregunta_secreta,
                               respuesta_pregunta_secreta=request.vars.respuesta_pregunta_secreta)
    # Caso 2: El form no se lleno de manera correcta asi que recargamos la pagina
    else:
        return response.render('empresa/registrarEmpresa/registrar_empresa.html',message=T("Registrar Empresa"),form=form)

def registrar_tutor_industrial():
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
        dbSPE.tutor_industrial.pregunta_secreta,
        dbSPE.tutor_industrial.respuesta_pregunta_secreta,
        dbSPE.tutor_industrial.profesion,
        dbSPE.tutor_industrial.cargo,
        dbSPE.tutor_industrial.departamento,
        dbSPE.tutor_industrial.direccion,
        dbSPE.tutor_industrial.id_pais,
        dbSPE.tutor_industrial.id_estado,
        dbSPE.tutor_industrial.id_universidad,
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
        # Buscamos el id de la empresa
        empresaRegistradoraSet = dbSPE(dbSPE.empresa.log == auth.user.username).select()
        empresaRegistradora = empresaRegistradoraSet[0]
        # Registramos la empresa
        dbSPE.tutor_industrial.insert(
            email = request.vars.email,
            nombre = request.vars.nombre,
            apellido = request.vars.apellido,
            ci = request.vars.ci,
            password = request.vars.password,
            pregunta_secreta = request.vars.pregunta_secreta,
            respuesta_pregunta_secreta = request.vars.respuesta_pregunta_secreta,
            id_empresa = empresaRegistradora.id,
            profesion = request.vars.profesion,
            cargo = request.vars.cargo,
            departamento = request.vars.departamento,
            direccion = request.vars.direccion,
            id_pais = request.vars.id_pais,
            id_estado = request.vars.id_estado,
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

        paisSet = dbSPE(dbSPE.pais.id == request.vars.id_pais).select()
        pais = paisSet[0].nombre

        estadoSet = dbSPE(dbSPE.estado.id == request.vars.id_estado).select()
        estado = estadoSet[0].nombre

        universidadSet = dbSPE(dbSPE.universidad.id == request.vars.id_universidad).select()
        universidad = universidadSet[0].nombre

        # Mensaje de exito
        response.flash = T("Registro Exitoso")
        # Nos dirigimos a la pagina de exito
        return response.render('empresa/registrarTutorIndustrial/registro_tutor_industrial_exitoso.html',message=T("Registrar Tutor Industrial"),
                               result=T("El registro de su tutor ha sido exitoso!"),
                               email = request.vars.email,
                               nombre = request.vars.nombre,
                               apellido = request.vars.apellido,
                               ci = request.vars.ci,
                               empresa = empresaRegistradora.nombre, # Cableado mientras se resuelven problemas
                               profesion = request.vars.profesion,
                               cargo = request.vars.cargo,
                               departamento = request.vars.departamento,
                               direccion = request.vars.direccion,
                               pais = pais,
                               estado = estado,
                               universidad = universidad,
                               telefono = request.vars.telefono)
    # Caso 2: El form no se lleno de manera correcta asi que recargamos la pagina
    else:
        return response.render('empresa/registrarTutorIndustrial/registrar_tutor_industrial.html',message=T("Registrar Tutor Industrial"),form=form)
