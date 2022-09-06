from django.urls import path, include

import app.vw_cliente as views

object_name = 'acuerdo'

urlpatterns = [
    path('cte/<pk>/', views.acuerdo_index, name=f"{object_name}_index"),
    path('nuevo/<pk>/', views.acuerdo_new, name=f"{object_name}_new"),
    path('<pk>', views.acuerdo_see, name=f"{object_name}_see"),
    path('actualizar/<pk>/', views.acuerdo_update, name=f"{object_name}_update"),
    path('eliminar/<pk>/', views.acuerdo_delete, name=f"{object_name}_delete"),
    path('mis-acuerdos', views.acuerdo_index_usr, name=f"{object_name}_index_usr"),
    ]
