# -*- coding: utf-8 -*-

def justificar_retiro_pasante():
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
        form = SQLFORM(dbSPE.pasantia, pasantia, readonly=True)

        if form.process().accepted:
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
