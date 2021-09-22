from django.shortcuts import render, redirect
from structure.models import like , products
from datetime import date, datetime

# Create your views here.
def like_product(request,pk):
    
    liked , created = like.objects.get_or_create(
        liked_by = request.user ,
        liked_product = products.objects.get(productid = pk),
        defaults={'liked_time' : datetime.now()},)

    print(liked , created)

    if created == False:
        liked.delete()
        print('unliked !!')

    return redirect('products:home',pk)


