from django.shortcuts import redirect, render
from django.db.models import Sum

from structure.models import categories,orderdetails, products
from homepage.forms import searchproductform
from .forms import orderdetailsForm


# Create your views here.
def home(request):

    category = categories.objects.all()

    form = searchproductform()

    order_details = orderdetails.objects.all().filter(customer = request.user , order = None)

    totalcost = 0

    for items in order_details:
        totalcost += (items.quantity) * items.product.unit_price

    related = products.objects.all()
    cart_count = orderdetails.objects.filter(customer=request.user ,  order = None).count()


    

    context = {
        'category' : category,
        'form' : form ,
        'orderdetails' : order_details,
        'related_items' : related,
        'cart_count' : cart_count,
        'totalcost' : totalcost
    }
    return render(request, 'cart/cart.html' , context)


def updatecart(request,pk):
    
    if request.method == "GET":
        print(pk)

        category = categories.objects.all()

        form = searchproductform()

        currentorderdetail = orderdetails.objects.get(orderdetailid = pk)
        orderdetailupdateform = orderdetailsForm(instance=currentorderdetail)

        #order_details = orderdetails.objects.all().filter(order__customerid = request.user)
        related = products.objects.all()
        cart_count = orderdetails.objects.filter(customer=request.user , order = None).count()

        context = {
            'category' : category,
            'form' : form,
            'cart_count' : cart_count,
            'related_items' : related,
            'orderdetailupdateform' : orderdetailupdateform,
            'currentorderdetail' : currentorderdetail
        }

        return render(request, 'cart/updatecart.html' , context)

    elif request.method == "POST":
        print(request.POST)

        currentorderdetail = orderdetails.objects.get(orderdetailid = pk)
        updatedcart = orderdetailsForm(data=request.POST , instance=currentorderdetail)
        if updatedcart.is_valid():
            updatedcart.save()
        else:
            
            print('error in form contents !')

        return redirect('cart:home')

def removefromcart(request,pk):

    print('removing ', pk, ' from cart !')

    item = orderdetails.objects.get(orderdetailid = pk , customer = request.user )
    print('removing ' , item.product.productname)
    item.delete()


    return redirect('cart:home')