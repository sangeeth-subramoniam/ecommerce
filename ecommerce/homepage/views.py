from structure.models import categories
from django.shortcuts import render
from registration.models import user_profile
from structure.models import categories,products


from .forms import searchproductform

# Create your views here.
def home(request):

    if request.method == "GET":
        if request.user.is_authenticated:
            curruser = request.user
            category = categories.objects.all()
            product = products.objects.all()

            form = searchproductform()

            context = {
                'curr_user' : curruser,
                'category' : category,
                'product' : product,
                'form' : form
            }
            return render(request,'landing/homepage.html',context)

        else:

            product = products.objects.all()
            category = categories.objects.all()

            context = {
                'product' : product,
                'category': category
            }
            return render(request,'landing/not_signed_in.html', context)
    else:
        search_term = request.POST.get('productname')
        category = categories.objects.all()
        if search_term:
            product = products.objects.all().filter(productname = search_term)
        else:
            product = products.objects.all()
        print('the requesttype is ', request.method ,' and the search_term is ' , search_term)
        form = searchproductform()

        context = {
            'product' : product,
            'category': category,
            'form' : form
        }
        return render(request,'landing/homepage.html',context)


def contact(request):
    return render(request,'landing/contact.html')

def about(request):
    return render(request,'landing/about.html')