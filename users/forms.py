from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        # fields = UserCreationForm.Meta.fields + ('age',)
        # fields = ['email','username','first_name','last_name','password1','password2'] + ['age']
        fields = ('email','username','first_name','last_name','age',)



class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email','username','first_name','last_name','age',)