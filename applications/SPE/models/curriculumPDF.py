# -*- coding: utf-8 -*-
import os
import ast
from uuid                         import uuid4
from cgi                          import escape
from reportlab.pdfgen             import canvas
from reportlab.platypus           import BaseDocTemplate, PageTemplate, Frame, Paragraph, PageBreak, Table, TableStyle
from reportlab.lib                import colors
from reportlab.lib.pagesizes      import letter 
from reportlab.lib.styles         import ParagraphStyle
from reportlab.lib.enums          import TA_CENTER,TA_RIGHT, TA_LEFT, TA_JUSTIFY
from reportlab.lib.units          import cm
from reportlab.lib.colors         import lightgrey
from reportlab.pdfbase            import pdfmetrics
from reportlab.pdfbase.ttfonts    import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily

#Registramos Times New Roman y Arial Bold como fuente permitida
pdfmetrics.registerFont(TTFont('Arial Bold',os.path.abspath('./applications/SPE/fonts/Arial Bold.ttf')))
registerFontFamily('Arial Bold',bold='Arial Bold')

pdfmetrics.registerFont(TTFont('Times New Roman',os.path.abspath('./applications/SPE/fonts/Times New Roman.ttf')))
registerFontFamily('Times New Roman',bold='Times New Roman')

def curriculum_en_pdf(ruta,nombreUsuario):
    #Creamos el camino con la ruta y el hash con el que se nombrara el pdf
    nombreArchivo = os.path.join(ruta,'private',str(uuid4()))

    #Buscamos los datos del curriculum si los hay
    ConsultaDatosCurriculum = dbSPE(dbSPE.curriculum.usbid==auth.user.username)
    #Obtenemos los datos
    DatosCurriculum = ConsultaDatosCurriculum.select()[0]

    #Buscamos las electivas a mostrar en pantalla
    if DatosCurriculum.electiva == None:
        arreglo_electivas = []
    else:
        arreglo_electivas = ast.literal_eval(DatosCurriculum.electiva)
        arreglo_electivas.sort()
            
    #Buscamos los cursos a mostrar en pantalla
    if DatosCurriculum.cursos == None:
        arreglo_cursos = []
    else:
        arreglo_cursos = ast.literal_eval(DatosCurriculum.cursos)
        arreglo_cursos.sort()

    #Buscamos los idiomas a mostrar en pantalla
    if DatosCurriculum.idiomas == None:
        arreglo_idiomas = []
    else:
        arreglo_idiomas = ast.literal_eval(DatosCurriculum.idiomas)
        arreglo_idiomas.sort()

    #Buscamos los conocimientos a mostrar en pantalla
    if DatosCurriculum.conocimientos == None:
        arreglo_conocimientos = []
    else:
        arreglo_conocimientos = ast.literal_eval(DatosCurriculum.conocimientos)
        arreglo_conocimientos.sort()

    #Buscamos las aficiones o intereses a mostrar en pantalla
    if DatosCurriculum.aficiones == None:
        arreglo_aficiones = []
    else:
        arreglo_aficiones = ast.literal_eval(DatosCurriculum.aficiones)
        arreglo_aficiones.sort()

    #Buscamos los datos del usuario
    ConsultaDatosUsuario    = dbSPE(dbSPE.usuario.usbid==auth.user.username)
    ConsultaDatosEstudiante = dbSPE(dbSPE.usuario_estudiante.usbid_usuario==auth.user.username)
    DatosUsuario    = ConsultaDatosUsuario.select()[0]
    DatosEstudiante = ConsultaDatosEstudiante.select()[0]

    nombreCompleto = DatosUsuario['nombre'] + ' ' + DatosUsuario['apellido']
    carnet         = DatosUsuario['usbid']
    direccion      = DatosEstudiante['direccion']
    tlf_celular    = DatosEstudiante['telf_cel']
    tlf_fijo       = DatosEstudiante['telf_hab']
    email          = DatosEstudiante['email_sec']
    codigoCarrera  = DatosEstudiante['carrera']

    #Buscamos los datos de la carrera
    ConsultaDatosCarrera = dbSPE(dbSPE.carrera.codigo==codigoCarrera)
    DatosCarrera = ConsultaDatosCarrera.select()   
    
    if DatosCarrera:
        DatosCarrera = DatosCarrera[0]
        carrera = DatosCarrera['nombre']
    else:
        #En caso de no encontrar la carrera
        carrera = codigoCarrera

    #Textos a mostrar
    text_electivas = 'Electivas profesionales cursadas:'
    text_cursos    = 'Cursos realizados:'
    text_idiomas   = 'Idiomas manejados:'
    text_aficiones = 'Aficiones o intereses:'
    text_conocimientos = 'Conocimientos en:'

    #Aqui comienza codigo para la generacion del pdf

    #Definimos los tamanos de los arreglos para establecer el tamaño de las celdas
    cant_electivas = len(arreglo_electivas)
    cant_cursos    = len(arreglo_cursos)
    cant_idiomas   = len(arreglo_idiomas)
    cant_aficiones = len(arreglo_aficiones)
    cant_conocimientos = len(arreglo_conocimientos)

    #Definimos el tamano permitido antes del salto de linea segun corresponda
    MAX_TAM_NOMBRE_CARNET = 41
    MAX_TAM_DIRECCION = 35
    MAX_TAM_CONTENIDO = 68


    def convertirArregloAListaConVineta(arreglo): 
        contenido = []
        numExceso = 0
        for i in range(len(arreglo)):
            contenido.append(Paragraph(arreglo[i],estilos['contenido']))

            #Verificamos que ningún contenido se pase del permitido y si se pasa agregamos una línea más para mostrar.
            #Esto para evitar que se sobremonte la información mostrada
            if (len(arreglo[i]) >= MAX_TAM_CONTENIDO):
                num = len(arreglo[i])/MAX_TAM_CONTENIDO
                numExceso += num
                num = len(arreglo[i]) % MAX_TAM_CONTENIDO
                if num != 0:
                    numExceso += 1
        return (contenido, numExceso)
        

    def enPaginaUnica(canvas,documento):
        canvas.saveState()
        canvas.restoreState()

    #Definimos la página en blanco y tamaño carta
    documento    = BaseDocTemplate(nombreArchivo,pagesize=letter,title='Minicurriculum',author=carnet)
    elementos    = []
    estilos      = {}
    estilo_tabla = []

    #Definimos el margen.
    pagina = Frame(documento.leftMargin,        #Margen de 3cm
                   documento.bottomMargin,
                   documento.width,             #Margen de 3cm
                   documento.height+0.8*cm,     #Margen de 2cm
                   id='paginaUnica')

    #Definimos el template para la página
    documento.addPageTemplates([PageTemplate(id='paginaUnica',
                                             frames=pagina,
                                             onPage=enPaginaUnica)])

    #Definimos lo estilos para la información mostrada
    estilos['defecto'] = ParagraphStyle('defecto',
        fontName='Times New Roman',
        fontSize=10,
        leading=15,
        leftIdent=0,
        rightIdent=0,
        firstLineIdent=0,
        alignment=TA_LEFT,
        spaceBefore=0,
        spaceAfter=0,
        bulletFontName='Times-Roman',
        bulletFontSize=5,
        bulletIdent=0,
        textColor='black',
        backColor=None,
        wordWrap=None,
        borderWidth=0,
        borderPadding=0,
        borderColor=None,
        borderRadius=None,
        allowWidows=1,
        alllowOrphans=0,
        textTarnsform=None,  #'uppercase' \ 'lowercase' \ None
        endDots=None,
        splitLongWords=1,
        )

    estilos['datos_personales'] = ParagraphStyle('datos_personales',
        parent=estilos['defecto'],
        fontSize=8,
        leading=10
        )

    estilos['nombre'] = ParagraphStyle('nombre',
        parent=estilos['defecto'],
        fontSize=18,
        leading=20
        )

    estilos['items'] = ParagraphStyle('items',
        parent=estilos['defecto'],
        fontName='Arial Bold',
        backColor='lightgrey',
        borderPadding=3,
        )

    estilos['contenido'] = ParagraphStyle('contenido',
        parent=estilos['defecto'],
        bulletText=u'●',
        )

    estilos['salto_linea'] = ParagraphStyle('salto_linea',
        parent=estilos['defecto'],
        textColor='white'
        )

    #Definimos el estilo de la tabla
    estilos_Tabla1 = [('ALIGN',(0,0),(-1,-1),'LEFT'), #La notación de las tuplas es (columna,fila)
                      ('VALIGN', (0,0),(-1,-1),'TOP')]
                      #('INNERGRID',(0,0),(-1,-1),0.25,colors.black),
                      #('BOX',(0,0),(-1,-1),0.25,colors.black)]

    estilos_Tabla2  = [('ALIGN',(0,0),(-1,-1),'LEFT'), #La notación de las tuplas es (columna,fila)
                      ('VALIGN', (0,0),(-1,-1),'TOP'),
                      ('BACKGROUND',(0,0),(0,0),colors.lightgrey)]


    #Elementos a mostrar
    #Verificamos los casos en que los teléfonos sean vacios
    if tlf_fijo != '' or tlf_fijo != None:
        tlf_fijo = 'Teléfono: '+ tlf_fijo + '<br />'
    
    if tlf_fijo == None:
        tlf_fijo = ''

    if tlf_celular != '' or tlf_celular != None: 
        tlf_celular = 'Celular: '+ tlf_celular + '<br />'

    if tlf_celular == None:
        tlf_celular = ''

    cabecera1 = Paragraph('Dirección: <br />'+direccion,estilos['datos_personales'])
    cabecera2 = Paragraph(tlf_fijo + tlf_celular + 'Correo electrónico: '+ email,estilos['datos_personales'])
    cabecera3 = Paragraph(nombreCompleto + ', Ct ' + carnet, estilos['nombre'])

    #Verificamos cuantas lineas ocupa nombre y carnet
    cantLineasNombreCarnet = 0
    cadena = nombreCompleto + ', Ct ' + carnet
    if (len(cadena) >= MAX_TAM_NOMBRE_CARNET):
        num = len(cadena) / MAX_TAM_NOMBRE_CARNET
        cantLineasNombreCarnet += num
        num = len(cadena) % MAX_TAM_NOMBRE_CARNET
        if num != 0:
            cantLineasNombreCarnet += 1
    elif (len(cadena) > 0 and len(cadena) < MAX_TAM_NOMBRE_CARNET):
        cantLineasNombreCarnet = 1
      
    general   = Paragraph('Estudiante de ' + carrera + '.',estilos['defecto'])

    #Verificamos la cantidad de lineas que ocupa la carrera

    numLineasCarrera = 0
    cadena = 'Estudiante de ' + carrera + '.'
    if (len(cadena) >= MAX_TAM_CONTENIDO):
        num = len(cadena)/MAX_TAM_CONTENIDO
        numLineasCarrera += num
        num = len(cadena) % MAX_TAM_CONTENIDO
        if num != 0:
            numLineasCarrera += 1
    elif (len(cadena) > 0 and len(cadena) < MAX_TAM_CONTENIDO):
        numLineasCarrera = 1

    salto_linea = Paragraph('. <br/>',estilos['salto_linea'])


    #Mostrar electivas
    electivas_cursadas, numExceso = convertirArregloAListaConVineta(arreglo_electivas)
    item_electivas  = Paragraph(text_electivas,estilos['items'])
    cant_electivas += numExceso

    #Mostrar cursos
    cursos_realizados, numExceso = convertirArregloAListaConVineta(arreglo_cursos)
    item_cursos  = Paragraph(text_cursos,estilos['items'])
    cant_cursos += numExceso

    #Mostrar idiomas
    idiomas_manejados, numExceso = convertirArregloAListaConVineta(arreglo_idiomas)
    item_idiomas  = Paragraph(text_idiomas,estilos['items'])
    cant_idiomas += numExceso

    #Mostrar conocimientos
    conocimientos, numExceso = convertirArregloAListaConVineta(arreglo_conocimientos)
    item_conocimientos  = Paragraph(text_conocimientos,estilos['items'])
    cant_conocimientos += numExceso

    #Mostrar idiomas
    aficiones, numExceso = convertirArregloAListaConVineta(arreglo_aficiones)
    item_aficiones  = Paragraph(text_aficiones,estilos['items'])
    cant_aficiones += numExceso

    if arreglo_cursos == []:
        cursos_realizados = ''
        item_cursos = ''

    if arreglo_idiomas == []:
        idiomas_manejados = ''
        item_idiomas = ''

    if arreglo_conocimientos == []:
        conocimientos = ''
        item_conocimientos = ''

    if arreglo_aficiones == []:
        aficiones = ''
        item_aficiones = ''

    #Definimos la estructura a través de tablas
    datos_Tabla1 = [[' ',cabecera1,cabecera2]]
    datos_Tabla2 = [[cabecera3]]
    datos_Tabla3 = [[' ',general],
                    [item_electivas,electivas_cursadas],
                    [item_cursos,cursos_realizados],
                    [item_idiomas,idiomas_manejados],
                    [item_conocimientos,conocimientos],
                    [item_aficiones,aficiones]]

    #Verificamos cual celda contiene mas información
    #Verificamos cuantas lineas ocupa la dirección
    cantLineasDireccion = 0
    cantLineasDatos     = 0
    cantLineas          = 0

    #Verificamos cuantas lineas ocupa la cabecera de direccion
    if (len(direccion) >= MAX_TAM_DIRECCION):
        num = len(direccion) / MAX_TAM_DIRECCION
        cantLineasDireccion += num
        num = len(direccion) % MAX_TAM_DIRECCION
        if num != 0:
            cantLineasDireccion += 1
    elif (len(direccion) > 0 and len(direccion) < MAX_TAM_DIRECCION):
        cantLineasDireccion = 1

    #Verificamos cuantas lineas ocupa la cabecera de datos de contacto
    if tlf_celular == '':
        cantLineasDatos = 2
    else:
        cantLineasDatos = 3

    if (cantLineasDatos >= cantLineasDireccion): 
        cantLineas = cantLineasDatos
    else:
        cantLineas = cantLineasDireccion

    #Definimos la tabla de dirección, datos de contacto y el tamaño de cada celda
    tam_colums = [0.3*cm,5*cm,6.5*cm]
    tam_filas  = [(cantLineas + 0.5)*0.5*cm] 
    t1 = Table(datos_Tabla1,tam_colums,tam_filas,style=estilos_Tabla2,hAlign='RIGHT')

    #Definimos la tabla del nombre y carnet y el tamaño de cada celda
    tam_colums = [11.5*cm]
    tam_filas  = [(cantLineasNombreCarnet+0.5)*0.7*cm] 
    t2 = Table(datos_Tabla2,tam_colums,tam_filas,style=estilos_Tabla1,hAlign='RIGHT')

    #Definimos la tabla de el contenido a mostrar y el tamaño de cada celda
    if (cant_electivas == 1):
        cant_electivas += 1
    elif (cant_electivas >= 5 and cant_electivas < 10):
        cant_electivas -= 0.5
    elif (cant_electivas >= 10):
        cant_electivas -= 1.6

    if (cant_cursos == 1):
        cant_cursos += 1
    elif (cant_cursos >= 5 and cant_electivas < 10):
        cant_cursos -= 0.5
    elif (cant_cursos >= 10):
        cant_cursos -= 1.6

    if (cant_idiomas == 1):
        cant_idiomas += 1
    elif (cant_idiomas >= 5 and cant_electivas < 10):
        cant_idiomas -= 0.5
    elif (cant_idiomas >= 10):
        cant_idiomas -= 1.6

    if (cant_aficiones == 1):
        cant_aficiones += 1
    elif (cant_aficiones >= 5 and cant_electivas < 10):
        cant_aficiones -= 0.5
    elif (cant_aficiones >= 10):
        cant_aficiones -= 1.6

    if (cant_conocimientos == 1):
       cant_conocimientos += 1
    elif (cant_conocimientos >= 5 and cant_electivas < 10):
        cant_conocimientos -= 0.5
    elif (cant_conocimientos >= 10):
        cant_conocimientos -= 1.6


    tam_colums = [4.5*cm,11.5*cm]
    tam_filas  = [(numLineasCarrera + 0.5)*1*cm,
                  (cant_electivas + 1)*0.5*cm,
                  (cant_cursos + 1)*0.5*cm,
                  (cant_idiomas + 1)*0.5*cm,
                  (cant_conocimientos + 1)*0.5*cm,
                  (cant_aficiones + 1)*0.5*cm]
    t3 = Table(datos_Tabla3,tam_colums,tam_filas,style=estilos_Tabla1,hAlign='RIGHT')


    elementos.append(t1)
    elementos.append(salto_linea)
    elementos.append(t2)
    elementos.append(salto_linea)
    elementos.append(salto_linea)
    elementos.append(t3)
    elementos.append(PageBreak())

    #Finaliza el dibujado sobre el documento
    documento.build(elementos)
 
    return nombreArchivo
