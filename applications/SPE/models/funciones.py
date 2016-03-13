# Funciones disponibles en todo el codigo.

def tiene_foto(usbid):
    import os
    path = '/SPE/static/profile_pictures' +str(usbid)+".jpg"
    return os.path.exists(path)

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
