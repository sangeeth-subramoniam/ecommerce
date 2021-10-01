from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from structure.models import products

class productsForm(ModelForm):

    class Meta:
        model = products
        fields = '__all__'
