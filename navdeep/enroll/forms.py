
from django import forms
from .models import add

class fo(forms.ModelForm):
    class Meta:
        model=add
        fields=['name','email','password']
        error_messages={'name':{'required':'Please enetr your good Name',"class":"error"},
                        'email':{'required':'Please enter your Email'}}
        widgets={'name':forms.TextInput(attrs={'class':'box','placeholder': 'Name'}),
                 'email':forms.TextInput(attrs={'class':'box','placeholder': 'Email'}),
                 'password':forms.PasswordInput(render_value=True,attrs={'class':'box','placeholder': 'Password'})}

        label_suffix={'name':'yoo','email':'','password=':''}