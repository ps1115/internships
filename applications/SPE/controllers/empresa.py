# -*- coding: utf-8 -*-

# Proceso de registro de empresa por medio de la opcion Empresa -> Registrarse, en el Index
def registrar_empresa():
    # Agregamos los campos en el orden deseado, comenzamos con el login y el password
    fields = [dbSPE.empresa.loginID,dbSPE.empresa.password]
    # Agregamos un campo extra de comfirm password el cual debera tener el mismo valor que el password para ser aceptado
    fields += [Field('comfirm_Password','password', label=T('Comfirm Password'), 
                     requires = [IS_EXPR('value==%s' % repr(request.vars.password),error_message=T('Las contraseñas no coinciden'))])]
    # Agregamos el resto de los campos
    fields += [dbSPE.empresa.pregunta_secreta,dbSPE.empresa.respuesta_pregunta_secreta,dbSPE.empresa.nombre,dbSPE.empresa.direccion,dbSPE.empresa.pag_web,dbSPE.empresa.descripcion,dbSPE.empresa.telefono,dbSPE.empresa.contacto_RRHH]
    # Generamos el SQLFORM utilizando los campos
    form = SQLFORM.factory(
    *fields,submit_button='Submit',
    separator=': ',
    buttons=['submit'],
    col3 = {'loginID':T('Identificación de acceso unica asignada a la empresa'),
            'password':T('Contraseña para acceder al sistema'),
            'comfirm_Password':T('Repita su contraseña'),
            'pregunta_secreta':T('Si necesita obtener de nuevo su contraseña se le hara esta pregunta'),
            'respuesta_pregunta_secreta':T('Respuesta a su pregunta secreta'),
            'nombre':T('Nombre comercial de la empresa'),
            'direccion':T('Direccion de las instalaciones de la empresa'),
            'pag_web':T('Pagina Web de la empresa'),
            'descripcion':T('Descripcion breve de la empresa, su vision y sus funciones'),
            'telefono':T('Numerico telefonico de contacto de la empresa'),
            'contacto_RRHH':T('Correo de contacto del departamento de recursos humanos de la empresa')}
    )

    # Caso 1: El form se lleno de manera correcta asi que registramos la empresa y procedemos a la pagina de exito
    if form.process().accepted:
        # Registramos la empresa
        dbSPE.empresa.insert(loginID = request.vars.loginID,
                             password = request.vars.password,
                             pregunta_secreta = request.vars.pregunta_secreta,
                             respuesta_pregunta_secreta = request.vars.respuesta_pregunta_secreta,
                             nombre = request.vars.nombre,
                             direccion = request.vars.direccion,
                             pag_web = request.vars.pag_web,
                             descripcion = request.vars.descripcion,
                             telefono = request.vars.telefono,
                             contacto_RRHH = request.vars.contacto_RRHH)
        # Mensaje de exito
        response.flash = T("Registro Exitoso")
        # Nos dirigimos a la pagina de exito
        return response.render('default/registro_empresa_exitoso.html',message=T("Registrar Empresa"),
                               result=T("El registro de su empresa ha sido exitoso!"),
                               loginID=request.vars.loginID,
                               nombre=request.vars.nombre,
                               direccion=request.vars.direccion,
                               pag_web=request.vars.pag_web,
                               descripcion=request.vars.descripcion,
                               telefono=request.vars.telefono,
                               contacto_RRHH=request.vars.contacto_RRHH)
    # Caso 2: El form no se lleno de manera correcta asi que recargamos la pagina
    else:
        return response.render('empresa/registrar_empresa.html',message=T("Registrar Empresa"),form=form)
