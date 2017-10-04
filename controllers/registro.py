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
