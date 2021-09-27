from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'orders'
urlpatterns = [
    path('', views.myorders , name = "myorders"),
    path('orderdetails/<pk>', views.orderdetail , name = "orderdetail"),
    path('createorder/', views.createorder , name = "createorder"),
    path('instantorder/', views.instantorder , name = "instantorder"),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
