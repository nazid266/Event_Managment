from django import forms
from django.contrib.auth.models import User,Group,Permission
import re
from events.form import StyledFormMixin
from django.contrib.auth.forms import AuthenticationForm

class RegistationForm(StyledFormMixin,forms.ModelForm):
    
    password=forms.CharField(widget=forms.PasswordInput)
    conform_password=forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields=['username','first_name','last_name','password','conform_password','email']
        
        def clean_email(self):
            email=self.cleaned_data.get('email')
            email_exists=User.objects.filter(email=email).exists()
            if email_exists:
                raise forms.ValidationError("Email Alredy Exists")
            return email
        
        def clean_password(self):
            password=self.cleaned_data.get('password')
            errors=[]
            if len(password)<8:
                errors.append('password Must Be 8 Character Long')
                
            if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]',password):
                errors.append("Password must include Uppercase,Lowercase,number & Specialcharecter")  
                
            if errors:
                raise forms.ValidationError(errors)
            return password
        
        def clean(self):
            cleaned_data=super().clean()
            password=cleaned_data.get('password')
            conform_password=cleaned_data.get('conform_password')
            
            if password != conform_password:
                raise forms.ValidationError("password Do Not Match")
            return cleaned_data
        
class loginForm(StyledFormMixin,AuthenticationForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs) 
                 
                
class Assing_role(StyledFormMixin,forms.Form):
    role=forms.ModelChoiceField(
        queryset=Group.objects.all(),
        empty_label="Select a Role"
    )     
    
class Create_group_Form(StyledFormMixin,forms.ModelForm):
    permissions=forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Assign Permission'
    )
    class Meta:
        model=Group
        fields=["name","permissions"]
        
        
        
        
