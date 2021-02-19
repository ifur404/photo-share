from django import forms
from django.forms import Select,Textarea,TextInput,FileInput
from .models import Photo,Category

class PhotoForm(forms.ModelForm):
    
    class Meta:
        model = Photo
        fields = ('category','description','images')
        widgets = {
            'category': Select(attrs={
                'class': 'form-control',
            }),
            'new_category': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'New Category',
            }),
            'description': Textarea(attrs={
                'class': 'form-control'
            }),
            'images': FileInput(attrs={
                'class': 'form-control'
            }),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
            }),
        }