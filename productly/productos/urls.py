from django.urls import path
from . import views
# expondria la ruta /productos/lala
app_name = 'productos'

urlpatterns = [
    path('', views.index, name='producto_index'),
    path('formulario', views.formulario, name='formulario'),
    path('<int:producto_id>', views.detalle,name='detalle')
]
