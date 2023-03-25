from django import forms
from django.core.exceptions import ValidationError

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'category', 'description', 'image')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'category': forms.Select(attrs={'class': 'form-control form-control-lg'}),
            'description': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
        }
        labels = {
            'name': 'Наименование',
            'category': 'Категория',
            'description': 'Описание',
            'image': 'Изображения'
        }

    def clean(self):
        cleaned_data = super().clean()
        if len(cleaned_data['name']) < 2 or len(cleaned_data['description']) < 2:
            raise ValidationError("Длина поле должна быть больше двух символов")
        return cleaned_data


class SearchForm(forms.Form):
    search = forms.CharField(max_length=20, required=False, label='')
