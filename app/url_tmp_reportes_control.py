from django.urls import path, include

import app.vw_tmp_reportes_control as views

urlpatterns = [
    path('admin/<pk_cte>/',
         views.admin,
         name="tmp_reporte_control_admin"),
    path('recepcion/',
         views.vwReporteControlRecepcion,
         name="tmp_reporte_recepcion"),
    path('proximos-pension-modalidad40/',
         views.vwReporteControlProximosPensionMod40,
         name="tpm_reporte_proximospensionmod40"),
    path('patron-sustituto/',
         views.vwReporteControlPatronSustituto,
         name="tpm_reporte_patronsustito"),
    path('inscripcion-a-modalidad-40/',
         views.vwReporteControlInscripcionModalidad40,
         name="tpm_reporte_inscmod40"),
    path('pensiones-en-proceso',
         views.vwReporteControlPensionesEnProceso,
         name="tmp_reporte_pens_pso"),
    path('tramites-y-correcciones',
         views.vwReporteControlTramitesYCorrecciones,
         name="tmp_reporte_control_tram_corr"),

    path('lc-insc-mod40/',
         views.vwGenerarLCInscMod40,
         name="tmp_generar_lc_insc_mod40"),

    path('medio-inscripcion-modalidad-40/', include('app.url_tmp_medio_insc_mod_40')),
    path('estatus-de-envio/', include('app.url_tmp_estatus_envio')),
    path('medio-patron-sustituto/', include('app.url_tmp_medio_patron_sustituto')),
    path('proximo-evento/', include('app.url_tmp_prox_evt')),

    path('medio-pensiones-proceso/', include('app.url_tmp_medio_pensiones_proceso')),
    path('medio-tamites-correciones/', include('app.url_tmp_medio_tramites_correcciones')),
    path('tipo-tamites-correcciones/', include('app.url_tmp_tipo_tramites_correcciones')),

    path('estatus-de-pension-en-proceso/', include('app.url_tmp_estatus_penspso')),
    path('estatus-de-tramites-y-correcciones/', include('app.url_tmp_estatus_tramcorr')),
    ]

