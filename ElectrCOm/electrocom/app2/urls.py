from django.contrib import admin
from django.urls import path
# from app2 import views
from django.conf import settings
# from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.userlogin,name="login"),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('sellerreg/',views.sellerreg,name='sellerreg'),
    path('mobile/',views.mobile_list,name='mobile'),
    path('laptop/',views.laptop_list,name='laptop'),
    path('headset/',views.headset_list,name='headset'),
    path('speaker/',views.speaker_list,name='speaker'),
    path('cart/',views.cart,name='cart'),
    # path('create_product/',views.create_product,name='create_product'),
    path('sellerindex/',views.sellerindex,name='sellerindex'),
    path('userLogout/',views.userLogout,name='userLogout'),
    path('addmobile/',views.addmobile,name='addmobile')
    # path('addproduct/',views.create_product,name='addproduct')
    # path('seller/login/',views.login,name="login"),
    # path('/delivery/register',views.sellerReg,name='deliveryReg'),
    # path('delivery/login/',views.login,name="deliverylogin"), 
]

