from django.contrib import admin
from .models import payment,orders,suppliers

# Register your models here.
admin.site.register(payment)
admin.site.register(orders)
admin.site.register(suppliers)
