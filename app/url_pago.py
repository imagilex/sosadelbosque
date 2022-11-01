from django.urls import path, include

import app.vw_cliente as views

object_name = 'pago'

urlpatterns = [
    path('cte/<pk>/', views.pago_index, name=f"{object_name}_index"),
    path('nuevo/<pk>/', views.pago_new, name=f"{object_name}_new"),
    path('actualizar/<pk>/', views.pago_update, name=f"{object_name}_update"),
    path('eliminar/<pk>/', views.pago_delete, name=f"{object_name}_delete"),
    path('pagado/<pk>/', views.pago_update_status, name=f"{object_name}_pagado"),
    ]
