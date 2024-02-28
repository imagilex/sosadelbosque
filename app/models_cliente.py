from django.db import models
from datetime import date
import pandas as pd

from routines.utils import BootstrapColors
from initsys.models import Usr, Direccion
from .models_opcs import *


def UsuarioCliente():
    return list(
        item['idusuario']
        for item in Cliente.objects.all().values('idusuario'))


def UsuarioNoCliente():
    dfUsr = pd.DataFrame(
        list(Usr.objects.all().values('idusuario')), columns=['idusuario'])
    return dfUsr[~dfUsr.idusuario.isin(UsuarioCliente())]['idusuario'].to_list()


def UsrResponsables():
    resps = list()
    for pk in UsuarioNoCliente():
        item = Usr.objects.filter(pk=pk)[0]
        resps.append((item.pk, f"{item}"), )
    return resps


class TaxonomiaExpediente(models.Model):
    idtaxonomia = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    color = models.CharField(
        max_length=50, blank=True, choices=BootstrapColors,
        default=BootstrapColors[0][0])
    descripcion = models.TextField(
        blank=True, verbose_name="Descripción")
    mostrar_en_panel = models.BooleanField(default=False, blank=True)
    padre = models.ForeignKey(
        to="self",
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="hijos")

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return "{}".format(self.nombre).strip()

    def __unicode__(self):
        return self.__str__()


class Cliente(Usr):
    idcliente = models.AutoField(primary_key=True)
    fecha_nacimiento = models.DateField(
        verbose_name="Fecha de nacimiento", blank=True, default=date.today)
    CURP = models.CharField(max_length=18, blank=True)
    RFC = models.CharField(max_length=13, blank=True)
    NSS = models.CharField(max_length=15, blank=True)
    estado_civil = models.CharField(
        max_length=15,
        choices=ESTADOS_CIVILES,
        default=ESTADO_CIVIL_CASADO)
    conyuge = models.CharField(max_length=150, blank=True)
    clinica = models.CharField(
        max_length=150, blank=True, verbose_name="Clínica")
    subdelegacion = models.CharField(
        max_length=150, blank=True, verbose_name="Subdelegación")
    empresa = models.CharField(max_length=150, blank=True)
    domicilicio = models.ForeignKey(
        Direccion, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="cliente")
    telefono_oficina = models.CharField(
        max_length=10, blank=True, verbose_name="Teléfono de oficina")
    otro_telefono = models.CharField(
        max_length=10, blank=True, verbose_name="Otro teléfono")
    afore_actual = models.CharField(max_length=50, blank=True)
    fecha_afore_actual = models.DateField(blank=True, default=date.today)
    tipo = models.ForeignKey(
        TaxonomiaExpediente,
        on_delete=models.PROTECT,
        related_name='clientes')
    observaciones = models.TextField(blank=True)
    obs_semanas_cotizadas = models.TextField(
        blank=True, verbose_name="Semanas Cotizadas")
    obs_homonimia = models.TextField(
        blank=True, verbose_name="Homonimia")
    obs_duplicidad = models.TextField(
        blank=True, verbose_name="Duplicidad")
    responsable = models.ForeignKey(
        Usr,
        on_delete=models.SET_NULL,
        related_name="clientes_asignados",
        blank=True,
        null=True,
        verbose_name="Ejecutivo",
        #limit_choices_to={'idusuario__in':UsuarioNoCliente}
        )
    gestor = models.ForeignKey(
        Usr,
        on_delete=models.SET_NULL,
        related_name="clientes_gestionados",
        blank=True,
        null=True,
        verbose_name="Gestor",
        #limit_choices_to={'idusuario__in':UsuarioNoCliente}
        )
    datos_estadisticos = models.TextField(
        blank=True, verbose_name="Datos Estadísticos")
    detalle_servicio = models.TextField(
        blank=True, verbose_name="Detalle de Servicio")
    actualizado_por = models.CharField(max_length=100, blank=True)
    fecha_de_actualizacion = models.DateField(blank=True, default=date.today)

    @property
    def edad(self):
        anios = date.today().year - self.fecha_nacimiento.year
        if date.today().month < self.fecha_nacimiento.month:
            anios -= 1
        elif (date.today().month == self.fecha_nacimiento.month
                and date.today().day < self.fecha_nacimiento.day):
            anios -= 1
        return anios

    class Meta:
        ordering = ["last_name", "apellido_materno", "first_name"]

    def __str__(self):
        return "{} {} {} - {}".format(
            self.last_name,
            self.apellido_materno,
            self.first_name,
            self.pk,
            ).strip()

    def __unicode__(self):
        return self.__str__()

class Acuerdo(models.Model):
    idacuerdo = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, related_name="acuerdos")
    titulo = models.CharField(max_length=250)
    acuerdo = models.TextField()
    aceptado = models.BooleanField(default=False)
    ip = models.GenericIPAddressField(null=True, verbose_name="IP de aceptación")
    fechaHora = models.DateTimeField(null=True, verbose_name="Fecha de Aceptación")

    class Meta:
        ordering = ["titulo", 'aceptado', 'fechaHora']

    @property
    def acuerdoStr(self):
        return "\n".join([f"<p>{p}</p>" for p in self.acuerdo.split('\n')])
    def __str__(self):
        return f"<h3>{self.titulo}</h3>{self.acuerdoStr}"


STATUS_PAGO = (
    ('pendiente', 'Pendiente de Pago'),
    ('pagado', 'Pagado'),
    ('verificado', 'Pagado y Verificado')
)


CUENTAS_PAGO = (
    ('efectivo', 'Efectivo'),
    ('daniel azteca', 'Daniel Azteca'),
    ('daniel banamex', 'Daniel Banamex'),
    ('sosa del bosque', 'Sosa del Bosque'),
    ('rebeca', 'Rebeca'),
)
class Pago(models.Model):
    idpago = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, related_name="pagos")
    concepto = models.CharField(max_length=250)
    cantidad = models.DecimalField(max_digits=7, decimal_places=2)
    fecha_de_pago = models.DateTimeField(null=True, blank=True)
    estatus = models.CharField(
        max_length=20, choices=STATUS_PAGO, default='pendiente')
    cuenta = models.CharField(
        max_length=50, blank=True, choices=CUENTAS_PAGO, default='efectivo')

    class Meta:
        ordering = ["-estatus", "fecha_de_pago", 'idpago']


    @property
    def cta(self):
        for c in CUENTAS_PAGO:
            if self.cuenta == c[0]:
                return c[1]
        return self.cuenta
