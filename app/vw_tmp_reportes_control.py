from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from datetime import datetime

from routines.mkitsafe import valida_acceso
from routines.utils import requires_jquery_ui

from .models import (
    TmpReporteControlRecepcion, TIPO_PROXIMO_EVTO,
    TmpReporteControlProximoPensionMod40)
from .models import Usr, Cliente, TaxonomiaExpediente, UsrResponsables

@valida_acceso(['cliente.clientes_cliente'])
def admin(request, pk_cte):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    cte = Cliente.objects.get(pk=pk_cte)
    if "POST" == request.method:
        action = request.POST.get('action')
        if "add-ultimo-contacto" == action:
            TmpReporteControlRecepcion.objects.create(
                cliente=cte,
                fecha_de_ultimo_contacto=request.POST.get(
                    'fecha_de_ultimo_contacto'),
                nota=request.POST.get('nota'),
                autor=usuario
            )
        elif "update-ultimo-contacto" == action:
            reg = TmpReporteControlRecepcion.objects.get(
                pk=request.POST.get('id_record'))
            reg.fecha_de_ultimo_contacto = request.POST.get(
                'fecha_de_ultimo_contacto')
            reg.nota = request.POST.get('nota')
            reg.save()
        elif "delete-ultimo-contacto" == action:
            TmpReporteControlRecepcion.objects.get(
                pk=request.POST.get('id_record')).delete()
        elif "add-prox-pension-mod40" == action:
            TmpReporteControlProximoPensionMod40.objects.create(
                cliente=cte,
                fecha_del_evento=request.POST.get('fecha_del_evento'),
                tipo=request.POST.get('tipo'),
                autor=usuario
            )
        elif "upd-prox-pension-mod40" == action:
            reg = TmpReporteControlProximoPensionMod40.objects.get(
                pk=request.POST.get('id_record'))
            reg.fecha_del_evento = request.POST.get('fecha_del_evento')
            reg.tipo = request.POST.get('tipo')
            reg.save()
        elif "delete-prox-pension-mod40" == action:
            TmpReporteControlProximoPensionMod40.objects.get(
                pk=request.POST.get('id_record')).delete()
    return render(
        request,
        'app/cliente/tmp_reportes_control/admin.html', {
            'menu_main': usuario.main_menu_struct(),
            'titulo': 'Información de Control',
            'titulo_descripcion': cte,
            'req_ui': requires_jquery_ui(request),
            'data_ultimo_contacto': list(
                TmpReporteControlRecepcion.objects.filter(cliente=cte)),
            'data_prox_pension_mod40': list(
                TmpReporteControlProximoPensionMod40.objects.filter(
                    cliente=cte)),
            'cbo_opt': {
                'TIPO_PROXIMO_EVTO': TIPO_PROXIMO_EVTO,
            },
            })

@valida_acceso(['cliente.clientes_cliente'])
def vwReporteControlRecepcion(request):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    data = []
    ftr_tipo_expediente = int("0" + request.POST.get('ftr_tipo_expediente', ''))
    ftr_ejecutivo = int("0" + request.POST.get('ftr_ejecutivo', ''))
    ftr_gestor = int("0" + request.POST.get('ftr_gestor', ''))
    ftr_fecha_ultimo_contacto_inicio = None
    if request.POST.get('ftr_fecha_ultimo_contacto_inicio', None):
        ftr_fecha_ultimo_contacto_inicio = datetime.strptime(
            request.POST.get('ftr_fecha_ultimo_contacto_inicio'),
            "%Y-%m-%d").date()
    ftr_fecha_ultimo_contacto_fin = None
    if request.POST.get('ftr_fecha_ultimo_contacto_fin', None):
        ftr_fecha_ultimo_contacto_fin = datetime.strptime(
            request.POST.get('ftr_fecha_ultimo_contacto_fin'),
            "%Y-%m-%d").date()
    if "POST" == request.method:
        data = TmpReporteControlRecepcion.objects.all()
        if ftr_tipo_expediente:
            data = data.filter(cliente__tipo__pk=ftr_tipo_expediente)
        if ftr_ejecutivo:
            data = data.filter(cliente__responsable__pk=ftr_ejecutivo)
        if ftr_gestor:
            data = data.filter(cliente__gestor__pk=ftr_gestor)
        if ftr_fecha_ultimo_contacto_inicio:
            data = data.filter(fecha_de_ultimo_contacto__gte=ftr_fecha_ultimo_contacto_inicio)
        if ftr_fecha_ultimo_contacto_fin:
            data = data.filter(fecha_de_ultimo_contacto__lte=ftr_fecha_ultimo_contacto_fin)
    data = [reg for reg in data if reg.isMaxDate]
    return render(
        request,
        'app/cliente/tmp_reportes_control/reporte_recepcion.html', {
            'menu_main': usuario.main_menu_struct(),
            'titulo': 'Reporte de Recepción, Cartera en Espera y Otros',
            'req_ui': requires_jquery_ui(request),
            'regs': data,
            'filters': {
                'ftr_tipo_expediente': ftr_tipo_expediente,
                'ftr_ejecutivo': ftr_ejecutivo,
                'ftr_gestor': ftr_gestor,
                'ftr_fecha_ultimo_contacto_inicio':
                    ftr_fecha_ultimo_contacto_inicio.strftime(
                        "%Y-%m-%d") if not ftr_fecha_ultimo_contacto_inicio is None else '',
                'ftr_fecha_ultimo_contacto_fin':
                    ftr_fecha_ultimo_contacto_fin.strftime(
                        "%Y-%m-%d") if not ftr_fecha_ultimo_contacto_fin is None else '',
            },
            'combo_options': {
                'tipo_expediente': list(TaxonomiaExpediente.objects.all()),
                'responsables': UsrResponsables(),
            },
        }
    )


@valida_acceso(['cliente.clientes_cliente'])
def vwReporteControlProximosPensionMod40(request):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    data = []
    ftr_tipo_expediente = int("0" + request.POST.get('ftr_tipo_expediente', ''))
    ftr_ejecutivo = int("0" + request.POST.get('ftr_ejecutivo', ''))
    ftr_gestor = int("0" + request.POST.get('ftr_gestor', ''))
    ftr_tipo = request.POST.get('ftr_tipo', '')
    ftr_fecha_evt_inicio = None
    if request.POST.get('ftr_fecha_evt_inicio', None):
        ftr_fecha_evt_inicio = datetime.strptime(
            request.POST.get('ftr_fecha_evt_inicio'),
            "%Y-%m-%d").date()
    ftr_fecha_evt_fin = None
    if request.POST.get('ftr_fecha_evt_fin', None):
        ftr_fecha_evt_fin = datetime.strptime(
            request.POST.get('ftr_fecha_evt_fin'),
            "%Y-%m-%d").date()
    if "POST" == request.method:
        data = TmpReporteControlProximoPensionMod40.objects.all()
        if ftr_tipo_expediente:
            data = data.filter(cliente__tipo__pk=ftr_tipo_expediente)
        if ftr_ejecutivo:
            data = data.filter(cliente__responsable__pk=ftr_ejecutivo)
        if ftr_gestor:
            data = data.filter(cliente__gestor__pk=ftr_gestor)
        if ftr_fecha_evt_inicio:
            data = data.filter(fecha_del_evento__gte=ftr_fecha_evt_inicio)
        if ftr_fecha_evt_fin:
            data = data.filter(fecha_del_evento__lte=ftr_fecha_evt_fin)
        if ftr_tipo:
            data = data.filter(tipo=ftr_tipo)
    return render(
        request,
        'app/cliente/tmp_reportes_control/reporte_proxpensionmod40.html', {
            'menu_main': usuario.main_menu_struct(),
            'titulo': 'Reporte de Próximos a Pension y/o Modalidad 40',
            'req_ui': requires_jquery_ui(request),
            'regs': data,
            'filters': {
                'ftr_tipo_expediente': ftr_tipo_expediente,
                'ftr_ejecutivo': ftr_ejecutivo,
                'ftr_gestor': ftr_gestor,
                'ftr_fecha_evt_inicio':
                    ftr_fecha_evt_inicio.strftime(
                        "%Y-%m-%d") if not ftr_fecha_evt_inicio is None else '',
                'ftr_fecha_evt_fin':
                    ftr_fecha_evt_fin.strftime(
                        "%Y-%m-%d") if not ftr_fecha_evt_fin is None else '',
                'ftr_tipo': ftr_tipo,
            },
            'combo_options': {
                'tipo_expediente': list(TaxonomiaExpediente.objects.all()),
                'responsables': UsrResponsables(),
                'tipo_proximo_evto': TIPO_PROXIMO_EVTO,
            },
        }
    )
