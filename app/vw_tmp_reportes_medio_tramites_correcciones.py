from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render


from routines.mkitsafe import valida_acceso
from routines.utils import requires_jquery_ui
from initsys.models import Usr

from .models_reportes_control_tmp import TmpMedioTramCorr
from .forms_tmp_rep_control import frmTmpMedioTramCorr


@valida_acceso()
def index(request):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    data = list(TmpMedioTramCorr.objects.all())
    toolbar = []
    toolbar.append({
        'type': 'link',
        'view': 'tmpmediotramcorr_new',
        'label': '<i class="far fa-file"></i> Nuevo'})
    perms = {
        'see': True,
        'update': True,
        'delete': True,
    }
    return render(request, 'app/cliente/tmp_reportes_control/index_medio_tram_corr.html', {
        'menu_main': usuario.main_menu_struct(),
        'titulo': 'Medio de Trámites y Correcciones',
        'data': data,
        'toolbar': toolbar,
        'req_ui': requires_jquery_ui(request),
        'cperms': perms,
    })


@valida_acceso()
def new(request):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    frm = frmTmpMedioTramCorr(request.POST or None)
    if 'POST' == request.method and frm.is_valid():
        obj = frm.save(commit=False)
        obj.created_by = usuario
        obj.updated_by = usuario
        obj.save()
        return HttpResponseRedirect(reverse('tmpmediotramcorr_see', kwargs={
            'pk': obj.pk
        }))
    return render(request, 'global/form.html', {
        'menu_main': usuario.main_menu_struct(),
        'titulo': 'Medio de Trámites y Correcciones',
        'titulo_descripcion': 'Nuevo',
        'frm': frm,
    })


@valida_acceso()
def see(request, pk):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    if not TmpMedioTramCorr.objects.filter(pk=pk).exists():
        return HttpResponseRedirect(reverse('item_no_encontrado'))
    obj = TmpMedioTramCorr.objects.get(pk=pk)
    frm = frmTmpMedioTramCorr(instance=obj)
    toolbar = []
    toolbar.append({
        'type': 'link',
        'view': 'tmpmediotramcorr_index',
        'label': '<i class="fas fa-list-ul"></i> Ver todos'})
    toolbar.append({
        'type': 'link_pk',
        'view': 'tmpmediotramcorr_update',
        'label': '<i class="far fa-edit"></i> Actualizar',
        'pk': pk})
    toolbar.append({
        'type': 'link_pk_del',
        'view': 'tmpmediotramcorr_delete',
        'label': '<i class="far fa-trash-alt"></i> Eliminar',
        'pk': pk})
    return render(request, 'global/form.html', {
        'menu_main': usuario.main_menu_struct(),
        'titulo': 'Medio de Trámites y Correcciones',
        'titulo_descripcion': obj,
        'frm': frm,
        'read_only': True,
        'toolbar': toolbar,
    })


@valida_acceso()
def update(request, pk):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    if not TmpMedioTramCorr.objects.filter(pk=pk).exists():
        return HttpResponseRedirect(reverse('item_no_encontrado'))
    obj = TmpMedioTramCorr.objects.get(pk=pk)
    frm = frmTmpMedioTramCorr(instance=obj, data=request.POST or None)
    if "POST" == request.method and frm.is_valid():
        obj = frm.save(commit=False)
        obj.updated_by = usuario
        obj.save()
        return HttpResponseRedirect(reverse(
            'tmpmediotramcorr_see', kwargs={'pk': obj.pk}))
    return render(request, 'global/form.html', {
        'menu_main': usuario.main_menu_struct(),
        'titulo': 'Medio de Trámites y Correcciones',
        'titulo_descripcion': obj,
        'frm': frm,
    })


@valida_acceso()
def delete(request, pk):
    usuario = Usr.objects.filter(id=request.user.pk)[0]
    if not TmpMedioTramCorr.objects.filter(pk=pk).exists():
        return HttpResponseRedirect(reverse('item_no_encontrado'))
    obj = TmpMedioTramCorr.objects.get(pk=pk)
    try:
        obj.delete()
        return HttpResponseRedirect(reverse('tmpmediotramcorr_index'))
    except ProtectedError:
        return HttpResponseRedirect(reverse('item_con_relaciones'))
