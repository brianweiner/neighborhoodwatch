from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    contact_phone = forms.CharField(help_text='Required. Format: Numbers Only')
    contact_email = forms.EmailField(help_text='Required. Format: Email Address')
    class Meta:
        model = User
        fields = ('username', 'contact_email', 'contact_phone', 'password1', 'password2', )
