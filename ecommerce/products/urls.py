from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'products'
urlpatterns = [
    path('<pk>', views.home , name = "home"),

    #path('options/<str:pk>',views.options, name = 'options'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)