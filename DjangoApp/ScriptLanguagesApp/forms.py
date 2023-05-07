from django import forms
from .models import PC
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import PC
from django import forms
from django.utils.translation import gettext_lazy
from django.core.exceptions import ValidationError

class PCForm(forms.ModelForm):
    class Meta:
        model = PC
        fields = ['name', 'cpu', 'gpu', 'ram', 'psu', 'cpu_price', 'gpu_price', 'ram_price', 'psu_price']
        

class PCEditForm(forms.ModelForm):
    class Meta:
        model = PC
        fields = ['name', 'cpu', 'gpu', 'ram', 'psu', 'cpu_price', 'gpu_price', 'ram_price', 'psu_price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'cpu',
            'gpu',
            'ram',
            'psu',
            'cpu_price',
            'gpu_price',
            'ram_price',
            'psu_price',
            Submit('submit', 'Save')
        )
        self.helper.form_method = 'POST'

class NewUserForm(UserCreationForm):
    username = forms.CharField(label=gettext_lazy("Nazwa Użytkownika"))
    password1 = forms.CharField(label=gettext_lazy("Hasło"),widget=forms.PasswordInput)
    password2 = forms.CharField(label=gettext_lazy("Powtórz hasło"),widget=forms.PasswordInput)
    error_messages = {
        'password_mismatch': gettext_lazy("Podane hasła nie są identyczne."),
    }
    
    class Meta:
        model = User
        fields = ("username", "password1", "password2")
    
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        if commit:
            user.save()
        return user
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password1')

        if password and username and password.startswith(username):
            raise ValidationError(gettext_lazy("Hasło nie może zaczynać się od nazwy użytkownika."))
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].error_messages['required'] = gettext_lazy("To pole jest wymagane.")
        self.fields['username'].error_messages['unique'] = gettext_lazy("Użytkownik o tej nazwie już istnieje.")
        self.fields['password1'].error_messages['required'] = gettext_lazy("To pole jest wymagane.")
        self.fields['password2'].error_messages['required'] = gettext_lazy("To pole jest wymagane.")


class UserLoginForm(AuthenticationForm):
    username = UsernameField(label=gettext_lazy("Nazwa Użytkownika"),widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '', 'id': 'hello'}))
    password = forms.CharField(label=gettext_lazy("Hasło"),widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
            'id': 'hi',
        }
    ))
    
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.error_messages['invalid_login'] = 'Niepoprawne dane logowania'