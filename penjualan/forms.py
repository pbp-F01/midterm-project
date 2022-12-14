from django import forms
from penjualan.models import Laporan


class PenjualanForm(forms.ModelForm):
    class Meta:
        model = Laporan
        exclude = ("user",)
        fields = "__all__"