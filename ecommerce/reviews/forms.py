from django.db import models
from django.forms import ModelForm
from structure.models import reviews

class reviewForm(ModelForm):
    class Meta:
        model = reviews
        fields = '__all__'
        exclude = ['reviewed_by' , 'reviewed_product', 'stars' ]