from django import forms
from django.forms import ModelForm, TextInput
from django.contrib.auth import get_user_model
from flights.models import  FlightDepartCode,FlightArriveCode
User = get_user_model()

class FlightDepartForm(ModelForm):
    class Meta:
        model = FlightDepartCode
        fields = ['code']
        widgets={'code':TextInput(attrs={'class':'theme-search-area-section-input typeahead','placeholder':'Departure','data-provide':'typeahead'})}

class FlightArriveForm(ModelForm):
    class Meta:
        model = FlightArriveCode
        fields = ['arrive_code']
        widgets={'arrive_code':TextInput(attrs={'class':'theme-search-area-section-input typeahead','placeholder':'Arrival','data-provide':'typeahead'})}

class ContactForm(forms.Form):
    fullname=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'fullname'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}))
    content=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'content'}))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not 'gmail.com' in email:
            raise forms.ValidationError('Email has to be gmail')
        return email

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'username'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}))

class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))
    password2 = forms.CharField(label='confirm password',widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))

    def clean_username(self):
        username=self.cleaned_data.get('username')
        qs=User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError('Username is taken')
        return username

    def clean_email(self):
        email=self.cleaned_data.get('email')
        qs=User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('email is taken')
        return email

    def clean(self):
        data=self.cleaned_data
        password=self.cleaned_data.get('password')
        password2=self.cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError('Passwords must match')
        return data

