from registration.forms import RegistrationForm
from django.contrib.auth import get_user_model
from django import forms

class MyRegistrationForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = get_user_model()

class MySimpleForm(forms.Form):
    title = forms.CharField;