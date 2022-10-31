from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUp(UserCreationForm):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    ROLES_CHOICES = [('K', 'Konsumen'),
                     ('I', 'Investor'),
                     ('P', 'Pemilik'), ]
    roles = forms.ChoiceField(
        label="Roles",
        required=True,
        choices=ROLES_CHOICES,
        widget=forms.RadioSelect()
    )

    class Meta:
        model = User
        fields = ['username', 'name', 'email', 'roles', 'password1']

    def save(self, commit=True):
        user = super(SignUp, self).save(commit=False)
        user.name = self.cleaned_data["name"]
        user.email = self.cleaned_data["email"]
        user.roles = self.cleaned_data["roles"]

        if commit:
            user.save()

        return user
