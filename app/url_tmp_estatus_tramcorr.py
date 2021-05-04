from django.urls import path

import app.vw_tmp_reportes_control_estatus_tramcorr as views

object_name = 'tmpestatustramcorr'

urlpatterns = [
    path('', views.index,
         name="{}_index".format(object_name)),
    path('nuevo/', views.new,
         name="{}_new".format(object_name)),
    path('<pk>/', views.see,
         name="{}_see".format(object_name)),
    path('actualizar/<pk>/', views.update,
         name="{}_update".format(object_name)),
    path('eliminar/<pk>/', views.delete,
         name="{}_delete".format(object_name)),
]
