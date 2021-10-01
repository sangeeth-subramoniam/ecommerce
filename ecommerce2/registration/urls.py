from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'registration'
urlpatterns = [
    path('signup', views.signup , name = "signup"),
    path('signin', views.signin , name = "signin"),
    path('signout', views.signout , name = "signout"),
    path('changepassword1', views.change_password1, name='change_password1'),
    path('changepassword2', views.change_password2, name='change_password2'),
    path('user_profile_update', views.user_profile_update, name='user_profile_update'),
    path('user_profile_picture_update', views.user_profile_picture_update, name='user_profile_picture_update'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

