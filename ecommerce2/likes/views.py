from django.shortcuts import render, redirect
from structure.models import  products
from .models import  like
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
        pdt = products.objects.get(productid = pk)
        if pdt.likes >= 1:
            pdt.likes -= 1
        print('unliked !!')
    
    if created == True:
        print('entering')
        pdt = products.objects.get(productid = pk)
        pdt.likes += 1
        pdt.save()
        print(pdt)

    return redirect('products:home',pk)


