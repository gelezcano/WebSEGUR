# -*- coding: utf-8 -*-
# try something like
def index(): return dict(message="hello from consultas.py")



# -*- coding: utf-8 -*-
# try something like

def index(): return dict(message="hello from consultas.py")
    #def index():
"""    
def listado_visitantes():
    datos_visitantes=db().select(db.visitantes.ALL)
    return dict(dc=datos_visitantes)
"""
def listado_visitantes():
    search_text=request.get_vars.keywords
    grid = SQLFORM.grid(db.visitantes, search_widget=search_form,
        csv=False,
        deletable=False,
          )
    return dict(gridito=grid)

def listado_cargos():
    datos_cargos=db().select(db.cargos.ALL)
    return dict (dp=datos_cargos)

def listado_proveedores():
    search_text=request.get_vars.keywords
    grid = SQLFORM.grid(db.proveedores, search_widget=search_form,
        csv=False,
        deletable=False,
        fields=[db.proveedores.nombre_empresa,
                db.proveedores.localidad,
                db.proveedores.direccion,
                db.proveedores.numero_calle,
                db.proveedores.telefono,
                db.proveedores.email
                ]
        )
    return dict(gridito=grid)
