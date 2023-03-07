import curses.ascii

from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

import imaplib
import email
from email.header import decode_header
import xmltodict
from time import sleep

from routines.utils import requires_jquery_ui
from .models_historialaboral import *


def str2pesos(cantidad):
    return float(cantidad.replace('$', '').replace(',', ''))


def clean(txt):
    return "".join(c if c.isalnum() else "_" for c in txt)


# @csrf_exempt
@xframe_options_exempt
def simulador(request):
    data = {
        'edad_qty': int(request.POST.get("edad_qty", 60)),
        'semanas_amt': int(request.POST.get("semanas_amt", 500)),
        'concubino_flg': request.POST.get("concubino_flg", "no") == "yes",
        'hijos_qty': int(request.POST.get("hijos_qty", 0)),
        'spd': str2pesos(request.POST.get('spd', "0")),
    }
    data['edad_qty'] = 65 if data['edad_qty'] > 65 else data['edad_qty']
    data['concubino_flg'] = True
    calculated = False
    results = {}
    if request.method == "POST":
        uma = UMA.objects.get(pk = getmaxUMA())
        uma_valor = uma.valor
        salario_promedio_diario = data['spd']
        salario_promedio_mensual = salario_promedio_diario * 365 / 12
        aux_cbi = salario_promedio_diario / float(uma_valor)
        cbis = Cuantiabasica.objects.all()
        porcentaje_cuantia_basica = float(cbis[0].porcentaje_de_cuantia_basica)
        porcentaje_incremento_anual = float(
            cbis[0].porcentaje_de_incremento_anual)
        for elem in cbis:
            if elem.salario_inicio <= aux_cbi and aux_cbi <= elem.salario_fin:
                porcentaje_cuantia_basica = float(
                    elem.porcentaje_de_cuantia_basica)
                porcentaje_incremento_anual = float(
                    elem.porcentaje_de_incremento_anual)
        semanas = data['semanas_amt'] - 500
        semanas_restantes = semanas % 52
        anios_incremento = ((semanas - semanas_restantes) / 52)
        if semanas_restantes >= 27:
            anios_incremento += 1
        elif semanas_restantes >= 13:
            anios_incremento += 0.5
        porcentaje_cuantia_basica_incremento = porcentaje_cuantia_basica \
                                               + anios_incremento \
                                               * porcentaje_incremento_anual
        porcentaje_factor_actualizacion = 1.11
        porcentaje_factor_edad = float(Factoredad.objects.get(
            edad = data['edad_qty']).factor_de_edad)
        porcentaje_asignaciones_familiares = 0
        if data['concubino_flg']:
            porcentaje_asignaciones_familiares += 15
        if data['hijos_qty'] > 0:
            porcentaje_asignaciones_familiares += data['hijos_qty'] * 10
        pension = (porcentaje_cuantia_basica_incremento / 100) \
                  * (porcentaje_factor_edad / 100) \
                  * (porcentaje_factor_actualizacion) \
                  * ( 1 + porcentaje_asignaciones_familiares / 100) \
                  * salario_promedio_mensual
        if salario_promedio_mensual > 0:
            porcentaje_pension = pension * 100 / salario_promedio_mensual
        else:
            porcentaje_pension = 0
        results = {
            'semanas_cotizadas': data['semanas_amt'],
            'porcentaje_cuantia_basica': porcentaje_cuantia_basica,
            'porcentaje_incremento_anual': porcentaje_incremento_anual,
            'porcentaje_cuantia_basica_incremento':
                porcentaje_cuantia_basica_incremento,
            'pension': pension,
            'porcentaje_pension': porcentaje_pension,
            'salario_promedio_mensual': salario_promedio_mensual,
            'salario_promedio_diario': salario_promedio_diario,
            'porcentaje_factor_edad': porcentaje_factor_edad,
            'porcentaje_factor_actualizacion': porcentaje_factor_actualizacion,
            'porcentaje_asignaciones_familiares':
                porcentaje_asignaciones_familiares,
        }
        calculated = True
    return render(
        request,
        'app/utilerias/simulador.html', {
            'menu_main': {'perms': None},
            'titulo': "Simulador de Pension IMSS Ley 73",
            'req_ui': requires_jquery_ui(request),
            'data': data,
            'results': results,
            'calculated': calculated,
        }
    )

def check_mail(request):
    imap = imaplib.IMAP4_SSL(settings.EMAIL_HOST)
    imap.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
    status, num = imap.select('INBOX',False)
    num = int(num[0])
    for idx in range(num, 0, -1):
        res, msg = imap.fetch(str(idx), "(RFC822)")
        for resp in msg:
            if isinstance(resp, tuple):
                msg = email.message_from_bytes(resp[1])
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding)
                if subject != "Simulador Pensión":
                    continue
                From, encoding = decode_header(msg["From"])[0]
                if isinstance(From, bytes):
                    From = From.decode(encoding)
                if msg.is_multipart():
                    for part in msg.walk():
                        ctype = part.get_content_type()
                        cdisp = str(part.get("Content-Disposition"))
                        try:
                            body = part.get_payload(decode=True).decode()
                        except:
                            pass
                        if ctype == "text/plain" and "attachment" not in cdisp:
                            break
                else:
                    ctype = msg.get_content_type()
                    body = msg.get_payload(decode=True).decode()
        data = xmltodict.parse(body)['html']['body']['table'][0]['tbody']['tr']['td']
        data = data['table']['tbody']['tr']['td']['table']['tbody']['tr']['td']
        data = data['table']['tbody']['tr']
        simData = list()
        for row in data:
            if isinstance(row['td'], list) and len(row['td'])==2:
                simData.append([row['td'][0]['#text'], row['td'][1]['#text'],])
        print(data)
        imap.copy(str(idx), 'INBOX.cotizaciones')
        imap.store(str(idx), '+FLAGS', '\\Deleted')
        imap.expunge()
        break
    imap.close()
    imap.logout()
    return render(
        request,
        'app/utilerias/simulador.html', {
            'menu_main': {'perms': None},
            'titulo': "Simulador de Pension IMSS Ley 73",
            'data': {
                'edad_qty': simData[0][1],
                'semanas_amt': simData[1][1],
                'hijos_qty': simData[2][1],
                'spd': simData[3][1],
            },
            'autosend': True,
        }
    )
