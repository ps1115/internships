# -*- coding: utf-8 -*-

# Proceso de registro de empresa por medio de la opcion Empresa -> Registrarse, en el Index
def justificar_retiro_pasante():
    # Agregamos los campos en el orden deseado
    fields = [dbSYQ.pasantia1.codigo,dbSYQ.pasantia1.periodo,dbSYQ.pasantia1.motivo_retiro_tutor_academico]
    # Generamos el SQLFORM utilizando los campos
    form = SQLFORM.factory(
    *fields,submit_button='Submit',
    separator=': ',
    buttons=['submit'],
    col3 = {'codigo':T('Codigo de La Pasantia'),
            'periodo':T('Trimestre'),
            'motivo_retiro_tutor_academico':T('Redacte el Motivo')}
    )

    # Caso 1: El form se lleno de manera correcta asi que registramos la empresa y procedemos a la pagina de exito
    if form.process().accepted:
        # Registramos la empresa
        dbSYQ.pasantia1.insert(codigo = request.vars.codigo,
                             periodo = request.vars.periodo,
                             motivo_retiro_tutor_academico = request.vars.motivo_retiro_tutor_academico)
        # Mensaje de exito
        response.flash = T("Registro Exitoso")
        # Nos dirigimos a la pagina de exito
        return response.render('default/index.html',message=T("Subir Carta"),
                               result=T("El registro de su empresa ha sido exitoso!"))
    # Caso 2: El form no se lleno de manera correcta asi que recargamos la pagina
    else:
        return response.render('profesor/justificar_retiro_pasante.html',message=T("Carta de Motivo"),form=form)
