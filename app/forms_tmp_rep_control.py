from django import forms

from .models_reportes_control_tmp import (
    TmpProxEvt, TmpEstatusEnvio, TmpMedioInscMod40, TmpMedioPatronSustituto)


class frmTmpProxEvt(forms.ModelForm):

    class Meta:
        model = TmpProxEvt
        fields = [
            'medio',
        ]


class frmTmpEstatusEnvio(forms.ModelForm):

    class Meta:
        model = TmpEstatusEnvio
        fields = [
            'medio',
        ]


class frmTmpMedioInscMod40(forms.ModelForm):

    class Meta:
        model = TmpMedioInscMod40
        fields = [
            'medio',
        ]


class frmTmpMedioPatronSustituto(forms.ModelForm):

    class Meta:
        model = TmpMedioPatronSustituto
        fields = [
            'medio',
        ]
