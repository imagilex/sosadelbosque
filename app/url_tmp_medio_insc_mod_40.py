from django.urls import path

import app.vw_tmp_reportes_control_medio_insc_mod_40 as views

object_name = 'tmpmedioinscmod40'

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
