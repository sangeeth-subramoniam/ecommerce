from django.contrib import admin
from .models import payment,orders,suppliers,orderdetails,products,categories,like,reviews

# Register your models here.
admin.site.register(payment)
admin.site.register(orders)
admin.site.register(suppliers)
admin.site.register(orderdetails)
admin.site.register(products)
admin.site.register(categories)
admin.site.register(like)
admin.site.register(reviews)
