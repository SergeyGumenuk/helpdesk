from django import forms
from django.contrib.auth.models import User

from customers.models import Profile


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='',
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
                               label='')


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
                               label='')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Repeat password'}),
                                label='')

    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {
            'username': '',
            'email': '',
        }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
        }
        help_texts = {
            'username': None,
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email already in used')
        return email

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_email(self):
        email = self.cleaned_data['email']
        invalid_email = User.objects.exclude(pk=self.instance.id).filter(email=email)
        if email in invalid_email:
            raise forms.ValidationError('This email already in used')
        return email


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo']
