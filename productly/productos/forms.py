from . import models
from django.forms import ModelForm


class ProductForm(ModelForm):
    class Meta:
        model = models.Product
        fields = ['nombre', 'stick', 'puntaje', 'category']
