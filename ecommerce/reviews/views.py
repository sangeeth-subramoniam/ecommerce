from django.shortcuts import render, redirect
from structure.models import categories, products, reviews
from .forms import reviewForm
from homepage.forms import searchproductform
# Create your views here.
def review(request,pk):
    
    if request.method == "POST":
        print(request.POST)

        reviewinstance = reviewForm(request.POST)
        if(reviewinstance.is_valid()):
            instance = reviewinstance.save(commit=False)
            instance.reviewed_by = request.user
            instance.reviewed_product = products.objects.get(productid = pk)
            instance.stars = request.POST['rating']
            instance.save()

        return redirect('products:home', pk)

    if request.method == "GET":

        print('Fetching all reviews !')

        review = reviews.objects.filter(reviewed_product__productid = pk).order_by('-reviewed_time')
        category = categories.objects.all()
        form = searchproductform()

        context = {
            'review' : review,
            'category' : category,
            'form' : form
        }

        return render(request, 'reviews/reviewpage.html' , context)

def delete_review(request, pk):
    
    review_instance = reviews.objects.get(reviewid = pk)

    redirect_page = review_instance.reviewed_product.productid

    if review_instance.reviewed_by == request.user:
        review_instance.delete()

    return redirect('products:home' , redirect_page )

    