from django.forms import ModelForm

from .models import Produse, CategoriiProduse


class ProductForm(ModelForm):
    class Meta:
        model = Produse
        fields = '__all__'


class CategoriiProduseForm(ModelForm):
    class Meta:
        model = CategoriiProduse
        fields = '__all__'
