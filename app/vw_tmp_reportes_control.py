from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from datetime import datetime

from routines.mkitsafe import valida_acceso
from routines.utils import requires_jquery_ui

from .models import (
    TmpReporteControlRecepcion, TmpReporteControlProximoPensionMod40,
    TmpReporteControlPatronSustituto, TmpReporteControlPatronSustitutoDetalle,
    TmpReporteControlInscritosMod40, TmpReporteControlInscritosMod40Detalle,
    TmpProxEvt, TmpEstatusEnvio, TmpMedioInscMod40, TmpMedioPatronSustituto
    )
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
                tipo=TmpProxEvt.objects.get(pk=request.POST.get('tipo')),
                autor=usuario
            )
        elif "upd-prox-pension-mod40" == action:
            reg = TmpReporteControlProximoPensionMod40.objects.get(
                pk=request.POST.get('id_record'))
            reg.fecha_del_evento = request.POST.get('fecha_del_evento')
            reg.tipo = TmpProxEvt.objects.get(pk=request.POST.get('tipo'))
            reg.save()
        elif "delete-prox-pension-mod40" == action:
            TmpReporteControlProximoPensionMod40.objects.get(
                pk=request.POST.get('id_record')).delete()
        elif "add-patron-sustituto" == action:
            TmpReporteControlPatronSustituto.objects.create(
                cliente=cte,
                medio=TmpMedioPatronSustituto.objects.get(pk=request.POST.get('medio')),
                fecha_de_alta=request.POST.get('fecha_de_alta'),
                fecha_estimada_de_baja=request.POST.get('fecha_estimada_de_baja'),
                autor=usuario
            )
        elif "update-patron-sustituto" == action:
            reg = TmpReporteControlPatronSustituto.objects.get(
                pk=request.POST.get('id_record'))
            reg.medio = TmpMedioPatronSustituto.objects.get(pk=request.POST.get('medio'))
            reg.fecha_de_alta = request.POST.get('fecha_de_alta')
            reg.fecha_estimada_de_baja = request.POST.get('fecha_estimada_de_baja')
            reg.save()
        elif "delete-patron-sustituto" == action:
            TmpReporteControlPatronSustituto.objects.get(
                pk=request.POST.get('id_record')).delete()
        elif "add-patron-sustituto-detalle" == action:
            TmpReporteControlPatronSustitutoDetalle.objects.create(
                raiz=TmpReporteControlPatronSustituto.objects.get(
                    pk=request.POST.get('raiz')),
                fecha_de_pago=request.POST.get('fecha_de_pago'),
                cantidad=request.POST.get('cantidad'),
                autor=usuario
            )
        elif "update-patron-sustituto-detalle" == action:
            reg = TmpReporteControlPatronSustitutoDetalle.objects.get(
                pk=request.POST.get('id_record'))
            reg.fecha_de_pago = request.POST.get('fecha_de_pago')
            reg.cantidad = request.POST.get('cantidad')
            reg.save()
        elif "delete-patron-sustituto-detalle" == action:
            TmpReporteControlPatronSustitutoDetalle.objects.get(
                pk=request.POST.get('id_record')).delete()
        elif "add-insc-mod-40" == action:
            TmpReporteControlInscritosMod40.objects.create(
                medio=TmpMedioInscMod40.objects.get(pk=request.POST.get('medio')),
                fecha_de_alta=request.POST.get('fecha_de_alta'),
                fecha_estimada_de_baja=request.POST.get('fecha_estimada_de_baja'),
                cliente=cte,
                autor=usuario
            )
        elif "update-insc-mod-40" == action:
            reg = TmpReporteControlInscritosMod40.objects.get(
                pk=request.POST.get('id_record'))
            reg.medio=TmpMedioInscMod40.objects.get(pk=request.POST.get('medio'))
            reg.fecha_de_alta=request.POST.get('fecha_de_alta')
            reg.fecha_estimada_de_baja=request.POST.get('fecha_estimada_de_baja')
            reg.save()
        elif "delete-insc-mod-40" == action:
            TmpReporteControlInscritosMod40.objects.get(
                pk=request.POST.get('id_record')).delete()
        elif "add-insc-mod-40-detalle" == action:
            TmpReporteControlInscritosMod40Detalle.objects.create(
                raiz=TmpReporteControlInscritosMod40.objects.get(
                    pk=request.POST.get('raiz')),
                fecha_de_pago=request.POST.get('fecha_de_pago'),
                estatus_de_envio=TmpEstatusEnvio.objects.get(pk=request.POST.get('estatus_de_envio')),
                autor=usuario
            )
        elif "update-insc-mod-40-detalle" == action:
            reg = TmpReporteControlInscritosMod40Detalle.objects.get(
                pk=request.POST.get('id_record'))
            reg.fecha_de_pago = request.POST.get('fecha_de_pago')
            reg.estatus_de_envio = TmpEstatusEnvio.objects.get(pk=request.POST.get('estatus_de_envio'))
            reg.save()
        elif "delete-insc-mod-40-detalle" == action:
            TmpReporteControlInscritosMod40Detalle.objects.get(
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
            'data_patron_sustituo': list(
                TmpReporteControlPatronSustituto.objects.filter(
                    cliente=cte)),
            'data_insc_mod40': list(
                TmpReporteControlInscritosMod40.objects.filter(cliente=cte)),
            'cbo_opt': {
                'TIPO_PROXIMO_EVTO': list(TmpProxEvt.objects.all()),
                'MEDIO_INSC_MOD40': list(TmpMedioInscMod40.objects.all()),
                'MEDIO_PATRON_SUST': list(TmpMedioPatronSustituto.objects.all()),
                'ESTATUS_ENVIO': list(TmpEstatusEnvio.objects.all()),
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
    ftr_tipo = int("0" + request.POST.get('ftr_tipo', ''))
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
            data = data.filter(tipo__pk=ftr_tipo)
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
                'tipo_proximo_evto': list(TmpProxEvt.objects.all()),
            },
        }
    )


@valida_acceso(['cliente.clientes_cliente'])
def vwReporteControlPatronSustituto(request):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    data = []
    ftr_tipo_expediente = int("0" + request.POST.get('ftr_tipo_expediente', ''))
    ftr_ejecutivo = int("0" + request.POST.get('ftr_ejecutivo', ''))
    ftr_gestor = int("0" + request.POST.get('ftr_gestor', ''))
    ftr_medio = int("0" + request.POST.get('ftr_medio', ''))
    ftr_fecha_de_alta_inicio = request.POST.get(
        'ftr_fecha_de_alta_inicio', None)
    ftr_fecha_de_alta_inicio = datetime.strptime(
            ftr_fecha_de_alta_inicio, '%Y-%m-%d').date() if ftr_fecha_de_alta_inicio else None
    ftr_fecha_de_alta_fin = request.POST.get(
        'ftr_fecha_de_alta_fin', None)
    ftr_fecha_de_alta_fin = datetime.strptime(
            ftr_fecha_de_alta_fin, '%Y-%m-%d').date() if ftr_fecha_de_alta_fin else None
    ftr_fecha_estimada_de_baja_inicio = request.POST.get(
        'ftr_fecha_estimada_de_baja_inicio', None)
    ftr_fecha_estimada_de_baja_inicio = datetime.strptime(
            ftr_fecha_estimada_de_baja_inicio, '%Y-%m-%d').date() if ftr_fecha_estimada_de_baja_inicio else None
    ftr_fecha_estimada_de_baja_fin = request.POST.get(
        'ftr_fecha_estimada_de_baja_fin', None)
    ftr_fecha_estimada_de_baja_fin = datetime.strptime(
            ftr_fecha_estimada_de_baja_fin, '%Y-%m-%d').date() if ftr_fecha_estimada_de_baja_fin else None
    ftr_fecha_de_pago_inicio = request.POST.get(
        'ftr_fecha_de_pago_inicio', None)
    ftr_fecha_de_pago_inicio = datetime.strptime(
            ftr_fecha_de_pago_inicio, '%Y-%m-%d').date() if ftr_fecha_de_pago_inicio else None
    ftr_fecha_de_pago_fin = request.POST.get(
        'ftr_fecha_de_pago_fin', None)
    ftr_fecha_de_pago_fin = datetime.strptime(
            ftr_fecha_de_pago_fin, '%Y-%m-%d').date() if ftr_fecha_de_pago_fin else None
    if "POST" == request.method:
        data = TmpReporteControlPatronSustituto.objects.all()
        if ftr_tipo_expediente:
            data = data.filter(cliente__tipo__pk=ftr_tipo_expediente)
        if ftr_ejecutivo:
            data = data.filter(cliente__responsable__pk=ftr_ejecutivo)
        if ftr_gestor:
            data = data.filter(cliente__gestor__pk=ftr_gestor)
        if ftr_medio:
            data = data.filter(medio__pk=ftr_medio)
        if ftr_fecha_de_alta_inicio:
            data = data.filter(fecha_de_alta__gte=ftr_fecha_de_alta_inicio)
        if ftr_fecha_de_alta_fin:
            data = data.filter(fecha_de_alta__lte=ftr_fecha_de_alta_fin)
        if ftr_fecha_estimada_de_baja_inicio:
            data = data.filter(fecha_estimada_de_baja__gte=ftr_fecha_estimada_de_baja_inicio)
        if ftr_fecha_estimada_de_baja_fin:
            data = data.filter(fecha_estimada_de_baja__lte=ftr_fecha_estimada_de_baja_fin)
        tmp_data = []
        for reg in data:
            for det in reg.detalle.all():
                if det.isMaxDate:
                    addable = True
                    if ftr_fecha_de_pago_inicio and ftr_fecha_de_pago_inicio > det.fecha_de_pago:
                        addable = False
                    if ftr_fecha_de_pago_fin and ftr_fecha_de_pago_fin < det.fecha_de_pago:
                        addable = False
                    if addable:
                        tmp_data.append({
                            'cliente': reg.cliente,
                            'medio': reg.medio,
                            'fecha_de_alta': reg.fecha_de_alta,
                            'fecha_estimada_de_baja': reg.fecha_estimada_de_baja,
                            'fecha_de_pago': det.fecha_de_pago,
                            'cantidad': det.cantidad,
                        })
        data = tmp_data
    return render(
        request,
        'app/cliente/tmp_reportes_control/reporte_patronsustituto.html', {
            'menu_main': usuario.main_menu_struct(),
            'titulo': 'Reporte de Patrón Sustituto',
            'req_ui': requires_jquery_ui(request),
            'regs': data,
            'filters': {
                'ftr_tipo_expediente': ftr_tipo_expediente,
                'ftr_ejecutivo': ftr_ejecutivo,
                'ftr_gestor': ftr_gestor,
                'ftr_medio': ftr_medio,
                'ftr_fecha_de_alta_inicio':
                    ftr_fecha_de_alta_inicio.strftime(
                        "%Y-%m-%d") if not ftr_fecha_de_alta_inicio is None else '',
                'ftr_fecha_de_alta_fin':
                    ftr_fecha_de_alta_fin.strftime(
                        "%Y-%m-%d") if not ftr_fecha_de_alta_fin is None else '',
                'ftr_fecha_estimada_de_baja_inicio':
                    ftr_fecha_estimada_de_baja_inicio.strftime(
                        "%Y-%m-%d") if not ftr_fecha_estimada_de_baja_inicio is None else '',
                'ftr_fecha_estimada_de_baja_fin':
                    ftr_fecha_estimada_de_baja_fin.strftime(
                        "%Y-%m-%d") if not ftr_fecha_estimada_de_baja_fin is None else '',
                'ftr_fecha_de_pago_inicio':
                    ftr_fecha_de_pago_inicio.strftime(
                        "%Y-%m-%d") if not ftr_fecha_de_pago_inicio is None else '',
                'ftr_fecha_de_pago_fin':
                    ftr_fecha_de_pago_fin.strftime(
                        "%Y-%m-%d") if not ftr_fecha_de_pago_fin is None else '',
            },
            'combo_options': {
                'tipo_expediente': list(TaxonomiaExpediente.objects.all()),
                'responsables': UsrResponsables(),
                'medio': list(TmpMedioPatronSustituto.objects.all())
            },
        }
    )


@valida_acceso(['cliente.clientes_cliente'])
def vwReporteControlInscripcionModalidad40(request):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    data = []
    ftr_tipo_expediente = int("0" + request.POST.get('ftr_tipo_expediente', ''))
    ftr_ejecutivo = int("0" + request.POST.get('ftr_ejecutivo', ''))
    ftr_gestor = int("0" + request.POST.get('ftr_gestor', ''))
    ftr_medio = int("0" + request.POST.get('ftr_medio', ''))
    if "POST" == request.method:
        data = TmpReporteControlInscritosMod40.objects.all()
        if ftr_tipo_expediente:
            data = data.filter(cliente__tipo__pk=ftr_tipo_expediente)
        if ftr_ejecutivo:
            data = data.filter(cliente__responsable__pk=ftr_ejecutivo)
        if ftr_gestor:
            data = data.filter(cliente__gestor__pk=ftr_gestor)
        if ftr_medio:
            data = data.filter(medio__pk=ftr_medio)
    return render(
        request,
        'app/cliente/tmp_reportes_control/reporte_inscrmod40.html', {
            'menu_main': usuario.main_menu_struct(),
            'titulo': 'Reporte de Inscritos a Modalidad 40',
            'req_ui': requires_jquery_ui(request),
            'regs': data,
            'filters': {
                'ftr_tipo_expediente': ftr_tipo_expediente,
                'ftr_ejecutivo': ftr_ejecutivo,
                'ftr_gestor': ftr_gestor,
                'ftr_medio': ftr_medio,
            },
            'combo_options': {
                'tipo_expediente': list(TaxonomiaExpediente.objects.all()),
                'responsables': UsrResponsables(),
                'medio': list(TmpMedioInscMod40.objects.all())
            },
        }
    )
