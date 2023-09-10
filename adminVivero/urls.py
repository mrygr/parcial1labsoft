from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),

    #Direccionamiento para los productores
    path('verProductores/', views.ver_productores, name='productor_ver'),
    path('crearProductor/', views.crear_productor, name='productor_crear'),
    path('verProductores/verDetalleProductor/<id_productor>/<nombre_productor>/<apellido_productor>/', views.ver_detalle_productor, name='productor_ver_detalle'),    
    path('verProductores/verDetalleProductor/<id_productor>/<nombre_productor>/<apellido_productor>/verDetalleProductorViveros/<id_finca>/', views.ver_detalle_productor_vivero, name='productor_ver_detalle_vivero'),

    #Direccionamiento para las Fincas
    path('verFincas/', views.ver_fincas, name='finca_ver'),
    path('crearFinca/', views.crear_finca, name='finca_crear'),

    #Direccionamiento para los vivieros
    path('verViveros/', views.ver_viveros, name='vivero_ver'),
    path('verViveros/verLaboresVivero/<id_vivero>/<tipo_cultivo>/', views.ver_detalle_labor_vivero, name='vivero_ver_detalle_labores'), 
    path('crearVivero/', views.crear_vivero, name='vivero_crear'),

    #Direccionamiento para las labores
    path('verLabores/', views.ver_labores, name='labor_ver'),
    path('crearLabor/', views.crear_labor, name='labor_crear'),

    #Direccionamiento para los productos que se utilizan en las labores
    path('verProductos/', views.ver_productos, name='producto_ver'),
    path('crearProducto/', views.crear_producto, name='producto_crear'),
]