from django import forms

class DjangoRegForm(forms.Form):
    username = forms.CharField(max_length=30, label='Your name:')
    email = forms.EmailField(label='E-Mail:')
    age = forms.CharField(max_length=2, label='Your age:')
    password = forms.CharField(max_length=10, label='Type your password:')
    re_password = forms.CharField(max_length=10, label='Retype your password:')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, label='Your name:')
    password = forms.CharField(max_length=30, label='Type your password:')

