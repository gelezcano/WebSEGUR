# -*- coding: utf-8 -*-
# intente algo como
def index(): return dict(message="hello from guardia.py")

def user():
    return dict(formulario=auth())

@auth.requires_login()
def inicio():
    d = 4
    return dict(datos=d)
