from django.shortcuts import redirect, render
from structure.models import categories, orders, products , orderdetails, payment , reviews
from likes.models import like
from homepage.forms import searchproductform
from django.db.models import Q
from datetime import datetime
from reviews.forms import reviewForm
from .forms import productsForm


# Create your views here.
def home(request,pk):

    

    product = products.objects.get(productid = pk)

    request.session['current_pdt_id'] = pk
    request.session['current_pdt_name'] = product.productname
    request.session['current_pdt_price'] = product.unit_price
    request.session['current_pdt_pic'] = product.picture.url
    request.session.modified = True

    form = searchproductform
    category = categories.objects.all()

    reviewform = reviewForm()

    try:
        liked = like.objects.get(liked_product__productid = pk ,liked_by = request.user)
    except:
        liked = None

    if liked:
        liked = True
    else:
        liked = False
    

    
    #related = products.objects.filter(Q(category__categoryid = product.category.categoryid) , ~Q(productid = product.productid)).order_by('unit_price')[:3]
    related = products.objects.all()
    cart_count = orderdetails.objects.filter(customer=request.user , order = None).count()

    like_count = like.objects.filter(liked_product__productid = pk ).count()

    pdtreviews = reviews.objects.filter(reviewed_product__productid = pk).order_by('-reviewed_time').first()


    print('the pdt is ', product)

    context = {
        'product' : product,
        'form' : form,
        'category' : category,
        'related_items' : related,
        'cart_count' : cart_count, 
        'like_count' : like_count,
        'liked' : liked,
        'reviewForm' : reviewform,
        'pdtreviews' : pdtreviews
    }




    return render(request, 'product/producthome.html' , context)


def addtocart(request,pk):

    #first lets create an order to accomodate the products in the order details.. this will be done first time when there is no order with comlete status incomplete exist

    payment_mode = payment.objects.get(paymentid = 1)

    #orderinst,createdorder = orders.objects.get_or_create(customerid = request.user , order_complete = False , defaults={
        #'customerid' : request.user , 'orderdate' : datetime.now() , 'ordernumber' : str(str(request.user) + str(datetime.now())) , 'paymentdate' : datetime.now() , 'paymentid' : payment_mode })

    #print(order , created)

    prod_item = products.objects.get(productid = pk)

    orderdetail,createdorderdetails = orderdetails.objects.get_or_create(product__productid = pk , customer = request.user , order = None , defaults={
        'orderdetailnumber' :  int(str(request.user.id) + str(datetime.now().strftime('%Y%m%d'))) ,  'product' : prod_item, 'price' : prod_item.unit_price , 'quantity' : 1 , 'discount' : 0 , 'date' : datetime.now() 
        })

    if createdorderdetails == False:
        updating_quantity = orderdetail
        updating_quantity.quantity += 1
        updating_quantity.save()

    #print('order detail ie cart ' , orderdetail,createdorderdetails)


    return redirect('cart:home')


def addproduct(request):
    if request.method == "GET":

        request.session['searchtype'] = 'home'
        request.session.modified = True

        if request.user.is_authenticated:
            curruser = request.user
            category = categories.objects.all()


            cart_count = orderdetails.objects.filter(customer=request.user , order = None).count()
            productsform = productsForm()

            context = {

                'curr_user' : curruser,
                'category' : category,
                #'product' : product,
                'cart_count' : cart_count ,
                'productsform' : productsform                
            }
            return render(request,'product/addproducts.html',context)
    
    elif request.method == "POST":

        print(request.POST)
        productinstance = productsForm(request.POST)

        if productinstance.is_valid():
            productinstance2 = productinstance.save(commit = False)

            if 'picture' in request.FILES:
                productinstance2.picture = request.FILES['picture']

            productinstance2.save()

        return redirect('products:addproduct')