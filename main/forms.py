
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class BlogUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Mot de passe",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    password2 = forms.CharField(
        label="Confirmer votre mot de passe",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("password1", "password2")

    





#login register
"""class UserForm(UserCreationForm):
    class Meta:
        model = User        
        fields = [
            'username',
            #'email',
            # 'first_name',
            # 'last_name',
            'password1',
            'password2',   ]"""
     