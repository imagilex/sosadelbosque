from django.urls import path

import app.vw_tmp_reportes_control as views

urlpatterns = [
    path('admin/<pk_cte>/',
         views.admin,
         name="tmp_reporte_control_admin"),
    path('recepcion/',
         views.vwReporteControlRecepcion,
         name="tmp_reporte_recepcion"),
    path('proximos-pension-modalidad40',
         views.vwReporteControlProximosPensionMod40,
         name="tpm_reporte_proximospensionmod40")
    ]

