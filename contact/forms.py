from django import forms
from django.core.exceptions import ValidationError
from .models import Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*'
            }
        ),
        required=False
    )

    remove_picture = forms.BooleanField(
        required=False,
        label='Remover imagem'
    )

    class Meta:
        model = Contact
        fields = (
            'firstName', 'lastName', 'phone',
            'email', 'description', 'category', 'picture'
        )
        widgets = {
            'firstName': forms.TextInput(
                attrs={
                    'placeholder': 'Escreva seu nome',
                }
            ),
            
            'lastName': forms.TextInput(
                attrs={
                    'placeholder': 'Escreva seu sobrenome'
                }
            ),

            'phone': forms.TextInput(
                attrs={
                    'placeholder': 'Escreva seu telefone'
                }
            ),

            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Digite seu e-mail'
                }
            ),

            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Escreva uma descrição',
                    'type': 'textarea'
                }
            ),

            'remove_picture': forms.CheckboxInput(
                attrs={
                    'class': 'remove-image'
                }
            )
        }
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': field.label
            })


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username', 'password1', 'password2',
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('Já existe este e-mail', code='invalid')
            )
        return email
    
class RegisterUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username',
        )