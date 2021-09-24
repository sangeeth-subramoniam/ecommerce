from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'homepage'
urlpatterns = [
    path('', views.home , name = "home"),
    path('profile', views.profile , name = "profile"),
    path('about', views.about , name = "about"),
    path('categories/<pk>', views.category , name = "category"),
    path('updateprofile/<pk>', views.updateprofile , name = "updateprofile"),

    #path('options/<str:pk>',views.options, name = 'options'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
