# -*- coding: utf-8 -*-
from usbutils import random_key
import re

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
        Field('cedula' ,label='Cédula ',required=True,
                default = DatosUsuario.ci),
        Field('carrera',label='Carrera',required=True, requires=IS_IN_DB(dbSPE,dbSPE.carrera,'%(codigo)s %(nombre)s',zero="Seleccione"),
                default = DatosCarrera.codigo),
        Field('sede',label='Sede',required=True, requires=IS_IN_SET(['Sartenejas','Litoral'],zero="Seleccione"),
                default = DatosEstudiante.estudiante_sede),
        Field('direccion',label='Dirección',required=True,
                default = DatosEstudiante.direccion),
        Field('correo',label='Correo Electrónico',required=True,
                default  = DatosEstudiante.email_sec),
        Field('telf_hab',label='Teléfono Habitación',required=True,
                default = DatosEstudiante.telf_hab),
        submit_button='Guardar datos',
        buttons=['submit'],
        formstyle='bootstrap3_stacked'
    )

    datos_pasantia = SQLFORM.factory(

        Field('codigo_pasantia',label='Código de la Pasantía',required=True,
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
        submit_button='Guardar datos',
        buttons=['submit'],
        formstyle='bootstrap3_stacked',

        col3={'es_graduando':'Conteste "Si" si la pasantía es su último requisito para el acto de grado.',
              'publicar_datos':'Al contestar "Si" las empresas podrán ver su curriculum. Deberá llenar su curriculum en el sistema.',
              'estado':'Estado del país donde usted tenga preferencia para realizar su pasantía.'}
    )

    existe_foto = tiene_foto(DatosUsuario.usbid)['check']

    #Funciones guardar_imagen y validar_foto estan definicads en models/funciones.py
    datos_perfil = SQLFORM.factory(

        Field('image', 'upload',label="Foto de Perfil", required=not(existe_foto),
                uploadfolder='applications/SPE/static/profile_pictures',
                requires = IS_IMAGE(extensions=('jpeg', 'png'))),
        submit_button='Subir Foto',
        buttons=['submit'],
	formstyle='bootstrap3_stacked',

        col3={'image':'Utilice una foto tipo carnet reciente.'}
    )

    #validamos la foto de perfil
    if datos_perfil.process(formname="datos_perfil").accepted:
        ConsultaDatosUsuario.update(foto=datos_perfil.vars.image)
        redirect(URL('estudiante', 'agregar_preinscripcion'))

    #Validamos los datos personales
    if datos_personales.process(formname="datos_personales").accepted:
        ConsultaDatosEstudiante.update(direccion=datos_personales.vars.direccion)
        ConsultaDatosEstudiante.update(email_sec=datos_personales.vars.correo)
        ConsultaDatosEstudiante.update(telf_hab=datos_personales.vars.telf_hab)
        redirect(URL('estudiante', 'agregar_preinscripcion'))

    #Validamos los datos de la pasantia
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
        redirect(URL('estudiante', 'agregar_preinscripcion'))

    return dict(message="Preinscripcion",form1=datos_personales,form2=datos_pasantia,form3=datos_perfil)

def finalizar_preinscripcion():

    DatosInscripcion = dbSPE(dbSPE.preinscripcion.usbid==auth.user.username).select()[0]
    DatosUsuario     = dbSPE(dbSPE.usuario.usbid==auth.user.username).select()[0]
    DatosEstudiante  = dbSPE(dbSPE.usuario_estudiante.usbid_usuario==auth.user.username).select()[0]
    DatosCarrera     = dbSPE(dbSPE.carrera.codigo==DatosEstudiante.carrera).select()[0]
    DatosPeriodo     = dbSPE(dbSPE.periodo.id==DatosInscripcion.id_periodo).select()[0]

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
    dbSPE.usuario_estudiante.usbid_usuario.default  = request.vars.usbid
    dbSPE.usuario_estudiante.carnet.default  = request.vars.usbid
    dbSPE.usuario_estudiante.usbid_usuario.writable  = False
    dbSPE.usuario_estudiante.carnet.writable  = False
    dbSPE.usuario_estudiante.carrera.requires = IS_IN_DB(dbSPE,dbSPE.carrera,'%(nombre)s',zero="Seleccione", error_message='Carrera Inválida')
    dbSPE.usuario_estudiante.carrera.default  = usuario['carrera']

    form_estudiante = SQLFORM(
                    dbSPE.usuario_estudiante,
                    formstyle='bootstrap3_stacked',
                    submit_button="Actualizar Datos"
                    )

    if form_estudiante.process().accepted:
        generar_Correo_Verificacion(form_estudiante.vars.email_sec)
        redirect(URL(c='default',f='verifyEmail',vars=dict(correo=form_estudiante.vars.email_sec)))

    return dict(message='Por favor actualiza tus datos para continuar',form=form_estudiante)

def plan_trabajo():

    import ast

    #Buscamos los datos del plan de trabajo si los hay
    ConsultaDatosPlan       = dbSPE(dbSPE.plan_de_trabajo.id_estudiante==auth.user.username)
    # ConsultaDatosPasantia   = dbSPE(dbSPE.pasantia.id_estudiante==auth.user.username)
    # DatosPasantia           = ConsultaDatosPasantia.select()


    #Si no los hay, lo creamos
    if ConsultaDatosPlan.isempty():
        dbSPE.plan_de_trabajo.insert(
            id_estudiante=auth.user.username,
            id_tutor_industrial='77@gmail.com',
            id_tutor_academico='77',
            codigo_pasantia='PS1110')
        ConsultaDatosPlan = dbSPE(dbSPE.plan_de_trabajo.id_estudiante==auth.user.username)

    #Obtenemos los datos
    DatosPlan = ConsultaDatosPlan.select()[0]
    print DatosPlan.id
    ConsultaDatosActividad = dbSPE(dbSPE.actividad.id_plan_de_trab==dbSPE.plan_de_trabajo.id)

    #Viene la parte de OBTENER las actividades ya cargadas

    if ConsultaDatosActividad.isempty():
        print "Es vacio"
        actividad = []
        duracion = []
    else:
        print "No es vacio"
        DatosActividad = ConsultaDatosActividad.select()[0]
        if DatosActividad.descripcion == None and DatosActividad.tiempo_estimado == None:
            actividad = []
            duracion = []
        else:
            actividad = ast.literal_eval(DatosActividad.descripcion)
            actividad.sort()
            duracion = ast.literal_eval(DatosActividad.tiempo_estimado)
            duracion.sort()


    ConsultaDatosFase = dbSPE(dbSPE.fase.id_plan_de_trab==DatosPlan.id)

    if ConsultaDatosFase.isempty():
        print "Es vacio fase"
        fases_nombre = []
        fases_obj    = []
    else:
        print "No es vacio fase"
        DatosFase = ConsultaDatosFase.select()[0]
        if DatosFase.nombre_fase == None and DatosActividad.objetivos_especificos == None:
            fases_nombre = []
            fases_obj    = []
        else:
            fases_nombre = ast.literal_eval(DatosFase.nombre_fase)
            fases_nombre.sort()
            fases_obj = ast.literal_eval(DatosActividad.objetivos_especificos)
            fases_obj.sort()

    #Generamos el SQLFORM
    datos_fase = SQLFORM.factory(
        Field('nombre_fase' ,label='Fase',required=True,
                default = 'Fase Reconocimiento'),
        Field('objetivo_fase' ,label='Objetivo específico de la fase',
                required=True, default = 'Objetivo de la fase actual'),
        formstyle='bootstrap3_stacked',
        submit_button=T('AGREGAR FASE')
    )

    datos_actividad = SQLFORM.factory(
        Field('descripcion_actividad' ,label='Descripción de la actividad',
                required=True, default = 'Descripción 1'),
        Field('duracion_actividad' ,label='Duración de la actividad',required=True,
                default = '1 semana'),
        formstyle='bootstrap3_stacked',
        submit_button=T('AGREGAR ACTIVIDAD')
    )

    if datos_fase.process(formname="datos_fase").accepted:
        print "."
    #     #Insertamos la fase.
        if (datos_fase.vars.nombre_fase  != '') and (datos_fase.vars.objetivo_fase  != ''):
            fases_nombre.append(datos_fase.vars.nombre_fase)
            fases_obj.append(datos_fase.vars.objetivo_fase)
            print fases_nombre
            print fases_obj

            dbSPE.fase.insert(
                id_plan_de_trab=DatosPlan.id,
                codigo_pasantia=DatosPlan.codigo_pasantia,
                nombre_fase=datos_fase.vars.nombre_fase,
                objetivos_especificos=datos_fase.vars.objetivo_fase)

    if datos_actividad.process(formname="datos_actividad").accepted:
        print "."
    #     #Insertamos la actividad.
        if (datos_actividad.vars.descripcion_actividad  != '') and (datos_actividad.vars.duracion_actividad  != ''):
            actividad.append(datos_actividad.vars.descripcion_actividad)
            duracion.append(datos_actividad.vars.duracion_actividad)
            print duracion
            print actividad
            # ConsultaDatosActividad.update(descripcion=str(actividad))

    return dict(message="Plan de Trabajo",
                form1=datos_fase,
                form2=datos_actividad,
                actividad=actividad)

    response.flash = T("¡Bienvenido!")

            ##################################################
            #              llenar_curriculum()               #
            ##################################################
def llenar_curriculum():

    import ast

    #Buscamos los datos del curriculum si los hay
    ConsultaDatosCurriculum = dbSPE(dbSPE.curriculum.usbid==auth.user.username)

    #Si no los hay, lo creamos
    if ConsultaDatosCurriculum.isempty():
        dbSPE.curriculum.insert(usbid=auth.user.username)
        ConsultaDatosCurriculum = dbSPE(dbSPE.curriculum.usbid==auth.user.username)

    #Obtenemos los datos
    DatosCurriculum = ConsultaDatosCurriculum.select()[0]

    #Buscamos las electivas a mostrar en pantalla
    if DatosCurriculum.electiva == None:
        electivas = []
    else:
        electivas = ast.literal_eval(DatosCurriculum.electiva)
        electivas.sort()

    #Buscamos los cursos a mostrar en pantalla
    if DatosCurriculum.cursos == None:
        cursos = []
    else:
        cursos = ast.literal_eval(DatosCurriculum.cursos)
        cursos.sort()

    #Buscamos los idiomas a mostrar en pantalla
    if DatosCurriculum.idiomas == None:
        idiomas = []
    else:
        idiomas = ast.literal_eval(DatosCurriculum.idiomas)
        idiomas.sort()

    #Buscamos los conocimientos a mostrar en pantalla
    if DatosCurriculum.conocimientos == None:
        conocimientos = []
    else:
        conocimientos = ast.literal_eval(DatosCurriculum.conocimientos)
        conocimientos.sort()

    #Buscamos las aficiones o intereses a mostrar en pantalla
    if DatosCurriculum.aficiones == None:
        aficiones = []
    else:
        aficiones = ast.literal_eval(DatosCurriculum.aficiones)
        aficiones.sort()

    #Generamos los SQLFORM
    datos_electivas = SQLFORM.factory(
        Field('electivas',label='Electivas Cursadas.'),
        submit_button='Agregar',
        buttons=['submit']
    )

    datos_cursos = SQLFORM.factory(
        Field('cursos',label='Cursos Realizados'),
        submit_button='Agregar',
        buttons=['submit']
    )

    datos_idiomas = SQLFORM.factory(
        Field('idiomas',label='Idiomas manejados'),
        submit_button='Agregar',
        buttons=['submit']
    )

    datos_aficiones = SQLFORM.factory(
        Field('aficiones',label='Aficiones'),
        submit_button='Agregar',
        buttons=['submit']
    )

    datos_conocimientos = SQLFORM.factory(
        Field('conocimientos',label='Conocimientos'),
        submit_button='Agregar',
        buttons=['submit']
    )


    if datos_electivas.process(formname="datos_electivas").accepted:
        #Insertamos la electiva
        if re.search('[^\s]+',datos_electivas.vars.electivas):
            electivas.append(datos_electivas.vars.electivas)
            ConsultaDatosCurriculum.update(electiva=str(electivas))
        redirect(URL('estudiante', 'llenar_curriculum'))

    if datos_cursos.process(formname="datos_cursos").accepted:
        #Insertamos el curso
        if datos_cursos.vars.cursos != '':
            cursos.append(datos_cursos.vars.cursos)
            ConsultaDatosCurriculum.update(cursos=str(cursos))
        redirect(URL('estudiante', 'llenar_curriculum'))

    if datos_idiomas.process(formname="datos_idiomas").accepted:
        #Insertamos el idioma
        if datos_idiomas.vars.idiomas != '':
            idiomas.append(datos_idiomas.vars.idiomas)
            ConsultaDatosCurriculum.update(idiomas=str(idiomas))
        redirect(URL('estudiante', 'llenar_curriculum'))

    if datos_aficiones.process(formname="datos_aficiones").accepted:
        #Insertamos la aficion o interes
        if datos_aficiones.vars.aficiones != '':
            aficiones.append(datos_aficiones.vars.aficiones)
            ConsultaDatosCurriculum.update(aficiones=str(aficiones))
        redirect(URL('estudiante', 'llenar_curriculum'))

    if datos_conocimientos.process(formname="datos_conocimientos").accepted:
        #Insertamos el conocimiento
        if datos_conocimientos.vars.conocimientos != '':
            conocimientos.append(datos_conocimientos.vars.conocimientos)
            ConsultaDatosCurriculum.update(conocimientos=str(conocimientos))
        redirect(URL('estudiante', 'llenar_curriculum'))

    return dict(message="Curriculum",
                form1=datos_electivas,
                form2=datos_cursos,
                form3=datos_idiomas,
                form4=datos_aficiones,
                form5=datos_conocimientos,
                electivas=electivas,
                cursos=cursos,
                idiomas=idiomas,
                conocimientos=conocimientos,
                aficiones=aficiones
                )


            ##################################################
            #              generar_curriculum()              #
            ##################################################
def generar_curriculum():
    import os

    #Buscamos los datos del curriculum si los hay
    ConsultaDatosCurriculum = dbSPE(dbSPE.curriculum.usbid==auth.user.username)
    #Obtenemos los datos
    DatosCurriculum = ConsultaDatosCurriculum.select()[0]

    #Buscamos las electivas a mostrar en pantalla
    if DatosCurriculum.electiva != None:
        #Obtenemos el usuario y la ruta donde guardaremos el curriculum
        nombreUsuario = auth.user.username
        ruta = request.folder
        #Obtenemos la ruta del archivo generado
        archivoTemporal = curriculum_en_pdf(ruta,nombreUsuario)
        #Abrimos el archivo generado
        archivo = open(archivoTemporal,"rb").read()
        #Quitamos el archivo generado
        os.unlink(archivoTemporal)
        #Indicamos la aplicacion con la que se abre el archivo
        response.headers['Content-Type']='application/pdf'
        #Enviamos la ruta del archivo a mostrar
        return archivo


def retirar_pasantia():
    pasantias = dbSPE((dbSPE.pasantia.id_estudiante == auth.user.username) & (dbSPE.pasantia.status=='en curso'))
    pasantia = pasantias.select()[0]
    field =[dbSPE.pasantia.motivo_retiro_estudiante]
    form = SQLFORM.factory(
        *field,submit_button='Subir Carta',
        separator=': ',
        buttons=['submit'],
        type='text',
        col3 = {'motivo':T('Motivo del retiro de la pasantía')}
        )
    if form.process().accepted:
        pasantias.update(motivo_retiro_estudiante=form.vars.motivo_retiro_estudiante)
        response.flash = 'Actualizado el motivo'
        redirect(URL('ver_retiro'))

    return dict(form=form,pasantia=pasantia)

def ver_retiro():
    estudiante = dbSPE(dbSPE.usuario.usbid==auth.user.username).select()[0]
    pasantias = dbSPE((dbSPE.pasantia.id_estudiante == auth.user.username) & (dbSPE.pasantia.status=='en curso'))
    pasantia = pasantias.select()[0]
    return dict(pasantia=pasantia,estudiante=estudiante)

def permiso_evaluacion():
    form = SQLFORM.factory(
        Field('defensa', label='Fecha de la defensa', required=True, requires=IS_DATE(format=T('%d-%m-%Y'), error_message='Formato: dd-mm-yyyy')),
        Field('justificacion', type='text', label='Justificacion', required=True, requires=IS_LENGTH(minsize=1, error_message='no puede estar vacio')),
        Field('fechas', label='Fechas propuestas', type='text')
        )

    if form.process().accepted:

        permiso = dbSPE.permiso.insert(
            fecha = request.now,
            codigo_seguridad = random_key(),
            tipo_permiso = 'evaluacion',
            fecha_propuesta = form.vars.defensa,
            justificacion = form.vars.justificacion,
            fechas_propuestas = form.vars.fechas
            )

        dbSPE.solicita_permiso.insert(
            usbid_estudiante = auth.user.username,
            codigo_permiso = permiso['codigo'],
            )

        response.flash = 'Permiso solicitado'
    elif form.errors:
        response.flash = 'Error'

    return dict(form=form)

def permiso_inscripcion():
    form = SQLFORM.factory(
        Field('justificacion', type='text', label='Justificacion', required=True, requires=IS_LENGTH(minsize=1, error_message='no puede estar vacio')),
        )

    if form.process().accepted:
        permiso = dbSPE.permiso.insert(
            fecha = request.now,
            codigo_seguridad = random_key(),
            tipo_permiso = 'inscripcion',
            justificacion = form.vars.justificacion,
            )

        dbSPE.solicita_permiso.insert(
            usbid_estudiante = auth.user.username,
            codigo_permiso = permiso['codigo'],
            )

        response.flash = 'Permiso solicitado'
    elif form.errors:
        response.flash = 'Error'

    return dict(form=form)
