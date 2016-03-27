# Funciones disponibles en todo el codigo.

def tiene_foto(usbid):
    # import os
    #
    # query =  dbSPE(dbSPE.usuario.usbid==usbid)
    # foto  = query.select()[0].foto
    # path = '/SPE/static/profile_pictures/' + str(foto)
    # print "foto " + foto
    # print path
    # print "path" + str(os.path.exists(path))
    # return os.path.exists(path)
    import requests

    query =  dbSPE(dbSPE.usuario.usbid==usbid)
    foto  = query.select()[0].foto
    path = 'http://127.0.0.1:8000/SPE/static/profile_pictures/' + str(foto)
    r = requests.head(path)
    print(r.status_code == requests.codes.ok)
    return dict(check=(r.status_code == requests.codes.ok),path=foto)

def validar_foto(form):
    if form.vars.image is not None:
        print "hello world"
        form.vars.image.imagename = str(auth.user.username) + ".jpg"

def guardar_imagen(image, imagename=None,path=None):
    import os
    import shutil
    path = "applications/SPE/static/profile_pictures"
    if not os.path.exists(path):
         os.makedirs(path)
    print imagename
    pathimagename = os.path.join(path, imagename)
    dest_file = open(pathimagename, 'wb')
    try:
            shutil.copyfileobj(image, dest_file)
    finally:
            dest_file.close()
    return imagename
