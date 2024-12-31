from django import forms
from .models import Food

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'description', 'category', 'price', 'image']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Taom nomi'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Taom tavsifi',
                'rows': 3
            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Narxi'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
        }

class MessageForm(forms.Form):
    subject = forms.CharField(
        max_length=200,
        required=True,
        label="Mavzu",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Xabar mavzusi'
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Xabar matni',
            'rows': 5
        }),
        required=True,
        label="Xabar"
    )