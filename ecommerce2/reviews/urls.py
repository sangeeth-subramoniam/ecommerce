from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'reviews'
urlpatterns = [
    path('review/<pk>', views.review , name = "review"),
    path('deletereview/<pk>', views.delete_review, name = "delete_review"),
    
    #path('options/<str:pk>',views.options, name = 'options'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
