from django.shortcuts import render
from structure.models import categories,orderdetails, products
from homepage.forms import searchproductform

# Create your views here.
def home(request):

    category = categories.objects.all()

    form = searchproductform()

    order_details = orderdetails.objects.all().filter(order__customerid = request.user)
    related = products.objects.all()
    

    context = {
        'category' : category,
        'form' : form ,
        'orderdetails' : order_details,
        'related_items' : related
    }
    return render(request, 'cart/cart.html' , context)