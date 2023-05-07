from django import forms
from .models import PC
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import PC

class PCForm(forms.ModelForm):
    class Meta:
        model = PC
        fields = ['name', 'cpu', 'gpu', 'ram', 'psu', 'cpu_price', 'gpu_price', 'ram_price', 'psu_price']
        

class PCEditForm(forms.ModelForm):
    class Meta:
        model = PC
        fields = '__all__'

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
    class Meta:
        model = User
        fields = ("username", "password1", "password2")
    
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        if commit:
            user.save()
        return user


class UserLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '', 'id': 'hello'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
            'id': 'hi',
        }
    ))
    
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.error_messages['invalid_login'] = 'Niepoprawne dane logowania'