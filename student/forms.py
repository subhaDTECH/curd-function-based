from django import forms 
from .models import User

class StudentForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['id','name','email','password','work']
        labels={'name':"Name",'email':"Email",'password':"Password",'work':"Work"}
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),
             'work':forms.TextInput(attrs={'class':'form-control'}),
        }
