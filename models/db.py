# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------
# This scaffolding model makes your app work on Google App Engine too
# File is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

if request.global_settings.web2py_version < "2.14.1":
    raise HTTP(500, "Requires web2py 2.13.3 or newer")

# -------------------------------------------------------------------------
# if SSL/HTTPS is properly configured and you want all HTTP requests to
# be redirected to HTTPS, uncomment the line below:
# -------------------------------------------------------------------------
# request.requires_https()

# -------------------------------------------------------------------------
# app configuration made easy. Look inside private/appconfig.ini
# -------------------------------------------------------------------------
from gluon.contrib.appconfig import AppConfig

# -------------------------------------------------------------------------
# once in production, remove reload=True to gain full speed
# -------------------------------------------------------------------------
myconf = AppConfig(reload=True)

if not request.env.web2py_runtime_gae:
    # ---------------------------------------------------------------------
    # if NOT running on Google App Engine use SQLite or other DB
    # ---------------------------------------------------------------------
    db = DAL(myconf.get('db.uri'),
             pool_size=myconf.get('db.pool_size'),
             migrate_enabled=myconf.get('db.migrate'),
             check_reserved=['all'])
else:
    # ---------------------------------------------------------------------
    # connect to Google BigTable (optional 'google:datastore://namespace')
    # ---------------------------------------------------------------------
    db = DAL('google:datastore+ndb')
    # ---------------------------------------------------------------------
    # store sessions and tickets there
    # ---------------------------------------------------------------------
    session.connect(request, response, db=db)
    # ---------------------------------------------------------------------
    # or store session in Memcache, Redis, etc.
    # from gluon.contrib.memdb import MEMDB
    # from google.appengine.api.memcache import Client
    # session.connect(request, response, db = MEMDB(Client()))
    # ---------------------------------------------------------------------

# -------------------------------------------------------------------------
# by default give a view/generic.extension to all actions from localhost
# none otherwise. a pattern can be 'controller/function.extension'
# -------------------------------------------------------------------------
response.generic_patterns = ['*'] if request.is_local else []
# -------------------------------------------------------------------------
# choose a style for forms
# -------------------------------------------------------------------------
response.formstyle = myconf.get('forms.formstyle')  # or 'bootstrap3_stacked' or 'bootstrap2' or other
response.form_label_separator = myconf.get('forms.separator') or ''

# -------------------------------------------------------------------------
# (optional) optimize handling of static files
# -------------------------------------------------------------------------
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

# -------------------------------------------------------------------------
# (optional) static assets folder versioning
# -------------------------------------------------------------------------
# response.static_version = '0.0.0'

# -------------------------------------------------------------------------
# Here is sample code if you need for
# - email capabilities
# - authentication (registration, login, logout, ... )
# - authorization (role based authorization)
# - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
# - old style crud actions
# (more options discussed in gluon/tools.py)
# -------------------------------------------------------------------------

from gluon.tools import Auth, Service, PluginManager

# host names must be a list of allowed host names (glob syntax allowed)
auth = Auth(db, host_names=myconf.get('host.names'))
service = Service()
plugins = PluginManager()

# -------------------------------------------------------------------------
# create all tables needed by auth if not custom tables
# -------------------------------------------------------------------------
auth.define_tables(username=False, signature=False)

# -------------------------------------------------------------------------
# configure email
# -------------------------------------------------------------------------
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else myconf.get('smtp.server')
mail.settings.sender = myconf.get('smtp.sender')
mail.settings.login = myconf.get('smtp.login')
mail.settings.tls = myconf.get('smtp.tls') or False
mail.settings.ssl = myconf.get('smtp.ssl') or False

# -------------------------------------------------------------------------
# configure auth policy
# -------------------------------------------------------------------------
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

# -------------------------------------------------------------------------
# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.
#
# More API examples for controllers:
#
# >>> db.mytable.insert(myfield='value')
# >>> rows = db(db.mytable.myfield == 'value').select(db.mytable.ALL)
# >>> for row in rows: print row.id, row.myfield
# -------------------------------------------------------------------------

# -------------------------------------------------------------------------
# after defining tables, uncomment below to enable auditing
# -------------------------------------------------------------------------
# auth.enable_record_versioning(db)


##SE DEFINE TABLA VISITANTES##

db.define_table('visitantes',
	db.Field('apellido','string'),
    db.Field('nombre','string'),
	db.Field ('dni','integer',unique=True),
    db.Field('nacionalidad','string'),
	db.Field('domicilio','string'),
    db.Field('GpoFechaHoraEntrada','datetime'),
    db.Field('GpoFechaHoraSalida','datetime'),
    db.Field('foto','upload',default=None),
    db.Field('destino','string'),
	db.Field('motivodevisita','string'),
    format='%(apellido,nombre)s'
    
                )

##VALIDACIONES TABLA VISITANTES
db.visitantes.apellido.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(15, error_message='Solo hasta 15 caracteres')
db.visitantes.apellido.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(15, error_message='Solo hasta 15 caracteres')
db.visitantes.nombre.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(15, error_message='Solo hasta 15 caracteres')
db.visitantes.nombre.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(15, error_message='Solo hasta 15 caracteres')
db.visitantes.dni.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio') ,IS_INT_IN_RANGE(2500000,100000000, error_message= 'Ingrese un DNI entre 2.500.000 y 100.000.000')
db.visitantes.motivodevisita.requires=IS_IN_SET(['reunion', 'inspeccion', 'recorrida'], zero=T('Selecciona motivo'))
db.visitantes.destino.requires=IS_IN_SET(['jefe','2dojefe', 'enc' , 'finanzas', 'cabuzo', 'caagua', 'finanzas'], zero=T('Selecciona destino'))



##SE DEFINE TABLA VEHICULOS##

db.define_table('vehiculos',
	db.Field('modelo','string'),
    db.Field('anio','integer'),
    db.Field ('patente',db.visitantes,'string',unique=True),
	db.Field ('color','string'),
    db.Field('observaciones','text'),
	)

##VALIDACIONES TABLA VEHICULOS##
db.vehiculos.modelo.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(15, error_message='Solo hasta 15 caracteres')
db.vehiculos.anio.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(4, error_message='Solo hasta 15 caracteres')
db.vehiculos.patente.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(15, error_message='Solo hasta 15 caracteres'),IS_ALPHANUMERIC()
db.vehiculos.color.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(15, error_message='Solo hasta 15 caracteres')


##SE DEFINE TABLA CARGOS##

db.define_table('cargos',
	db.Field('ni_cargo','id'),
	db.Field('nombre','string'),
    db.Field('descripcion','text'),
	db.Field('cantidad','integer'),
    db.Field('responsable','string'),            
  )          

##VALIDACIONES TABLA CARGOS##
db.cargos.nombre.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(15, error_message='Solo hasta 15 caracteres')
db.cargos.descripcion.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(4, error_message='Solo hasta 15 caracteres')
db.cargos.cantidad.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(15, error_message='Solo hasta 15 caracteres')
db.cargos.responsable.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(15, error_message='Solo hasta 15 caracteres')
    



##SE DEFINE TABLA PROVEEDORES##

db.define_table('proveedores',
                 db.Field('nombre_empresa','string'),
                 db.Field('localidad','string'),
                 db.Field('direccion','string'),
                 db.Field('numero_calle','integer'),
                 db.Field('telefono','integer'),
                 db.Field('email','string'))


##VALIDACIONES TABLA PROVEEDORES##
db.proveedores.nombre_empresa.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(15, error_message='Solo hasta 15 caracteres')
db.proveedores.localidad.requires=IS_NOT_EMPTY(error_message='Campo obligatorio')
db.proveedores.direccion.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(15, error_message='Solo hasta 15 caracteres')
db.proveedores.numero_calle.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(6, error_message='Solo hasta 6 caracteres')
db.proveedores.telefono.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(15, error_message='Solo hasta 15 caracteres')
db.proveedores.email.requires=IS_EMAIL(error_message='¡El mail no es válido!'), IS_LENGTH(30, error_message='Solo hasta 30 caracteres')


##SE DEFINE TABLA JGUARDIA##

db.define_table('jguardia',
                db.Field('codigo_jguardia','integer'),
                db.Field('dni','integer',unique=True),
                db.Field('apellido','string'),
                db.Field('nombre','string'),
                db.Field('usuario','string'),
                db.Field('password','password'))

##VALIDACIONES TABLA JGUARDIA##
db.jguardia.codigo_jguardia.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(4, error_message='Solo hasta 4 caracteres')
db.jguardia.dni.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio') ,IS_INT_IN_RANGE(2500000,100000000, error_message= 'Ingrese un DNI entre 2.500.000 y 100.000.000')
db.jguardia.apellido.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.jguardia.nombre.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.jguardia.usuario.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.jguardia.password.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(15, error_message='Solo hasta 15 caracteres')


###FOTOS

db.define_table('fotos',
                db.Field('listado'),
                db.Field('imagen','string'),
                )

# mostrar la imagen en los formularios:
db.fotos.imagen.widget = lambda campo,valor:IMG(_src=valor)

db.define_table('logueo',
                db.Field('usuarios'))
