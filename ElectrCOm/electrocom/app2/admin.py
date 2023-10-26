from django.contrib import admin
from .models import ProductMobile,ProductLap,ProductSpeaker,ProductHeadset, Product, Profile,SellerProfile,sellerRegistrationRequest

# Register your models here.

from .models import CustomUser
admin.site.register(CustomUser)

admin.site.register(ProductHeadset)
admin.site.register(ProductLap)
admin.site.register(ProductMobile)
admin.site.register(ProductSpeaker)
admin.site.register(Product)
admin.site.register(Profile)
admin.site.register(SellerProfile)
admin.site.register(sellerRegistrationRequest)




