from django.db.models import fields
from django.forms import ModelForm
from structure.models import orderdetails

class orderdetailsForm(ModelForm):
    class Meta:
        model = orderdetails
        fields = ['quantity',]
        exclude = ['orderdetailid','orderdetailnumber','order','product','price','discount','total','date']
    
    def __init__(self, *args, **kwargs):
        super(orderdetailsForm, self).__init__(*args, **kwargs)
        self.fields['quantity'].widget.attrs['min'] = 1
