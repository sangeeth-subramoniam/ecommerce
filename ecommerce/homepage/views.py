from structure.models import categories, orderdetails
from django.shortcuts import redirect, render
from registration.models import user_profile
from structure.models import categories,products

from django.db.models import Q


from .forms import searchproductform

from django.core.paginator import Paginator

# Create your views here.
def home(request):

    if request.method == "GET":

        request.session['searchtype'] = 'home'
        request.session.modified = True

        if request.user.is_authenticated:
            curruser = request.user
            category = categories.objects.all()
            product = products.objects.all()

            slideimgs = products.objects.filter(discount = 1).order_by('unit_price')

            

            form = searchproductform()


            per_page = 12
            product_paginator = Paginator(product , per_page)
            page_num = request.GET.get('page')
            product_page = product_paginator.get_page(page_num)

            cart_count = orderdetails.objects.filter(customer=request.user , order = None).count()
            

            context = {

                'product' : product_page,
                'per_page' : per_page,
                'pgcount' : product_paginator.num_pages,
                'curr_user' : curruser,
                'category' : category,
                #'product' : product,
                'cart_count' : cart_count ,
                'form' : form,
                'slideimgs' : slideimgs
            }
            return render(request,'landing/homepage.html',context)

        else:

            product = products.objects.all()
            category = categories.objects.all()

            context = {
                'product' : product,
                'category': category,
            }
            return render(request,'landing/not_signed_in.html', context)
    

    elif request.method == "POST":

        search_term = request.POST.get('productname')

        if(search_term is not None):
            request.session['searchtype'] = search_term
            request.session.modified = True


        print('the method is a ' , request.method , 'with parameters ', request.POST , '.... Now redireccting ..')

        if search_term == '':
            print('empty search, so showing homepage!')
            return redirect('homepage:home')
        
        else: #POST 

            if search_term: #POST WITH KEYWORD IN SEARCHBOX searching for a product
                print('ther is search term' , search_term , 'rendering in storesearch page')
                request.session['searchtype'] = search_term
                request.session.modified = True

                category = categories.objects.all()
                product = products.objects.all().filter(Q(productname__icontains = search_term) | Q(category__categoryname__icontains = search_term) )
                print('the requesttype is ', request.method ,' and the search_term is ' , search_term , 'params are ' , request.POST)
                form = searchproductform()
                form.fields["productname"].initial = search_term
                cart_count = orderdetails.objects.filter(customer=request.user , order = None).count()

                context = {
                    'product' : product,
                    'category': category,
                    'form' : form,
                    'cart_count' : cart_count
                }
                return render(request,'landing/storesearch.html',context)


            else: #POST FOR SORTING AND MANIPULATION
                if request.session['searchtype'] == 'home':
                    print(' sort from homepage ')

                    form = searchproductform()

                    manipulate_type = request.POST.get('manipulation_type')
                    print('the manipulation type is ', manipulate_type , 'and it is done in the homepage ')

                    if manipulate_type == 'sort_asc':
                        product = products.objects.all().order_by('unit_price')

                    elif manipulate_type == 'sort_desc':
                        product = products.objects.all().order_by('-unit_price')

                    elif manipulate_type == 'recent':
                        product = products.objects.all().order_by('-created_at')

                    elif manipulate_type == 'most popular':
                        product = products.objects.all().order_by('-likes')
                        print(product)

                    else:
                        product = products.objects.all()
                
                            
                        

                elif request.session['searchtype'] != 'home' and request.session['searchtype'] != 'category' :

                    print('sorting on searched page' , search_term) # , 'session variable is ' ,request.session['searchtype'])

                    manipulate_type = request.POST.get('manipulation_type')
                    search_product = request.session['searchtype']

                    form = searchproductform()
                    form.fields["productname"].initial = search_product

                    print('the manipulation type is ', manipulate_type , 'and it is done in the searchpage ' , request.session['searchtype'])

                    if manipulate_type == 'sort_asc':
                        product = products.objects.all().filter(Q(productname__icontains = search_product) | Q(category__categoryname__icontains = search_product)).order_by('unit_price')
                    
                    elif manipulate_type == 'sort_desc':
                        product = products.objects.all().filter(Q(productname__icontains = search_product) | Q(category__categoryname__icontains = search_product)).order_by('-unit_price')

                    elif manipulate_type == 'recent':
                        product = products.objects.all().filter(Q(productname__icontains = search_product) | Q(category__categoryname__icontains = search_product)).order_by('-created_at')

                    elif manipulate_type == 'most popular':
                        print('enter')
                        product = products.objects.all().filter(Q(productname__icontains = search_product) | Q(category__categoryname__icontains = search_product)).order_by('-likes')
                        print('over')
                    else:
                        print('enter2')
                        product = products.objects.all()
            
            cart_count = orderdetails.objects.filter(customer=request.user , order = None).count()

            category = categories.objects.all()
            context = {
            'product' : product,
            'category': category,
            'form' : form,
            'cart_count' : cart_count
            }
            return render(request,'landing/storesearch.html',context)


        


def profile(request):
    userdetails = user_profile.objects.get(user = request.user)
    context = {
        'pp' : userdetails,
        'curr_user' : request.user
    }
    return render(request,'landing/profile.html' , context)

def about(request):
    return render(request,'landing/about.html')

def category(request,pk):

    if request.method == "GET":
        cat = categories.objects.get(categoryid = pk)
        print(cat)

        request.session['searchtype'] = 'category'
        request.session.modified = True

        if request.user.is_authenticated:
            curruser = request.user
            category = categories.objects.all()
            product = products.objects.filter(category__categoryid = cat.categoryid)

            form = searchproductform()
            form.fields['productname'].initial = cat.categoryname
            cart_count = orderdetails.objects.filter(customer=request.user , order = None).count()

            context = {
                'curr_user' : curruser,
                'category' : category,
                'product' : product,
                'form' : form,
                'cart_count' : cart_count
            }
            return render(request,'landing/category.html',context)

        else:
            product = products.objects.all()
            category = categories.objects.all()
            cart_count = orderdetails.objects.filter(customer=request.user , order = None).count()

            context = {
                'product' : product,
                'category': category,
                'cart_count' : cart_count
            }
            return render(request,'landing/not_signed_in.html', context)

    else:
        print('post in category and pk' , request.session['searchtype'] , pk)

        cat = categories.objects.get(categoryid = pk)
        print(cat)

        request.session['searchtype'] = 'category'
        request.session.modified = True

        if request.session['searchtype'] == 'category':
            print('sort from categoty page ')

            form = searchproductform()
            form.fields['productname'].initial = cat.categoryname

            manipulate_type = request.POST.get('manipulation_type')
            print('the manipulation type is ', manipulate_type , 'and it is done in the homepage ')

            if manipulate_type == 'sort_asc':
                product = products.objects.all().filter(category__categoryid = cat.categoryid).order_by('unit_price')

            elif manipulate_type == 'sort_desc':
                product = products.objects.all().filter(category__categoryid = cat.categoryid).order_by('-unit_price')

            elif manipulate_type == 'recent':
                product = products.objects.all().filter(category__categoryid = cat.categoryid).order_by('-created_at')

            elif manipulate_type == 'most popular':
                print('ttt')
                product = products.objects.all().filter(category__categoryid = cat.categoryid).order_by('-likes')

        else:
            product = products.objects.all()

        category = categories.objects.all()

        cart_count = orderdetails.objects.filter(customer=request.user , order = None).count()

        context = {
            'product' : product,
            'category': category,
            'form' : form,
            'cart_count' : cart_count
        }
        return render(request,'landing/category.html',context)

    
def updateprofile(request , pk):
    return redirect('homepage:home')