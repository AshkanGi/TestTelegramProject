from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-group'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-group'}))

    def clean(self):
        cd = super().clean()
        username = cd.get('username')
        password = cd.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError('نام کاربری یا رمز عبور اشتباه است')
        return cd