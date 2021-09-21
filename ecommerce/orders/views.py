from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from homepage.forms import searchproductform
from structure.models import orderdetails , orders, payment , orderdetails
from datetime import datetime



# Create your views here.
def myorders(request):
    print('redirecting from  orders')
    form = searchproductform()
    cart_count = orderdetails.objects.filter(customer=request.user , order = None).count()

    myorders = orders.objects.all().filter(customerid=request.user)
    
    corres_order_details = orderdetails.objects.filter(order__in = myorders )






    context = {
        'form' : form , 
        'cart_count' : cart_count,
        'myorders' : myorders,
        'corres_order_details' : corres_order_details
    }

    return render(request, 'orders/myorders.html' , context)


def orderdetail(request, pk):
    print('order details ...')

    form = searchproductform()

    cart_count = orderdetails.objects.filter(customer = request.user).count()

    myorders = orderdetails.objects.all().filter(order__orderid = pk)

    context = {
        'form' : form ,
        'cart_count' : cart_count,
        'myorders' : myorders
    }

    return render(request, 'orders/myorderdetails.html' , context)


def createorder(request):
    print('creating order !')

    totcost = 0

    order_details = orderdetails.objects.all().filter(customer = request.user , order = None)

    for items in order_details:
        totcost += (items.quantity) * items.product.unit_price

    date_of_order = datetime.now()

    neworder = orders.objects.create(
        customerid = request.user,
        ordernumber = int(str(request.user.id) + str(datetime.now().strftime('%Y%m%d'))) ,
        paymentid = payment.objects.get(paymentid = 1) ,
        orderdate = date_of_order, 
        totalcost = totcost, 
        #shipment_date = datetime.strptime(date_of_order, "%m/%d/%y") + datetime.timedelta(days=7),
        shipment_date = '7 Days',
        transactionstatus = True,
        deliverystatus = False,
        deleted = False,
        paymentdate = date_of_order,
        order_complete = True        
        )


    print('new order created !! ')

    

    print('/n ' , neworder)
    
    neworder.save()

    for items in order_details:
        items.order = neworder
        items.save()

    print('cart items assignes to the created order !')

    return redirect('homepage:home')
