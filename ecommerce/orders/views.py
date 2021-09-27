from django.contrib.auth.models import User
from django.http import request
from django.http.response import Http404
from django.shortcuts import render,redirect
from homepage.forms import searchproductform
from structure.models import orderdetails , orders, payment , orderdetails
from datetime import datetime

from structure.models import products



# Create your views here.
def myorders(request):
    print('redirecting from  orders')
    form = searchproductform()
    
    cart_count = orderdetails.objects.filter(customer=request.user , order = None).count()

    myorders = orders.objects.all().filter(customerid=request.user)
    
    corres_order_details = orderdetails.objects.filter(order__in = myorders )

    order_details = orderdetails.objects.all().filter(customer = request.user , order = None)

    totalcost = 0

    for items in order_details:
        totalcost += (items.quantity) * items.product.unit_price






    context = {
        'form' : form , 
        'cart_count' : cart_count,
        'myorders' : myorders,
        'corres_order_details' : corres_order_details,
        'totalcost' : totalcost,
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

    #check if there are items in cart
    crt_empty = orderdetails.objects.filter(order = None , customer = request.user)
    print('ctemt ======================== ', crt_empty)
    
    if crt_empty:
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

        return render(request , 'orders/orderplaced.html')
    
    else:
        print('nothing in cart ')
        return render(request , 'orders/emptyorder.html')


def instantorder(request):
    pk = request.session['current_pdt_id']
    prod_item = products.objects.get(productid = pk)
    print('creating instant cart items for ' , prod_item.productname)
    orderdetail,createdorderdetails = orderdetails.objects.get_or_create(product__productid = pk , customer = request.user , order = None , defaults={
        'orderdetailnumber' :  int(str(request.user.id) + str(datetime.now().strftime('%Y%m%d'))) ,  'product' : prod_item, 'price' : prod_item.unit_price , 'quantity' : 1 , 'discount' : 0 , 'date' : datetime.now() 
        })

    if createdorderdetails == False:
        updating_quantity = orderdetail
        updating_quantity.quantity += 1
        updating_quantity.save()

    print('creating instant order !')

    totcost = 0

    order_details = orderdetails.objects.all().filter(product__productid = pk , customer = request.user , order = None)

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

    return render(request , 'orders/orderplaced.html')

