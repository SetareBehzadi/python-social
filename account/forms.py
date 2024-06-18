from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=60, widget= forms.TextInput(attrs={'class':'form-control', "placeholder": "Your username"}))
    email = forms.EmailField(widget= forms.EmailInput(attrs={'class':'form-control',"placeholder": "Your email"}))
    password = forms.CharField(label='password', min_length=5, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    passwordConfirm = forms.CharField(label='confirm-password',min_length=5, widget=forms.PasswordInput(attrs={'class':'form-control'}))


    def clean_email(self):
        user = User.objects.filter(email=self.cleaned_data['email']).exists()
        if user:
            raise ValidationError('this email ia already exist!')
        return self.cleaned_data['email']

    def clean_username(self):
        user = User.objects.filter(username=self.cleaned_data['username']).exists()
        if user:
            raise ValidationError('this username ia already exist!')
        return self.cleaned_data['username']

    def clean(self):
        cd = super().clean()
        p1 = cd.get('password')
        p2 = cd.get('passwordConfirm')

        if p1 and p2 and p1 != p2 :
            raise ValidationError('Password is not valid!')


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=60, widget= forms.TextInput(attrs={'class':'form-control', "placeholder": "Your username"}))
    password = forms.CharField(label='password', min_length=5,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserForgetPasswordForm(forms.Form):
    password = forms.CharField(label='password', min_length=5,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    re_password = forms.CharField(label='repeat-password', min_length=5,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
