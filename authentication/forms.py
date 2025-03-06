from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

User = get_user_model()  # Get the custom User model


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-field', 'placeholder': "Nom d'utilisateur"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-field', 'placeholder': "Mot de passe"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-field',
                                          'placeholder': "Confirmer mot de passe"})
    )

    class Meta:
        model = User  # Use the custom User model
        fields = ['username', 'password1', 'password2']


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-field', 'placeholder': "Nom d'utilisateur"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-field', 'placeholder': "Mot de passe"})
    )
