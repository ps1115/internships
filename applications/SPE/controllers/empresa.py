# -*- coding: utf-8 -*-

def justificar_retiro_empresa():
    # Argumentos son: codigo, año, periodo(nombre)
    if len(request.args)==3:

        field =[dbSPE.pasantia.motivo_retiro_tutor_industrial]
        form = SQLFORM.factory(
            *field,submit_button='Subir Carta',
            separator=': ',
            buttons=['submit'],
            col3 = {'motivo':T('Motivo justificativo')}
            )
        if form.process().accepted:
            # Falta refinar este query con año, periodo e id_estudiante
            busqueda = dbSPE(dbSPE.pasantia.codigo==request.args[0])
            busqueda.update(motivo_retiro_tutor_industrial = request.vars.motivo_retiro_tutor_industrial)
            response.flash = 'Actualizado el motivo'
            redirect(URL('justificar_retiro_empresa'))

        elif form.errors:
            response.flash = 'Error'

    else:
        # Este query debe ser remplazado por el correcto
        # Buscar las pasantias segun el id del usuario(estudiante)
        pasantias = dbSPE(dbSPE.pasantia.periodo == 77)
        pasantia = pasantias.select()[0]

        opciones = []
        for p in pasantias.select():
            periodo = dbSPE.periodo(p.periodo)
            opciones.append('['+p.codigo+'] '+periodo.nombre+' '+str(p.anio)+' '+p.titulo)

        form = SQLFORM.factory(
            Field('pasantia', requires = IS_IN_SET(opciones)))

        if form.process().accepted:
            # Datos: codigo, periodo(nombre), año
            datos = form.vars.pasantia.split()
            datos[0] = datos[0][1:-1]
            redirect(URL('justificar_retiro_empresa/'+datos[0]+'/'+datos[2]+'/'+datos[1]))

        elif form.errors:
            response.flash = 'Error'

    return dict(form=form)