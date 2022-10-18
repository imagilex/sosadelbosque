from django.urls import path, include

import app.vw_cliente as views

object_name = 'incmod40'

urlpatterns = [
    path('cte/<pk>/', views.incmod40_index, name=f"{object_name}_index"),
    path('nuevo/<pk>/', views.incmod40_new, name=f"{object_name}_new"),
    path('actualizar/<pk>/', views.incmod40_update, name=f"{object_name}_update"),
    path('eliminar/<pk>/', views.incmod40_delete, name=f"{object_name}_delete"),
    ]
