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
        formstyle='bootstrap3_stacked'
    )

    datos_pasantia = SQLFORM.factory(

        Field('codigo_pasantia',label='Codigo de la Pasantia',required=True,
                requires=IS_IN_DB(dbSPE,dbSPE.tipo_pasantia,'%(codigo)s %(nombre)s',
                zero="Seleccione")),
        # Field('periodo',label='Periodo',required=True,
        #                 requires=IS_IN_DB(dbSPE,dbSPE.sub_evento.nombre == Inscripcion,'%(nombre_supra_evento)s',
        #                 zero="Seleccione")),
        Field('periodo',label='Periodo',required=True,
                requires=IS_IN_SET(["Enero - Marzo 2016","Abril-Septiembre 2016"],
                zero="Seleccione")),
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
    print(existe_foto)

    #Funciones guardar_imagen y validar_foto estan definicads en models/funciones.py
    datos_perfil = SQLFORM.factory(

        Field('image', 'upload',label="Foto de Perfil", required=not(existe_foto),
                uploadfolder='applications/SPE/static/profile_pictures',
                requires = IS_IMAGE(extensions=('jpeg', 'png'))),
        col3={'image':'Utilice una foto tipo carnet reciente.'},
        formstyle='bootstrap3_stacked'
    )

    #validamos la foto de perfil
    if datos_perfil.process(formname="datos_perfil").accepted:
        print "Foto!"
        ConsultaDatosUsuario.update(foto=datos_perfil.vars.image)

    if datos_personales.process(formname="datos_personales").accepted:
        print "Datos!"
        ConsultaDatosEstudiante.update(direccion=datos_personales.vars.direccion)
        ConsultaDatosEstudiante.update(email_sec=datos_personales.vars.correo)
        ConsultaDatosEstudiante.update(telf_hab=datos_personales.vars.telf_hab)

    if datos_pasantia.process(formname="datos_pasantia").accepted:
        print "Aceptado!"
        dbSPE.preinscripcion.insert(
                id_periodo    = '00',
                anio          = int(request.now.year),
                codigo        = datos_pasantia.vars.codigo_pasantia,
                usbid         = auth.user.username,
                fecha_ingreso = request.now,
                id_estado     = datos_pasantia.vars.id,
                cod_seguridad = random_key()
                )

    response.flash = T("¡Bienvenido!")
    return dict(message="Preinscripcion",form1=datos_personales,form2=datos_pasantia,form3=datos_perfil)

def finalizar_preinscripcion():

    DatosInscripcion = dbSPE(dbSPE.preinscripcion.usbid==auth.user.username).select()[0]
    DatosUsuario     = dbSPE(dbSPE.usuario.usbid==auth.user.username).select()[0]
    DatosEstudiante  = dbSPE(dbSPE.usuario_estudiante.usbid_usuario==auth.user.username).select()[0]
    DatosCarrera     = dbSPE(dbSPE.carrera.codigo==DatosEstudiante.carrera).select()[0]

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
                'Periodo'            : 'Nombre Periodo',
                'Codigo Pasantia'    : DatosInscripcion.codigo,
                'Fecha Inscripcion'  : DatosInscripcion.fecha_ingreso.strftime('%d-%m-%Y'),
                'Codigo de Seguridad': DatosInscripcion.cod_seguridad
                }
            )

def plan_trabajo():
    return dict(message="Plan de Trabajo")

def llenar_curriculum():
    return dict(message="Curriculum")
