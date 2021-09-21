from django.shortcuts import render
from structure.models import like , products
from datetime import date, datetime

# Create your views here.
def likes(request,pk):
    
    liked , created = like.objects.get_or_create(
    liked_time = datetime.now() ,
    defaults={'liked_by': request.user , 'liked_product' : products.objects.get(productid = pk)},
)
