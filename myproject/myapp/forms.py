from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser 
from .models import CatPost


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']

class CatPostForm(forms.ModelForm):
    class Meta:
        model = CatPost
        fields = ['cat_name', 'breed', 'pet_name', 'description', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }