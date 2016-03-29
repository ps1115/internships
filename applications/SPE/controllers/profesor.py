# -*- coding: utf-8 -*-

# Falta especificar que el usario sea profesor.
def justificar_retiro_profesor():
    # Argumentos son: codigo, año, periodo(nombre)
    if len(request.args)==3:
        r = dbSPE(dbSPE.pasantia.codigo==request.args[0]).select(dbSPE.pasantia.motivo_retiro_tutor_academico)
        print r
        if r != 'NULL':
            redirect(URL(c ='default', f='index'))

        field =[dbSPE.pasantia.motivo_retiro_tutor_academico]
        form = SQLFORM.factory(
            *field,submit_button='Subir Carta',
            separator=': ',
            buttons=['submit'],
            col3 = {'motivo':T('Motivo justificativo')}
            )
        if form.process().accepted:
            pasantia = dbSPE((dbSPE.pasantia.codigo==request.args[0]) &
                (dbSPE.pasantia.anio==request.args[1]) &
                (dbSPE.pasantia.periodo==request.args[2]) &
                (dbSPE.pasantia.id_tutor_academico==auth_user.username)
                )

            pasantia.update(motivo_retiro_tutor_academico = request.vars.motivo_retiro_tutor_academico)
            response.flash = 'Actualizado el motivo'
            redirect(URL('justificar_retiro_profesor'))

        elif form.errors:
            response.flash = 'Error'

    else:
        pasantias = dbSPE((dbSPE.pasantia.id_estudiante==auth_user.username) &
            (dbSPE.pasantia.motivo_retiro_estudiante!=None)
        )

        opciones = []
        periodos = {}
        for p in pasantias.select():
            periodo = dbSPE.periodo(p.periodo)
            periodos[periodo.nombre] = p.periodo
            opciones.append('['+p.codigo+'] '+periodo.nombre+' '+str(p.anio)+' '+p.titulo)

        form = SQLFORM.factory(
            Field('pasantia', requires = IS_IN_SET(opciones)),submit_button='Buscar')

        if form.process().accepted:
            # Datos: codigo, periodo(nombre), año
            datos = form.vars.pasantia.split()
            datos[0] = datos[0][1:-1]
            redirect(URL('justificar_retiro_profesor/'+datos[0]+'/'+datos[2]+'/'+str(periodos[datos[1]])))

        elif form.errors:
            response.flash = 'Error'

    return dict(form=form)