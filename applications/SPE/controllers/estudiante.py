from usbutils import random_key

def agregar_preinscripcion():

    #Buscamos los datos del usuario
    ConsultaDatosUsuario    = dbSPE(dbSPE.usuario.usbid==auth.user.username)
    ConsultaDatosEstudiante = dbSPE(dbSPE.usuario_estudiante.usbid_usuario==auth.user.username)
    DatosUsuario    = ConsultaDatosUsuario.select()[0]
    DatosEstudiante = ConsultaDatosEstudiante.select()[0]

    #Datos de las carrera
    DatosCarrera   = dbSPE(dbSPE.carrera.codigo==DatosEstudiante.carrera).select()[0]

    #llenamos el formulario
    datos_personales = SQLFORM.factory(
        Field('nombre' ,label='Nombre y Apellido ',required=True,
                default = DatosUsuario.nombre + ' ' + DatosUsuario.apellido),
        Field('cedula' ,label='Cedula ',required=True,
                default = DatosUsuario.ci),
        Field('carrera',label='Carrera',required=True, requires=IS_IN_DB(dbSPE,dbSPE.carrera,'%(codigo)s %(nombre)s',zero="Seleccione"),
                default = DatosCarrera.codigo),
        Field('sede',label='Sede',required=True, requires=IS_IN_SET(['Sartenejas','Litoral'],zero="Seleccione"),
                default = DatosEstudiante.estudiante_sede),
        Field('direccion',label='Direccion',required=True,
                default = DatosEstudiante.direccion),
        Field('correo',label='Correo Electronico',required=True,
                default  = DatosEstudiante.email_sec),
        Field('telf_hab',label='Telefono Habitacion',required=True,
                default = DatosEstudiante.telf_hab),
        formstyle='bootstrap3_stacked',
        submit_button=T('Actualizar Datos')
    )

    datos_pasantia = SQLFORM.factory(

        Field('codigo_pasantia',label='Codigo de la Pasantia',required=True,
                requires=IS_IN_DB(dbSPE,dbSPE.tipo_pasantia,'%(codigo)s %(nombre)s',
                zero="Seleccione")),
        Field('periodo',label='Periodo',required=True,
                        requires=IS_IN_DB(dbSPE(dbSPE.periodo.periodo_activo == 1),dbSPE.periodo,
                        '%(nombre)s',zero="Seleccione")),
        Field('es_graduando',label="¿Es usted graduando?",required=True, requires=IS_IN_SET(["Si","No"]),
                widget=lambda k,v:SQLFORM.widgets.radio.widget(k,v,style='divs')),
        Field('publicar_datos',label="¿Desea que las empresas puedan ver sus datos?",
                required=True, requires=IS_IN_SET(["Si","No"]),
                widget=lambda k,v:SQLFORM.widgets.radio.widget(k,v,style='divs')),
        Field('estado',label='Estado',
                requires=IS_IN_DB(dbSPE,dbSPE.estado,'%(nombre)s',zero="Seleccione")),
        formstyle='bootstrap3_stacked',

        col3={'es_graduando':'Conteste "Si" si la pasantia es su ultimo requisito para el acto de grado.',
              'publicar_datos':'Al contestar "Si" empresas podran ver su curriculum. Debera llenar su curriculum en el sistema.',
              'estado':'Estado del pais donde usted tenga preferencia para realizar su pasantia.'}
    )

    existe_foto = tiene_foto(DatosUsuario.usbid)['check']

    #Funciones guardar_imagen y validar_foto estan definicads en models/funciones.py
    datos_perfil = SQLFORM.factory(

        Field('image', 'upload',label="Foto de Perfil", required=not(existe_foto),
                uploadfolder='applications/SPE/static/profile_pictures',
                requires = IS_IMAGE(extensions=('jpeg', 'png'))),
        col3={'image':'Utilice una foto tipo carnet reciente.'},
        formstyle='bootstrap3_stacked',
        submit_button=T('Subir Foto')
    )

    #validamos la foto de perfil
    if datos_perfil.process(formname="datos_perfil").accepted:
        ConsultaDatosUsuario.update(foto=datos_perfil.vars.image)

    if datos_personales.process(formname="datos_personales").accepted:
        ConsultaDatosEstudiante.update(direccion=datos_personales.vars.direccion)
        ConsultaDatosEstudiante.update(email_sec=datos_personales.vars.correo)
        ConsultaDatosEstudiante.update(telf_hab=datos_personales.vars.telf_hab)

    if datos_pasantia.process(formname="datos_pasantia").accepted:
        dbSPE.preinscripcion.update_or_insert(
                dbSPE.preinscripcion.usbid == auth.user.username,
                id_periodo    = datos_pasantia.vars.periodo,
                anio          = int(request.now.year),
                codigo        = datos_pasantia.vars.codigo_pasantia,
                usbid         = auth.user.username,
                fecha_ingreso = request.now,
                id_estado     = datos_pasantia.vars.id,
                cod_seguridad = random_key()
                )

    return dict(message="Preinscripcion",form1=datos_personales,form2=datos_pasantia,form3=datos_perfil)

def finalizar_preinscripcion():

    DatosInscripcion = dbSPE(dbSPE.preinscripcion.usbid==auth.user.username).select()[0]
    DatosUsuario     = dbSPE(dbSPE.usuario.usbid==auth.user.username).select()[0]
    DatosEstudiante  = dbSPE(dbSPE.usuario_estudiante.usbid_usuario==auth.user.username).select()[0]
    DatosCarrera     = dbSPE(dbSPE.carrera.codigo==DatosEstudiante.carrera).select()[0]
    DatosPeriodo     = dbSPE(dbSPE.evento.codigo==DatosInscripcion.id_periodo).select()[0]

    return  dict(message=T("Preinscripcion Exitosa"),
                datos_personales = {
                'Nombre'   : DatosUsuario.nombre + ' ' + DatosUsuario.apellido,
                'Cedula'   : str(DatosUsuario.ci),
                'Carrera'  : DatosCarrera.nombre,
                'Sede'     : DatosEstudiante.estudiante_sede,
                'Direccion': DatosEstudiante.direccion,
                'Correo'   : DatosEstudiante.email_sec,
                'Telfono habitacion' : DatosEstudiante.telf_hab
                },
                datos_pasantia = {
                'Periodo'            : DatosPeriodo.nombre,
                'Codigo Pasantia'    : DatosInscripcion.codigo,
                'Fecha Inscripcion'  : DatosInscripcion.fecha_ingreso.strftime('%d-%m-%Y'),
                'Codigo de Seguridad': DatosInscripcion.cod_seguridad
                }
            )

def registrar_estudiante():

    import ast
    #Aqui estan las variables obtenidas por el CAS
    usuario =  ast.literal_eval(request.vars['usuario'])

    #Llenamos el formulario con el default
    dbSPE.usuario_estudiante.usbid_usuario.default  = auth.user.username
    dbSPE.usuario_estudiante.carrera.requires = IS_IN_DB(dbSPE,dbSPE.carrera,'%(nombre)s',zero="Seleccione", error_message='Carrera Inválida')
    dbSPE.usuario_estudiante.carrera.default  = usuario['carrera']


    form_estudiante = SQLFORM(
                    dbSPE.usuario_estudiante,
                    formstyle='bootstrap3_stacked',
                    submit_button="Actualizar Datos"
                    )

    if form_estudiante.process().accepted:
        enviar_Correo_Verificacion(form_estudiante.vars.email_sec)
        redirect(URL(c='default',f='verifyEmail'))

    return dict(message='Por favor actualiza tus datos para continuar',form=form_estudiante)

def plan_trabajo():
    return dict(message="Plan de Trabajo")

def llenar_curriculum():

    print('Voy a llenar curriculum')
    #Buscamos los datos del curriculum si los hay
    ConsultaDatosCurriculum = dbSPE(dbSPE.curriculum.usbid==auth.user.username)
    DatosCurriculum = ConsultaDatosCurriculum.select()

    electivas = []
    cursos    = []
    idiomas   = []
    conocimientos = []
    aficiones = []

    for i in range(len(DatosCurriculum)):
        electivas.append(DatosCurriculum[i]['electiva'])
        cursos.append(DatosCurriculum[i]['cursos'])
        idiomas.append(DatosCurriculum[i]['idiomas'])
        conocimientos.append(DatosCurriculum[i]['conocimientos'])
        aficiones.append(DatosCurriculum[i]['aficiones'])

    #Generamos el SQLFORM utilizando los campos
    datos_electivas = SQLFORM.factory(
        Field('electivas',label='Electivas Cursadas',required=True,
                default='Nombre de la electiva'),
        submit_button='Agregar',
        buttons=['submit'],
    )

    datos_cursos = SQLFORM.factory(
        Field('cursos',label='Cursos Realizados',
                default='Nombre o tema del curso'),
        submit_button='Submit',
        buttons=['submit']
    )

    datos_idiomas = SQLFORM.factory(
        Field('idiomas',label='Idiomas manejados',
                default='Nombre del idioma'),
        submit_button='Submit',
        buttons=['submit']
    )

    datos_aficiones = SQLFORM.factory(
        Field('aficiones',label='Aficiones',
                default='Cosas que te gustan o interesan'),
        submit_button='Submit',
        buttons=['submit']
    )

    if datos_electivas.process().accepted:
        #Insertamos la electiva
        print("Heyyy1")

    if datos_cursos.process().accepted:
        #Insertamos la electiva
        print("Heyyy2")

    if datos_idiomas.process().accepted:
        #Insertamos la electiva
        print("Heyyy3")

    if datos_aficiones.process().accepted:
        #Insertamos la electiva
        print("Heyyy5")

    return dict(message="Curriculum", form1=datos_electivas, form2=datos_cursos, form3=datos_idiomas, form4=datos_aficiones,
                electivas=electivas, cursos=cursos, idiomas=idiomas, conocimientos=conocimientos, aficiones=aficiones)

def retirar_pasantia():
    # Argumentos son: codigo, año, periodo
    if len(request.args)==3:
        form = SQLFORM.factory(
            Field('motivo', label = 'Motivo del retiro')
            )
        if form.process().accepted:
            # Falta refinar este query con año, periodo e id_estudiante
            pasantia = dbSPE((dbSPE.pasantia.codigo==request.args[0]) &
                (dbSPE.pasantia.anio==request.args[1]) &
                (dbSPE.pasantia.periodo==request.args[2]) &
                (dbSPE.pasantia.id_estudiante==auth.user.username)
                )

            pasantia.update(motivo_retiro_estudiante=form.vars.motivo)
            response.flash = 'Actualizado el motivo'
            redirect(URL('default', 'index'))
        elif form.errors:
            response.flash = 'Error'

    else:
        # Este query debe ser remplazado por el correcto
        # Buscar las pasantias segun el id del usuario(estudiante)
        pasantias = dbSPE(dbSPE.pasantia.id_estudiante == auth.user.username)

        opciones = []
        periodos = {}
        for p in pasantias.select():
            periodo = dbSPE.periodo(p.periodo)
            periodos[periodo.nombre] = p.periodo
            opciones.append('['+p.codigo+'] '+periodo.nombre+' '+str(p.anio)+' '+p.titulo)

        form = SQLFORM.factory(
            Field('pasantia', requires = IS_IN_SET(opciones))
            )

        if form.process().accepted:
            # Datos: codigo, periodo(nombre), año
            datos = form.vars.pasantia.split()
            datos[0] = datos[0][1:-1]
            redirect(URL('retirar_pasantia/'+datos[0]+'/'+datos[2]+'/'+str(periodos[datos[1]])))

        elif form.errors:
            response.flash = 'Error'

    return dict(form=form)
