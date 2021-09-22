from django.db import models
from django.forms import ModelForm
from structure.models import reviews
from django import forms

class reviewForm(ModelForm):

    class Meta:
        model = reviews
        fields = '__all__'
        exclude = ['reviewed_by' , 'reviewed_product', 'stars' ]

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(reviewForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['review_title'].required = True
        self.fields['review_content'].required = True