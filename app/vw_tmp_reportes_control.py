from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from datetime import datetime, date

from routines.mkitsafe import valida_acceso
from routines.utils import requires_jquery_ui

from .models import (
    TmpReporteControlRecepcion, TmpReporteControlProximoPensionMod40,
    TmpReporteControlPatronSustituto, TmpReporteControlPatronSustitutoDetalle,
    TmpReporteControlInscritosMod40, TmpReporteControlInscritosMod40Detalle,
    TmpProxEvt, TmpEstatusEnvio, TmpMedioInscMod40, TmpMedioPatronSustituto,
    TmpMedioPensPso, TmpMedioTramCorr, TmpTipoTramCorr,
    TmpReportPensionesEnProceso, TmpReportTramitesYCorrecciones,
    EstatusDeTramite, TmpEstatusPensPso, TmpEstatusTramCorr
    )
from .models import Usr, Cliente, TaxonomiaExpediente, UsrResponsables


class POSTParam():
    request = None
    def __init__(self, req):
        self.request = req
    def AsInt(self, var, req=None) -> int:
        if req:
            self.request = req
        return int("0" + self.request.POST.get(var, ''))
    def AsFloat(self, var, req=None) -> int:
        if req:
            self.request = req
        return float("0" + self.request.POST.get(var, ''))
    def AsDate(self, var, req=None) -> date:
        value = None
        if req:
            self.request = req
        if self.request.POST.get(var, None):
            value = datetime.strptime(
                self.request.POST.get(var),"%Y-%m-%d").date()
        return value
    def Date2Str(self, value) -> str:
        if value is None:
            return ""
        return value.strftime("%Y-%m-%d")
    def setOptionalField(self,field, key, req):
        value = req.POST.get(key, None)
        if value:
            field = value
        return field

@valida_acceso(['cliente.clientes_cliente'])
def admin(request, pk_cte):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    cte = Cliente.objects.get(pk=pk_cte)
    toolbar = [{
        'type': 'link_pk',
        'view': 'cliente_see',
        'pk': pk_cte,
        'label': 'Ver Cliente',
    }]
    if "POST" == request.method:
        reader = POSTParam(request)
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
        elif "add-pens-pso" == action:
            TmpReportPensionesEnProceso.objects.create(
                medio=TmpMedioPensPso.objects.get(pk=request.POST.get('medio')),
                estatus=TmpEstatusPensPso.objects.get(pk=request.POST.get('estatus')),
                fecha_de_envio=reader.AsDate('fecha_de_envio'),
                fecha_de_pago_inicial=reader.AsDate('fecha_de_pago_inicial'),
                fecha_de_retiro_total=reader.AsDate('fecha_de_retiro_total'),
                fecha_de_envio_p=reader.AsDate('fecha_de_envio_p'),
                fecha_de_correccion=reader.AsDate('fecha_de_correccion'),
                prorroga_o_incorformidad= request.POST.get('prorroga_o_incorformidad')=="yes",
                concluido= request.POST.get('concluido')=="yes",
                comentarios= request.POST.get('comentarios'),
                cliente=cte,
                autor=usuario
            )
        elif "update-pens-pso" == action:
            reg = TmpReportPensionesEnProceso.objects.get(
                pk=request.POST.get('id_record'))
            reg.medio = TmpMedioPensPso.objects.get(pk=request.POST.get('medio'))
            reg.estatus = TmpEstatusPensPso.objects.get(pk=request.POST.get('estatus'))
            reg.fecha_de_envio = reader.AsDate('fecha_de_envio')
            reg.fecha_de_pago_inicial = reader.AsDate('fecha_de_pago_inicial')
            reg.fecha_de_retiro_total = reader.AsDate('fecha_de_retiro_total')
            reg.fecha_de_envio_p = reader.AsDate('fecha_de_envio_p')
            reg.fecha_de_correccion = reader.AsDate('fecha_de_correccion')
            reg.prorroga_o_incorformidad = request.POST.get('prorroga_o_incorformidad') == "yes"
            reg.concluido = request.POST.get('concluido') == "yes"
            reg.comentarios = request.POST.get('comentarios')
            reg.save()
        elif "delete-pens-pso" == action:
            TmpReportPensionesEnProceso.objects.get(
                pk=request.POST.get('id_record')).delete()
        elif "add-tram-corr" == action:
            TmpReportTramitesYCorrecciones.objects.create(
                medio=TmpMedioTramCorr.objects.get(pk=request.POST.get('medio')),
                estatus=TmpEstatusTramCorr.objects.get(pk=request.POST.get('estatus')),
                tipo_de_tramite=TmpTipoTramCorr.objects.get(pk=request.POST.get('tipo_de_tramite')),
                fecha_de_envio=reader.AsDate('fecha_de_envio'),
                fecha_de_conclusion=reader.AsDate('fecha_de_conclusion'),
                costo=reader.AsFloat('costo'),
                fecha_de_liquidacion=reader.AsDate('fecha_de_liquidacion'),
                comentarios=request.POST.get('comentarios'),
                cliente=cte,
                autor=usuario
            )
        elif "update-tram-corr" == action:
            reg = TmpReportTramitesYCorrecciones.objects.get(
                pk=request.POST.get('id_record'))
            reg.medio = TmpMedioTramCorr.objects.get(pk=request.POST.get('medio'))
            reg.estatus = TmpEstatusTramCorr.objects.get(pk=request.POST.get('estatus'))
            reg.tipo_de_tramite = TmpTipoTramCorr.objects.get(pk=request.POST.get('tipo_de_tramite'))
            reg.fecha_de_envio = reader.AsDate('fecha_de_envio')
            reg.fecha_de_conclusion = reader.AsDate('fecha_de_conclusion')
            reg.costo = reader.AsFloat('costo')
            reg.fecha_de_liquidacion = reader.AsDate('fecha_de_liquidacion')
            reg.comentarios = request.POST.get('comentarios')
            reg.save()
        elif "delete-tram-corr" == action:
            TmpReportTramitesYCorrecciones.objects.get(
                pk=request.POST.get('id_record')).delete()
    return render(
        request,
        'app/cliente/tmp_reportes_control/admin.html', {
            'menu_main': usuario.main_menu_struct(),
            'titulo': 'Información de Control',
            'titulo_descripcion': cte,
            'toolbar': toolbar,
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
            'data_pens_pso': list(
                TmpReportPensionesEnProceso.objects.filter(cliente=cte)),
            'data_tram_corr': list(
                TmpReportTramitesYCorrecciones.objects.filter(cliente=cte)),
            'cbo_opt': {
                'TIPO_PROXIMO_EVTO': list(TmpProxEvt.objects.all()),
                'MEDIO_INSC_MOD40': list(TmpMedioInscMod40.objects.all()),
                'MEDIO_PATRON_SUST': list(TmpMedioPatronSustituto.objects.all()),
                'ESTATUS_ENVIO': list(TmpEstatusEnvio.objects.all()),
                'MEDIO_PENS_PSO': list(TmpMedioPensPso.objects.all()),
                'MEDIO_TRAM_CORR': list(TmpMedioTramCorr.objects.all()),
                'TIPO_TRAM_CORR': list(TmpTipoTramCorr.objects.all()),
                'ESTATUS_PENS_PSO': list(TmpEstatusPensPso.objects.all()),
                'ESTATUS_TRAM_CORR': list(TmpEstatusTramCorr.objects.all()),
            },
            })




@valida_acceso(['cliente.clientes_cliente'])
def vwReporteControlRecepcion(request):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    data = []
    reader = POSTParam(request)
    ftr_tipo_expediente = reader.AsInt('ftr_tipo_expediente')
    ftr_ejecutivo = reader.AsInt('ftr_ejecutivo')
    ftr_gestor = reader.AsInt('ftr_gestor')
    ftr_fecha_ultimo_contacto_inicio = reader.AsDate(
        'ftr_fecha_ultimo_contacto_inicio')
    ftr_fecha_ultimo_contacto_fin = reader.AsDate(
        'ftr_fecha_ultimo_contacto_fin')
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
            'titulo': 'Reporte de Recepción, Cartera en Espera y Otro Estatus',
            'req_ui': requires_jquery_ui(request),
            'regs': data,
            'filters': {
                'ftr_tipo_expediente': ftr_tipo_expediente,
                'ftr_ejecutivo': ftr_ejecutivo,
                'ftr_gestor': ftr_gestor,
                'ftr_fecha_ultimo_contacto_inicio':
                    reader.Date2Str(ftr_fecha_ultimo_contacto_inicio),
                'ftr_fecha_ultimo_contacto_fin':
                    reader.Date2Str(ftr_fecha_ultimo_contacto_fin),
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
    reader = POSTParam(request)
    ftr_tipo_expediente = reader.AsInt('ftr_tipo_expediente', '')
    ftr_ejecutivo = reader.AsInt('ftr_ejecutivo', '')
    ftr_gestor = reader.AsInt('ftr_gestor', '')
    ftr_tipo = reader.AsInt('ftr_tipo', '')
    ftr_fecha_evt_inicio = reader.AsDate('ftr_fecha_evt_inicio')
    ftr_fecha_evt_fin = reader.AsDate('ftr_fecha_evt_fin')
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
                'ftr_fecha_evt_inicio': reader.Date2Str(ftr_fecha_evt_inicio),
                'ftr_fecha_evt_fin': reader.Date2Str(ftr_fecha_evt_fin),
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
    reader = POSTParam(request)
    ftr_tipo_expediente = reader.AsInt('ftr_tipo_expediente', '')
    ftr_ejecutivo = reader.AsInt('ftr_ejecutivo', '')
    ftr_gestor = reader.AsInt('ftr_gestor', '')
    ftr_medio = reader.AsInt('ftr_medio', '')
    ftr_fecha_de_alta_inicio =reader.AsDate('ftr_fecha_de_alta_inicio')
    ftr_fecha_de_alta_fin =reader.AsDate('ftr_fecha_de_alta_fin')
    ftr_fecha_estimada_de_baja_inicio =reader.AsDate(
        'ftr_fecha_estimada_de_baja_inicio')
    ftr_fecha_estimada_de_baja_fin =reader.AsDate(
        'ftr_fecha_estimada_de_baja_fin')
    ftr_fecha_de_pago_inicio =reader.AsDate('ftr_fecha_de_pago_inicio')
    ftr_fecha_de_pago_fin =reader.AsDate('ftr_fecha_de_pago_fin')
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
            if reg.detalle.all().count():
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
            else:
                if ftr_fecha_de_pago_inicio or ftr_fecha_de_pago_fin:
                    pass
                else:
                    tmp_data.append({
                        'cliente': reg.cliente,
                        'medio': reg.medio,
                        'fecha_de_alta': reg.fecha_de_alta,
                        'fecha_estimada_de_baja': reg.fecha_estimada_de_baja,
                        'fecha_de_pago': "",
                        'cantidad': "",
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
                'ftr_fecha_de_alta_inicio': reader.Date2Str(ftr_fecha_de_alta_inicio),
                'ftr_fecha_de_alta_fin': reader.Date2Str(ftr_fecha_de_alta_fin),
                'ftr_fecha_estimada_de_baja_inicio': reader.Date2Str(ftr_fecha_estimada_de_baja_inicio),
                'ftr_fecha_estimada_de_baja_fin': reader.Date2Str(ftr_fecha_estimada_de_baja_fin),
                'ftr_fecha_de_pago_inicio': reader.Date2Str(ftr_fecha_de_pago_inicio),
                'ftr_fecha_de_pago_fin': reader.Date2Str(ftr_fecha_de_pago_fin),
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
    reader = POSTParam(request)
    ftr_tipo_expediente = reader.AsInt('ftr_tipo_expediente')
    ftr_ejecutivo = reader.AsInt('ftr_ejecutivo')
    ftr_gestor = reader.AsInt('ftr_gestor')
    ftr_medio = reader.AsInt('ftr_medio')
    ftr_estatus_de_envio = reader.AsInt('ftr_estatus_de_envio')
    ftr_fecha_de_alta_inicio = reader.AsDate('ftr_fecha_de_alta_inicio')
    ftr_fecha_de_alta_fin = reader.AsDate('ftr_fecha_de_alta_fin')
    ftr_fecha_estimada_de_baja_inicio = reader.AsDate(
        'ftr_fecha_estimada_de_baja_inicio')
    ftr_fecha_estimada_de_baja_fin = reader.AsDate(
        'ftr_fecha_estimada_de_baja_fin')
    ftr_fecha_de_pago_inicio = reader.AsDate('ftr_fecha_de_pago_inicio')
    ftr_fecha_de_pago_fin = reader.AsDate('ftr_fecha_de_pago_fin')
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
            if reg.detalle.all().count() > 0:
                for det in reg.detalle.all():
                    if det.isMaxDate:
                        addable = True
                        if ftr_fecha_de_pago_inicio and ftr_fecha_de_pago_inicio > det.fecha_de_pago:
                            addable = False
                        if ftr_fecha_de_pago_fin and ftr_fecha_de_pago_fin < det.fecha_de_pago:
                            addable = False
                        if ftr_estatus_de_envio and ftr_estatus_de_envio != det.estatus_de_envio.pk:
                            addable = False
                        if addable:
                            tmp_data.append({
                                'cliente': reg.cliente,
                                'medio': reg.medio,
                                'fecha_de_alta': reg.fecha_de_alta,
                                'fecha_estimada_de_baja': reg.fecha_estimada_de_baja,
                                'fecha_de_pago': det.fecha_de_pago,
                                'estatus_de_envio': det.estatus_de_envio,
                            })
            else:
                if ftr_fecha_de_pago_inicio or ftr_fecha_de_pago_fin or ftr_estatus_de_envio:
                    pass
                else:
                    tmp_data.append({
                        'cliente': reg.cliente,
                        'medio': reg.medio,
                        'fecha_de_alta': reg.fecha_de_alta,
                        'fecha_estimada_de_baja': reg.fecha_estimada_de_baja,
                        'fecha_de_pago': "",
                        'estatus_de_envio': "",
                    })
        data = tmp_data
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
                'ftr_fecha_de_alta_inicio': reader.Date2Str(ftr_fecha_de_alta_inicio),
                'ftr_fecha_de_alta_fin': reader.Date2Str(ftr_fecha_de_alta_fin),
                'ftr_fecha_estimada_de_baja_inicio': reader.Date2Str(ftr_fecha_estimada_de_baja_inicio),
                'ftr_fecha_estimada_de_baja_fin': reader.Date2Str(ftr_fecha_estimada_de_baja_fin),
                'ftr_fecha_de_pago_inicio': reader.Date2Str(ftr_fecha_de_pago_inicio),
                'ftr_fecha_de_pago_fin': reader.Date2Str(ftr_fecha_de_pago_fin),
                'ftr_estatus_de_envio': ftr_estatus_de_envio,
            },
            'combo_options': {
                'tipo_expediente': list(TaxonomiaExpediente.objects.all()),
                'responsables': UsrResponsables(),
                'medio': list(TmpMedioInscMod40.objects.all()),
                'estatus_envio': list(TmpEstatusEnvio.objects.all()),
            },
        }
    )

@valida_acceso(['cliente.clientes_cliente'])
def vwGenerarLCInscMod40(request):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    if "GET" == request.method:
        data = TmpReporteControlInscritosMod40.objects.filter(
            fecha_de_alta__lte=date.today(),
            fecha_estimada_de_baja__gte=date.today(),
            cliente__tipo__nombre__icontains="Mod 40 Inscr",
            medio__medio__icontains='internet'
        )
        return render(
            request,
            'app/cliente/tmp_reportes_control/gen_lc_inscrmod40.html',
            {
                'menu_main': usuario.main_menu_struct(),
                'titulo':
                    'Generador de Líneas de Captura de Inscritos a Modalidad 40',
                'req_ui': requires_jquery_ui(request),
                'regs': data,
                'hoy': date.today(),
            })
    elif "POST" == request.method:
        regs = request.POST.getlist("reg_pk", [])
        data = []
        for reg in regs:
            data.append(TmpReporteControlInscritosMod40Detalle.objects.create(
                raiz=TmpReporteControlInscritosMod40.objects.get(pk=int(reg)),
                fecha_de_pago=date.today(),
                estatus_de_envio=TmpEstatusEnvio.objects.get(
                    medio__icontains='pend'),
                autor=usuario
            ))
        return render(
            request,
            'app/cliente/tmp_reportes_control/gen_lc_inscrmod40_resultado.html',
            {
                'menu_main': usuario.main_menu_struct(),
                'titulo':
                    'Generador de Líneas de Captura de Inscritos a Modalidad 40',
                'req_ui': requires_jquery_ui(request),
                'regs': data,
            })


@valida_acceso(['cliente.clientes_cliente'])
def vwReporteControlPensionesEnProceso(request):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    data = []
    reader = POSTParam(request)
    ftr_tipo_expediente = reader.AsInt('ftr_tipo_expediente')
    ftr_ejecutivo = reader.AsInt('ftr_ejecutivo')
    ftr_gestor = reader.AsInt('ftr_gestor')
    ftr_medio = reader.AsInt('ftr_medio')
    ftr_fecha_de_envio_inicio = reader.AsDate('ftr_fecha_de_envio_inicio')
    ftr_fecha_de_envio_fin = reader.AsDate('ftr_fecha_de_envio_fin')
    ftr_fecha_de_pago_inicial_inicio = reader.AsDate(
        'ftr_fecha_de_pago_inicial_inicio')
    ftr_fecha_de_pago_inicial_fin = reader.AsDate(
        'ftr_fecha_de_pago_inicial_fin')
    ftr_fecha_de_retiro_total_inicio = reader.AsDate(
        'ftr_fecha_de_retiro_total_inicio')
    ftr_fecha_de_retiro_total_fin = reader.AsDate(
        'ftr_fecha_de_retiro_total_fin')
    ftr_estatus = reader.AsInt('ftr_estatus')
    if "POST" == request.method:
        data = TmpReportPensionesEnProceso.objects.all()
        if ftr_tipo_expediente:
            data = data.filter(cliente__tipo__pk=ftr_tipo_expediente)
        if ftr_ejecutivo:
            data = data.filter(cliente__responsable__pk=ftr_ejecutivo)
        if ftr_gestor:
            data = data.filter(cliente__gestor__pk=ftr_gestor)
        if ftr_medio:
            data = data.filter(medio__pk=ftr_medio)
        if ftr_fecha_de_envio_inicio:
            data = data.filter(
                fecha_de_envio__gte=ftr_fecha_de_envio_inicio)
        if ftr_fecha_de_envio_fin:
            data = data.filter(
                fecha_de_envio__lte=ftr_fecha_de_envio_fin)
        if ftr_fecha_de_pago_inicial_inicio:
            data = data.filter(
                fecha_de_pago_inicial__gte=ftr_fecha_de_pago_inicial_inicio)
        if ftr_fecha_de_pago_inicial_fin:
            data = data.filter(
                fecha_de_pago_inicial__lte=ftr_fecha_de_pago_inicial_fin)
        if ftr_fecha_de_retiro_total_inicio:
            data = data.filter(
                fecha_de_retiro_total__gte=ftr_fecha_de_retiro_total_inicio)
        if ftr_fecha_de_retiro_total_fin:
            data = data.filter(
                fecha_de_retiro_total__lte=ftr_fecha_de_retiro_total_fin)
        if ftr_estatus:
            data = data.filter(estatus__pk=ftr_estatus)
    return render(
        request,
        'app/cliente/tmp_reportes_control/reporte_pens_pso.html', {
            'menu_main': usuario.main_menu_struct(),
            'titulo': 'Reporte de Pensiones en Proceso',
            'req_ui': requires_jquery_ui(request),
            'regs': data,
            'filters': {
                'ftr_tipo_expediente': ftr_tipo_expediente,
                'ftr_ejecutivo': ftr_ejecutivo,
                'ftr_gestor': ftr_gestor,
                'ftr_medio': ftr_medio,
                'ftr_fecha_de_envio_inicio': reader.Date2Str(
                    ftr_fecha_de_envio_inicio),
                'ftr_fecha_de_envio_fin': reader.Date2Str(
                    ftr_fecha_de_envio_fin),
                'ftr_fecha_de_pago_inicial_inicio': reader.Date2Str(
                    ftr_fecha_de_pago_inicial_inicio),
                'ftr_fecha_de_pago_inicial_fin': reader.Date2Str(
                    ftr_fecha_de_pago_inicial_fin),
                'ftr_fecha_de_retiro_total_inicio': reader.Date2Str(
                    ftr_fecha_de_retiro_total_inicio),
                'ftr_fecha_de_retiro_total_fin': reader.Date2Str(
                    ftr_fecha_de_retiro_total_fin),
                'ftr_estatus': ftr_estatus,
            },
            'combo_options': {
                'tipo_expediente': list(TaxonomiaExpediente.objects.all()),
                'responsables': UsrResponsables(),
                'medio': list(TmpMedioPensPso.objects.all()),
                'estatus': list(TmpEstatusPensPso.objects.all()),
            },
        })

@valida_acceso(['cliente.clientes_cliente'])
def vwReporteControlTramitesYCorrecciones(request):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    data = []
    reader = POSTParam(request)
    ftr_tipo_expediente = reader.AsInt('ftr_tipo_expediente')
    ftr_ejecutivo = reader.AsInt('ftr_ejecutivo')
    ftr_gestor = reader.AsInt('ftr_gestor')
    ftr_medio = reader.AsInt('ftr_medio')
    ftr_fecha_de_envio_inicio = reader.AsDate('ftr_fecha_de_envio_inicio')
    ftr_fecha_de_envio_fin = reader.AsDate('ftr_fecha_de_envio_fin')
    ftr_fecha_de_conclusion_inicio = reader.AsDate(
        'ftr_fecha_de_conclusion_inicio')
    ftr_fecha_de_conclusion_fin = reader.AsDate('ftr_fecha_de_conclusion_fin')
    ftr_fecha_de_liquidacion_inicio = reader.AsDate(
        'ftr_fecha_de_liquidacion_inicio')
    ftr_fecha_de_liquidacion_fin = reader.AsDate('ftr_fecha_de_liquidacion_fin')
    ftr_tipo_de_tramite = reader.AsInt('ftr_tipo_de_tramite')
    ftr_estatus = reader.AsInt('ftr_estatus')
    if "POST" == request.method:
        data = TmpReportTramitesYCorrecciones.objects.all()
        if ftr_tipo_expediente:
            data = data.filter(cliente__tipo__pk=ftr_tipo_expediente)
        if ftr_ejecutivo:
            data = data.filter(cliente__responsable__pk=ftr_ejecutivo)
        if ftr_gestor:
            data = data.filter(cliente__gestor__pk=ftr_gestor)
        if ftr_medio:
            data = data.filter(medio__pk=ftr_medio)
        if ftr_tipo_de_tramite:
            data = data.filter(tipo_de_tramite__pk=ftr_tipo_de_tramite)
        if ftr_fecha_de_envio_inicio:
            data = data.filter(
                fecha_de_envio__gte=ftr_fecha_de_envio_inicio)
        if ftr_fecha_de_envio_fin:
            data = data.filter(
                fecha_de_envio__lte=ftr_fecha_de_envio_fin)
        if ftr_fecha_de_conclusion_inicio:
            data = data.filter(
                fecha_de_conclusion__gte=ftr_fecha_de_conclusion_inicio)
        if ftr_fecha_de_conclusion_fin:
            data = data.filter(
                fecha_de_conclusion__lte=ftr_fecha_de_conclusion_fin)
        if ftr_fecha_de_liquidacion_inicio:
            data = data.filter(
                fecha_de_liquidacion__gte=ftr_fecha_de_liquidacion_inicio)
        if ftr_fecha_de_liquidacion_fin:
            data = data.filter(
                fecha_de_liquidacion__lte=ftr_fecha_de_liquidacion_fin)
        if ftr_estatus:
            data = data.filter(estatus__pk=ftr_estatus)
    return render(
        request,
        'app/cliente/tmp_reportes_control/reporte_tram_corr.html', {
            'menu_main': usuario.main_menu_struct(),
            'titulo': 'Reporte de Trámites y Correcciones',
            'req_ui': requires_jquery_ui(request),
            'regs': data,
            'filters': {
                'ftr_tipo_expediente': ftr_tipo_expediente,
                'ftr_ejecutivo': ftr_ejecutivo,
                'ftr_gestor': ftr_gestor,
                'ftr_medio': ftr_medio,
                'ftr_tipo_de_tramite': ftr_tipo_de_tramite,
                'ftr_fecha_de_envio_inicio': reader.Date2Str(
                    ftr_fecha_de_envio_inicio),
                'ftr_fecha_de_envio_fin': reader.Date2Str(
                    ftr_fecha_de_envio_fin),
                'ftr_fecha_de_conclusion_inicio': reader.Date2Str(
                    ftr_fecha_de_conclusion_inicio),
                'ftr_fecha_de_conclusion_fin': reader.Date2Str(
                    ftr_fecha_de_conclusion_fin),
                'ftr_fecha_de_liquidacion_inicio': reader.Date2Str(
                    ftr_fecha_de_liquidacion_inicio),
                'ftr_fecha_de_liquidacion_fin': reader.Date2Str(
                    ftr_fecha_de_liquidacion_fin),
            },
            'combo_options': {
                'tipo_expediente': list(TaxonomiaExpediente.objects.all()),
                'responsables': UsrResponsables(),
                'medio': list(TmpMedioTramCorr.objects.all()),
                'tipo_tram': list(TmpTipoTramCorr.objects.all()),
                'estatus': list(TmpEstatusTramCorr.objects.all()),
            },
        })
