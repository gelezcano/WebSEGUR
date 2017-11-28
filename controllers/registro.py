# -*- coding: utf-8 -*-
# try something like
def index(): return dict(message="hello from registro.py")


def registro_visitante():
    formulario=SQLFORM(db.visitantes)
    if formulario.accepts(request.vars, session):
        response.flash = 'Formulario correctamente cargado'
    elif formulario.errors:
		response.flash = 'Su formulario contiene errores, porfavor modifiquelo'
    else:
		response.flash = 'Por favor rellene el formulario'
    return dict(formulario=formulario)

def registro_vehiculo():
    formulario=SQLFORM(db.vehiculos)
    if formulario.accepts(request.vars, session):
        response.flash = 'Formulario correctamente cargado'
    elif formulario.errors:
		response.flash = 'Su formulario contiene errores, porfavor modifiquelo'
    else:
		response.flash = 'Por favor rellene el formulario'
    return dict(formulario=formulario)

def registro_foto():
    formulario=SQLFORM(db.fotos)
    if formulario.accepts(request.vars, session):
        response.flash = 'Formulario correctamente cargado'
    elif formulario.errors:
		response.flash = 'Su formulario contiene errores, porfavor modifiquelo'
    else:
		response.flash = 'Por favor rellene el formulario'
    return dict(formulario=formulario)

def subir():
    id_foto = db.fotos.insert(imagen=request.vars.foto)# buscar request.vars.dni   # guardar imagen en la base de datos
    reg = db(db.fotos.id==id_foto).select().first()  # buscar y obtener el registro de la base de datos:
    return {"foto": reg}
