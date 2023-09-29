from django.contrib import admin
# from app2 import views
from django.conf import settings
# from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
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
    path('sellerindex/',views.sellerindex,name='sellerindex'),
    path('userLogout/',views.userLogout,name='userLogout'),
    path('addlaptop/<int:product_id>/',views.addlaptop,name='addlaptop'),
    path('addmobile/<int:product_id>',views.addmobile,name='addmobile'),
    path('addheadset/<int:product_id>',views.addheadset,name='addheadset'),
    path('addspeaker/<int:product_id>',views.addspeaker,name='addspeaker'),
    path('headset/<int:product_id>/', views.headset_details, name='headset_details'),
    path('speaker/<int:product_id>/', views.speaker_details, name='speaker_details'),
    path('laptop/<int:product_id>/', views.laptop_details, name='laptop_details'),
    path('mobile/<int:product_id>/', views.mobile_details, name='mobile_details'),
    path('',views.sellerDashboard,name='sellerDashboard'),
    path('product_form/',views.product_form,name='product_form'),
    path('regheadset/',views.regheadset,name='regheadset'),
    path('regmobile/',views.regmobile,name='regmobile'),
    path('reglaptop/',views.reglaptop,name='reglaptop'),
    path('regspeaker/',views.regspeaker,name='regspeaker'),
    path('viewHeadset/',views.viewHeadset,name='viewHeadset'),
    path('viewSpeaker/',views.viewSpeaker,name='viewSpeaker'),
    path('viewMobile/',views.viewMobile,name='viewMobile'),
    path('viewLaptop/',views.viewLaptop,name='viewLaptop'),
    path('cart/', views.cart, name='cart'),
    path('addtocart/<int:product_id>', views.addtocart, name='addtocart'),
    path('allproducts/',views.allproducts,name='allproducts'),
    # path('cart/',views.cart,name='cart'),
    # path('<str:category>/<int:product_id>/add_to_cart/', views.add_to_cart, name='add_to_cart'),
    
    path('seller/login/',views.sellerlogin,name="sellerlogin"),
    # path('/delivery/register',views.sellerReg,name='deliveryReg'),
    # path('delivery/login/',views.login,name="deliverylogin"), 
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

