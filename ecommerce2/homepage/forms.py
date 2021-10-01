from django.db.models import fields
from django.forms import ModelForm
from structure.models import products

class searchproductform(ModelForm):

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(searchproductform, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['productname'].required = False


    class Meta:
        model = products
        fields = ['productname']

        
