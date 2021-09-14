from django.contrib import admin
from .models import payment,orders,suppliers,orderdetails,products,categories

# Register your models here.
admin.site.register(payment)
admin.site.register(orders)
admin.site.register(suppliers)
admin.site.register(orderdetails)
admin.site.register(products)
admin.site.register(categories)
