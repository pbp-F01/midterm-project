from django import forms
from profileUMKM.models import ProfileUMKM


class ProfileUMKMForm(forms.ModelForm):
    class Meta:
        model = ProfileUMKM
        exclude = ("pemilik",)
        fields = "__all__"
