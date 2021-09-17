from django.shortcuts import redirect, render
from structure.models import categories, orders, products , orderdetails, payment
from homepage.forms import searchproductform
from django.db.models import Q
from datetime import datetime


# Create your views here.
def home(request,pk):

    product = products.objects.get(productid = pk)
    form = searchproductform
    category = categories.objects.all()

    
    #related = products.objects.filter(Q(category__categoryid = product.category.categoryid) , ~Q(productid = product.productid)).order_by('unit_price')[:3]
    related = products.objects.all()
    cart_count = orderdetails.objects.filter(order__customerid=request.user).count()

    print('the pdt is ', product)

    context = {
        'product' : product,
        'form' : form,
        'category' : category,
        'related_items' : related,
        'cart_count' : cart_count
    }




    return render(request, 'product/producthome.html' , context)


def addtocart(request,pk):

    #first lets create an order to accomodate the products in the order details.. this will be done first time when there is no order with comlete status incomplete exist

    payment_mode = payment.objects.get(paymentid = 1)

    orderinst,createdorder = orders.objects.get_or_create(customerid = request.user , order_complete = False , defaults={
        'customerid' : request.user , 'orderdate' : datetime.now() , 'ordernumber' : str(str(request.user) + str(datetime.now())) , 'paymentdate' : datetime.now() , 'paymentid' : payment_mode })

    #print(order , created)

    prod_item = products.objects.get(productid = pk)

    orderdetail,createdorderdetails = orderdetails.objects.get_or_create(product__productid = pk , order__customerid = request.user , defaults={
        'orderdetailnumber' :  int(str(request.user.id) + str(datetime.now().strftime('%Y%m%d'))) , 'order' : orderinst , 'product' : prod_item, 'price' : prod_item.unit_price , 'quantity' : 1 , 'discount' : 0 , 'date' : datetime.now() 
        })

    if createdorderdetails == False:
        updating_quantity = orderdetail
        updating_quantity.quantity += 1
        updating_quantity.save()

    #print('order detail ie cart ' , orderdetail,createdorderdetails)


    return redirect('cart:home')