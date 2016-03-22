# -*- coding: utf-8 -*-
# try something like
def index(): return dict(message="hello from catalogos_grid.py")

def retirar_pasantia():
    return response.render('default/retirar_pasantia.html')


def crear_estudiante():
    form = SQLFORM(dbSPE.usuario_estudiante)
    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'

    return form



def crear_profesor():
    form = SQLFORM(dbSPE.usuario_profesor)
    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'

    return form


def crear_empresa():
    form = SQLFORM(dbSPE.empresa)
    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'

    return form


def crear_departamento():
    form = SQLFORM(dbSPE.departamento)
    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'

    return form


def crear_carrera():
    form = SQLFORM(dbSPE.carrera)
    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'

    return form


def estudiantes():
    grid = SQLFORM.grid(dbSPE.usuario_estudiante,user_signature=False)
    return grid

def carreras():
    grid = SQLFORM.grid(dbSPE.carrera,user_signature=False)
    return grid

def empresas():
    grid = SQLFORM.grid(dbSPE.empresa,user_signature=False)
    return grid

def profesores():
    grid = SQLFORM.grid(dbSPE.usuario_profesor,user_signature=False)
    return grid

def departamentos():
    grid = SQLFORM.grid(dbSPE.departamento,user_signature=False)
    return grid

def gestion_cct2():
    return dict()

def especificar_configuraciones():
    return dict()

def roles():
    grid = SQLFORM.grid(dbSPE.rol_sistema,user_signature=False, csv=False)
    return grid

def montos():
    grid = SQLFORM.grid(dbSPE.calculo_pago, deletable=False, csv=False, user_signature=False)
    return grid

"""
def eventos():
    grid = SQLFORM.grid(dbSPE.evento,user_signature=False,
                        deletable=False,
                       csv=False)
    return grid

def sub_evento():
    grid = SQLFORM.grid(dbSPE.sub_evento
        ,user_signature=False
        ,deletable=False
        ,csv=False
        )
    return grid
"""

def periodos():
    grid = SQLFORM.grid(dbSPE.periodo,user_signature=False,
                        deletable=False,
                       csv=False)
    return grid

def semana_muerta():
    grid = SQLFORM.grid(dbSPE.semana_muerta,user_signature=False,
                        deletable=False,
                       csv=False)
    return grid
