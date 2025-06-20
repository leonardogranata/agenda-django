from django import forms
from django.core.exceptions import ValidationError
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'firstName', 'lastName', 'phone',
            'email', 'description', 'category',
        )
        widgets = {
            'firstName': forms.TextInput(
                attrs={
                    'placeholder': 'Escreva aqui',
                }
            ),
            
            'lastName': forms.TextInput(
                attrs={
                    'placeholder': 'Escreva aqui'
                }
            ),

            'phone': forms.TextInput(
                attrs={
                    'placeholder': 'Escreva aqui'
                }
            ),
        }
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': field.label
            })
