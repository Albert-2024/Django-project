from django.contrib import admin
from django.urls import path
from app2 import views
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register',views.register,name='register'),
    path('login/',views.userlogin,name="login"),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
     path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
     path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
     path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    # path('/seller/register',views.sellerReg,name='SellerReg'),
    # path('seller/login/',views.login,name="login"),
    # path('/delivery/register',views.sellerReg,name='deliveryReg'),
    # path('delivery/login/',views.login,name="deliverylogin"), 
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
