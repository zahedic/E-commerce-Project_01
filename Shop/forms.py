from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation
from .models import Customer_Profile

# Registration
class CustomerRegistrationForm(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    email=forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model=User
        fields=['username','email','password1','password2']
        labels={'email':'Email'}
        widgets={'username':forms.TextInput(attrs={'class':'form-control'})}


#Login
class LoginFrom(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))

    password=forms.CharField(label=_('Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current_password','class':'form-control'}))

#Password Change
class MyPasswordChangeForm(PasswordChangeForm):
    old_password=forms.CharField(label=_('Old Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','autofocus':True,'class':'form-control'}))
    
    new_password1=forms.CharField(label=_('New Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new password','class':'form-control'}),help_text=password_validation.password_validators_help_text_html())


    new_password2=forms.CharField(label=_('Confirm New Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new password','class':'form-control'}))

#Password Reset for Forget Password
    
class MyPasswordResetForm(PasswordResetForm):
    email=forms.EmailField(label=_('Email'),max_length=254,widget=forms.EmailInput(attrs={'autocomplete':'email','class':'form-control'}))


#Set Password for Forget Password
class MySetPasswordForm(SetPasswordForm):
    new_password1=forms.CharField(label=_('New Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),help_text=password_validation.password_validators_help_text_html())

    new_password2=forms.CharField(label=_('Confirm New Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))


class Customer_Profile_Form(forms.ModelForm):
    class Meta:
        model=Customer_Profile
        fields=['name','phone','country','division','district','thana','vill_or_road','house_name','zipcode']

        widgets={'name':forms.TextInput(attrs={'class':'form-control'}),
        'phone':forms.NumberInput(attrs={'class':'form-control'}),
        'country':forms.Select(attrs={'class':'form-control'}),
        'division':forms.Select(attrs={'class':'form-control'}),
        'district':forms.TextInput(attrs={'class':'form-control'}),
        'thana':forms.TextInput(attrs={'class':'form-control'}),
        'vill_or_road':forms.TextInput(attrs={'class':'form-control'}),
        'house_name':forms.TextInput(attrs={'class':'form-control'}),
         'zipcode':forms.NumberInput(attrs={'class':'form-control'})}



    