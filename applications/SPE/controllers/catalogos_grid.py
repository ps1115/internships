# -*- coding: utf-8 -*-
# try something like
def index(): return dict(message="hello from catalogos_grid.py")

def retirar_pasantia():
    return response.render('default/retirar_pasantia.html')


def crear_estudiante():
    form = SQLFORM(db.usuario_estudiante)
    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    
    return form



def crear_profesor():
    form = SQLFORM(db.usuario_profesor)
    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    
    return form


def crear_empresa():
    form = SQLFORM(db.empresa)
    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    
    return form


def crear_departamento():
    form = SQLFORM(db.departamento)
    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    
    return form


def crear_carrera():
    form = SQLFORM(db.carrera)
    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    
    return form


def estudiantes():
    grid = SQLFORM.grid(db.usuario_estudiante,user_signature=False)
    return grid

def carreras():
    grid = SQLFORM.grid(db.carrera,user_signature=False)
    return grid

def empresas():
    grid = SQLFORM.grid(db.empresa,user_signature=False)
    return grid

def profesores():
    grid = SQLFORM.grid(db.usuario_profesor,user_signature=False)
    return grid

def departamentos():
    grid = SQLFORM.grid(db.departamento,user_signature=False)
    return grid

def gestion_cct2():
    return dict()

def especificar_configuraciones():
    return dict()

def roles():
    grid = SQLFORM.grid(db.rol_sistema,user_signature=False)
    return grid

def montos():
    grid = SQLFORM.grid(db.calculo_pago, deletable=False, editable=False, user_signature=False)
    return grid

def eventos():
    grid = SQLFORM.grid(db.evento,user_signature=False,
                        deletable=False,
                       csv=False)
    return grid

def sub_evento():
    grid = SQLFORM.grid(db.sub_evento,user_signature=False,
                        deletable=False,
                       csv=False)
    return grid

def semana_muerta():
    grid = SQLFORM.grid(db.semana_muerta,user_signature=False,
                        deletable=False,
                       csv=False)
    return grid
