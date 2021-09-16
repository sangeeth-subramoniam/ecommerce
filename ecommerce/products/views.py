from django.shortcuts import render
from structure.models import categories, products
from homepage.forms import searchproductform
from django.db.models import Q

# Create your views here.
def home(request,pk):

    product = products.objects.get(productid = pk)
    form = searchproductform
    category = categories.objects.all()

    
    #related = products.objects.filter(Q(category__categoryid = product.category.categoryid) , ~Q(productid = product.productid)).order_by('unit_price')[:3]
    related = products.objects.all()

    print('the pdt is ', product)

    context = {
        'product' : product,
        'form' : form,
        'category' : category,
        'related_items' : related
    }




    return render(request, 'product/producthome.html' , context)