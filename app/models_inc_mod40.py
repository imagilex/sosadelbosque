from django.db import models
from datetime import date

from .models_cliente import Cliente

def inicio_yr():
    return date.today().year+1

def fin_yr():
    return date.today().year+6

class IncrementoModalidad40(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, related_name="incrementos_m40")
    inicio = models.PositiveSmallIntegerField(
        verbose_name="Año de Inicio", default=inicio_yr)
    fin = models.PositiveSmallIntegerField(
        verbose_name="Año de Termino", default=fin_yr)
    tipo = models.CharField(
        choices=(("inicio", "Pago al inicio"), ("fin", "Pago al término")),
        default=inicio, max_length=10)
    monto = models.DecimalField(max_digits=7, decimal_places=2, default=0.0, verbose_name="Monto Mensual")

    def factor_cobro(self, anio):
        if anio <= 2022:
            return 10.075
        elif anio == 2023:
            return 11.166
        elif anio == 2024:
            return 12.256
        elif anio == 2025:
            return 13.347
        elif anio == 2026:
            return 14.438
        elif anio == 2027:
            return 15.528
        elif anio == 2028:
            return 16.619
        elif anio == 2029:
            return 17.709
        return 18.8

    @property
    def sdi(self):
        if self.tipo == "inicio":
            sm = float(self.monto) / self.factor_cobro(self.inicio)
            sdi = sm / 30.4
            monto = sdi * self.factor_cobro(self.inicio) * 30.4
            return monto / (self.factor_cobro(self.inicio) * 30.4) * 100
        else:
            sm = float(self.monto) / self.factor_cobro(self.fin)
            sdi = sm / 30.4
            monto = sdi * self.factor_cobro(self.inicio) * 30.4
            return monto / (self.factor_cobro(self.inicio) * 30.4) * 100

    @property
    def pagos(self):
        regs = list()
        for anio in range(self.inicio, self.fin + 1):
            if self.tipo == "inicio":
                sm = float(self.monto) / self.factor_cobro(self.inicio)
                sdi = sm / 30.4
                monto = sdi * self.factor_cobro(anio) * 30.4
                regs.append({
                    'anio':anio,
                    'cantidad': monto,
                    'diario': monto / 30.4,
                })
            else:
                sm = float(self.monto) / self.factor_cobro(self.fin)
                sdi = sm / 30.4
                monto = sdi * self.factor_cobro(anio) * 30.4
                regs.append({
                    'anio': anio,
                    'cantidad': monto,
                    'diario': monto / 30.4,
                })
        return regs

    class meta:
        ordering = ['inicio', 'fin', 'sdi']
