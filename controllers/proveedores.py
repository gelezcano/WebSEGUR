# -*- coding: utf-8 -*-
# try something like
def index(): return dict(message="hello from proveedores.py")

def registro_proveedor():
    formulario=SQLFORM(db.proveedores)
    if formulario.accepts(request.vars, session):
        response.flash = 'Formulario correctamente cargado'
    elif formulario.errors:
		response.flash = 'Su formulario contiene errores, porfavor modifiquelo'
    else:
		response.flash = 'Por favor rellene el formulario'
    return dict(formulario=formulario)
