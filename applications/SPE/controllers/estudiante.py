
def agregar_preinscripcion():
    # return dict(message="Para preinscribirse complete los siguientes datos:")
    response.flash = T("¡Bienvenido!")
    return dict(message="Preinscripcion")

def plan_trabajo():
    return dict(message="Plan de Trabajo")

def llenar_curriculum():
    return dict(message="Curriculum")
