from django import forms
from django.contrib.auth.models import User
from django.forms.models import ModelForm
from django.http.response import HttpResponse
from SCE_Proj.models import bloguser
from django.contrib.auth.forms import UserCreationForm

#login form
class loginForm(forms.Form):
    email = forms.EmailField(max_length = 50)
    password = forms.CharField(widget = forms.PasswordInput(),max_length =30)
    class Meta:
        model = bloguser
    #email validation
    def clean_email(self):
        emailval = self.cleaned_data.get('email')
        #querying the database
        try:
            dbemail = bloguser.objects.get(email = emailval)
        except bloguser.DoesNotExist:
            raise forms.ValidationError("User does not exist in our db!")        
        return emailval
    #password validation
    def clean_password(self):
        passval = self.cleaned_data.get('password')
        emailval = self.cleaned_data.get('email')
        #querying the database
        try:
            dbpass = bloguser.objects.get(password = passval,email = emailval)
        except bloguser.DoesNotExist:
            raise forms.ValidationError("User does not exist in our db!")        
        return passval
#register form
class RegisterForm(forms.Form):
    name = forms.CharField(max_length =20,required=True)
    surname = forms.CharField(max_length = 20,required=True)
    email = forms.EmailField(max_length = 50,required= True)
    password = forms.CharField(widget = forms.PasswordInput(),max_length = 30,required=True)
    confirmpass = forms.CharField(widget = forms.PasswordInput(),max_length = 30,required=True)
    class Meta:
        model = bloguser
    #email validation
    def clean_email(self):
        emailval = self.cleaned_data.get('email')
        #querying the database
        try:
            dbemail = bloguser.objects.get(email = emailval)
        except bloguser.DoesNotExist:
            return emailval        
        raise forms.ValidationError("User already exist in our db!")  
    def clean_confirmpassword(self):
        passval = self.cleaned_data.get('password')
        passval2 = self.cleaned_data.get('confirmpass')
        if passval == passval2:
            return passval
        raise forms.ValidationError("passwords dont match !")
class settings_info(forms.Form):
    name = forms.CharField(max_length =20,required=False)
    surname = forms.CharField(max_length = 20,required=False)
    nickname = forms.CharField(max_length= 20,required = False)
    bio = forms.CharField(max_length=300,required = False)
    old_pass = forms.CharField(widget = forms.PasswordInput(),max_length = 30,required=False)
    password = forms.CharField(widget = forms.PasswordInput(),max_length = 30,required=False)
    confirmpass = forms.CharField(widget = forms.PasswordInput(),max_length = 30,required=False)

class new_post(forms.Form):
    title = forms.CharField(max_length=30,required = True)
    tags = forms.CharField(max_length=250,required = True)
    content = forms.CharField(max_length = 1000,required = True)

class search_form(forms.Form):
    search_string = forms.CharField(max_length=20,required = True)

class become_editor_form(forms.Form):
    content = forms.CharField(max_length=300,required=False)

class confirm_editor_form(forms.Form):
    email = forms.EmailField(max_length = 50,required= True)
