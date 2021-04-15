from django import forms

from .models_reportes_control_tmp import (
    TmpProxEvt, TmpEstatusEnvio, TmpMedioInscMod40, TmpMedioPatronSustituto,
    TmpMedioPensPso, TmpMedioTramCorr, TmpTipoTramCorr)


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


class frmTmpMedioPensPso(forms.ModelForm):

    class Meta:
        model = TmpMedioPensPso
        fields = [
            'medio',
        ]


class frmTmpMedioTramCorr(forms.ModelForm):

    class Meta:
        model = TmpMedioTramCorr
        fields = [
            'medio',
        ]


class frmTmpTipoTramCorr(forms.ModelForm):

    class Meta:
        model = TmpTipoTramCorr
        fields = [
            'medio',
        ]
