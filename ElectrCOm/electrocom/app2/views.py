from decimal import Decimal
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth import login as auth_login ,authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
# from .forms import ProductForm,SpecificationForm

from django.contrib  import messages,auth
# from .models import Brand, Category, CustomUser, Product
from .models import CustomUser, Product, ProductHeadset, ProductLap, ProductMobile, ProductSpeaker,Cart, Wishlist,Profile,SellerProfile
# from accounts.backends import EmailBackend
from django.contrib.auth import get_user_model
#from .forms import UserForm, ServiceForm 

User = get_user_model()

# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', None)
        last_name = request.POST.get('last_name', None)
        email = request.POST.get('email', None)
        password = request.POST.get('pass', None)
        role = 1
        print(email)

        if first_name and last_name and email and role and password:
            if User.objects.filter(email=email).exists():
                error_message = "Email is already registered."
                return render(request, 'register.html', {'error_message': error_message})
            
            else:
                user = User(first_name = first_name, last_name=last_name, email=email, role=role)
                # profile = Profile(user=user)
                user.set_password(password)  # Set the password securely
                user.save()
                # profile.save()
                return redirect('login')  
            
    return render(request, 'register.html')

def userlogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pass')
       

        if not email or not password:
            error_message = "please provide details to login in"
            return render(request, 'login.html', {'error_message': error_message})
        
        user = authenticate(request, email=email, password=password)
            
        if user is not None:
            auth_login(request, user) 
            if user.role == 2:       
                return redirect('sellerDashboard')
            else:
                return redirect('/')
        else:
                error_message = "Invalid login credentials."
                return render(request, 'login.html', {'error_message': error_message})
            
    return render(request,'login.html')

def userLogout(request):
    auth.logout(request)
    request.session.pop('is_logged_in',None)
    return redirect('/') 
    
# def profile(request):
#     # def seller_profile(request):
#     user=User.objects.filter(id=request.user.id)
#     userexists=Profile.objects.filter(user_id=request.user.id).exists()
#     if userexists:
#         seller=Profile.objects.filter(user_id=request.user.id)
#     else:
#         seller=None
#         # print(seller)
#     if request.method=='POST':
#         phone=request.POST.get('seller-number')
#         userdata1=UserData.objects.get(user_id=request.user.id)
#         userdata1.number=phone
#         userdata1.save()
#         if userexists:
#             seller1=SellerProfile.objects.get(user_id=request.user.id)
#             seller1.district=request.POST.get('seller-district')
#             seller1.state=request.POST.get('seller-state')
#             seller1.country=request.POST.get('seller-country')
#             seller1.address=request.POST.get('seller-address')
#             seller1.pincode=request.POST.get('seller-pincode')
#             image=request.FILES.get('seller-image')
#             if image==None:
#                 seller1.image=seller1.image
#             else:
#                 seller1.image=image
#             seller1.save()
#             return redirect('seller_profile')
#         else:
#             user1=SellerProfile(
#             district=request.POST.get('seller-district'),
#             state=request.POST.get('seller-state'),
#             country=request.POST.get('seller-country'),
#             address=request.POST.get('seller-address'),
#             pincode=request.POST.get('seller-pincode'),
#             image=request.FILES.get('seller-image'),
#             user_id=request.user.id,
#             )
#             user1.save()
#             return redirect('profile')
#     return render(request,'profile.html',{'user':user,'seller':seller,'userdata':userdata,})

            
@login_required
def profile(request):
    user = request.user
    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        profile=None
        
    if request.method == "POST":
        if profile is None:
            profile = Profile(user=user)
        profile.district = request.POST.get('district')
        profile.state = request.POST.get('state')
        profile.country = request.POST.get('country')
        profile.address = request.POST.get('address')
        profile.pincode = request.POST.get('pincode')
        
        profile.save()
            
        return redirect('profile')
    
    return render(request,'profile.html',{'user':user,'profile':profile})


def sellerreg(request):
    user=request.user

    if user.role==2:
        
        return redirect('sellerDashboard')
    else:
        if request.method == 'POST':
            
            gst = request.POST.get('gst')
            pan = request.POST.get('pan')
            SellerProfile(
            gst=gst,
            pan=pan,
            user_id=request.user.id
            ).save()
            user.role = 2
            user.save()
            
            return redirect('sellerDashboard')
                
    return render(request, 'sellerreg.html')

def sellerProfile(request):
    user = request.user
    data = SellerProfile.objects.get(user_id=user.id)
    profile = Profile.objects.get(user_id=user.id)
    return render(request,'sellerProfile.html',{'data': data,'profile':profile})

def sellerindex(request):
    return render(request,'sellerindex.html')

def sellerlogin(request): 
    return render(request,'sellerlogin.html')

# new Product

def addProduct(request):
    user = request.user
    userid = user.id
    if request.method == 'POST':
        newproduct = Product(
        user = userid,
        name = request.POST.get('name'),
        brand_name = request.POST.get('brand_name'),
        product_name = request.POST.get('product_name'),
        price = request.POST.get('price'),
        image1 = request.POST.get('image1'),
        image2 = request.POST.get('image2'),
        image3 = request.POST.get('image3'),
        description = request.POST.get('description'),
        stock = request.POST.get('stock'),
        category = request.POST.get('category'),
        
        )
        newproduct.save()
        
        return redirect("/")
    return render(request,'addproduct.html')

def regheadset(request):
    print("headset")
    user = request.user
    userid = user.id
    if request.method == 'POST':
        newproduct = Product(
        user_id = userid,
        name = request.POST.get('name'),
        brand_name = request.POST.get('brandName'),
        product_name = request.POST.get('productName'),
        price = request.POST.get('price'),
        image1 = request.FILES.get('image1'),
        image2 = request.FILES.get('image2'),
        image3 = request.FILES.get('image3'),
        description = request.POST.get('description'),
        stock = request.POST.get('stock'),
        
        category = 'headset'
        
        )
        newproduct.save()
        headset_id=newproduct.id
        headset_obj = ProductHeadset(
            product_id=headset_id,
        )
        headset_obj.save()
        
        return redirect("/")
    return render(request,'product_form.html')

def regmobile(request):
    print("mobile")
    user = request.user
    userid = user.id
    if request.method == 'POST':
        newproduct = Product(
        user_id = userid,
        name = request.POST.get('name'),
        brand_name = request.POST.get('brandName'),
        product_name = request.POST.get('productName'),
        price = request.POST.get('price'),
        image1 = request.FILES.get('image1'),
        image2 = request.FILES.get('image2'),
        image3 = request.FILES.get('image3'),
        description = request.POST.get('description'),
        stock = request.POST.get('stock'),
        category = 'mobile'
        
        )
        newproduct.save()
        mobile_id=newproduct.id
        mobile_obj = ProductMobile(
            product_id=mobile_id,
        )
        mobile_obj.save()
        
        return redirect("/")
    return render(request,'product_form2.html')

def reglaptop(request):
    user = request.user
    userid = user.id
    if request.method == 'POST':
        newproduct = Product(
        user_id = userid,
        name = request.POST.get('name'),
        brand_name = request.POST.get('brandName'),
        product_name = request.POST.get('productName'),
        price = request.POST.get('price'),
        image1 = request.FILES.get('image1'),
        image2 = request.FILES.get('image2'),
        image3 = request.FILES.get('image3'),
        description = request.POST.get('description'),
        stock = request.POST.get('stock'),
        category = 'laptop'
        
        )
        newproduct.save()
        laptop_id=newproduct.id
        laptop_obj = ProductLap(
            product_id=laptop_id,
        )
        laptop_obj.save()
        
        return redirect("/")
    return render(request,'product_form3.html')

def regspeaker(request):
    user = request.user
    userid = user.id
    if request.method == 'POST':
        newproduct = Product(
        user_id = userid,
        name = request.POST.get('name'),
        brand_name = request.POST.get('brandName'),
        product_name = request.POST.get('productName'),
        price = request.POST.get('price'),
        image1 = request.FILES.get('image1'),
        image2 = request.FILES.get('image2'),
        image3 = request.FILES.get('image3'),
        description = request.POST.get('description'),
        stock = request.POST.get('stock'),
        category = 'speaker'
        
        )
        newproduct.save()
        speaker_id=newproduct.id
        speaker_obj = ProductSpeaker(
            product_id=speaker_id,
        )
        speaker_obj.save()
        
        return redirect("/")
    return render(request,'product_form4.html')

def addlaptop(request,product_id):
    user = request.user
    userid = user.id
    laptop = ProductLap.objects.get(product_id=product_id)
    if request.method == 'POST':
        print(laptop)
        laptop.screen_size = request.POST.get('screen_size')
        laptop.storage = request.POST.get('storage')
        laptop.processor = request.POST.get('processor')
        laptop.ram = request.POST.get('ram')
        laptop.os = request.POST.get('os')
        laptop.graphics = request.POST.get('graphics')
        laptop.color = request.POST.get('color')
        laptop.stock = request.POST.get('stock')
        print(laptop)
        laptop.save()   
        
        return redirect("/")
    return render(request,'addproduct/laptop.html',{'laptop':laptop})

def addmobile(request,product_id):
    user = request.user
    userid = user.id
    mobile = ProductMobile.objects.get(product_id=product_id)
    if request.method == 'POST':
        print(mobile)
        # Create a new Category instance and assign values
        mobile.wireless=request.POST.get('wireless')
        mobile.m_os=request.POST.get('m_os')
        mobile.cellular=request.POST.get('cellular')
        mobile.memory=request.POST.get('memory')
        mobile.connectivity=request.POST.get('connectivity')
        mobile.m_screen=request.POST.get('m_screen')
        mobile.wireless_network_technology=request.POST.get('wireless_network_technology')
        mobile.color=request.POST.get('color')
        mobile.ram=request.POST.get('ram')
        mobile.processor=request.POST.get('processor')
        mobile.camrear=request.POST.get('camrear')
        mobile.camfront=request.POST.get('camfront')
        mobile.stock = request.POST.get('stock')
        
        print(mobile)
        mobile.save()  
        
        return redirect("/")
    return render(request, 'addproduct/mobile.html',{'mobile':mobile})

def addheadset(request,product_id):
    user = request.user
    userid = user.id
    head=ProductHeadset.objects.get(product_id=product_id)
    if request.method == 'POST':
        
        print(head)
        
        head.battery = request.POST.get('battery')
        head.color = request.POST.get('color')
        head.form_factor = request.POST.get('form_factor')
        head.h_connectivity = request.POST.get('h_connectivity')
        head.weight = request.POST.get('weight')
        head.charging = request.POST.get('charging')
        head.working = request.POST.get('working')
        head.stock = request.POST.get('stock')
        
        print(head)
        head.save()   
        
        return redirect("/")
    return render(request,'addproduct/headset.html',{'head':head})

def addspeaker(request,product_id):
    user = request.user
    userid = user.id
    speaker=ProductSpeaker.objects.get(product_id=product_id)
    if request.method == 'POST':
        print(speaker)
        # Create a new Category instance and assign values
        speaker.battery = request.POST.get('battery')
        speaker.s_connectivity = request.POST.get('s_connectivity')
        speaker.s_type = request.POST.get('s_type')
        speaker.special_features = request.POST.get('special_features')
        speaker.weight = request.POST.get('weight')
        speaker.charging = request.POST.get('charging')
        speaker.working = request.POST.get('working')
        
        print(speaker)
        speaker.save()   
        
        return redirect("/")
    return render(request,'addproduct/speaker.html',{'speaker':speaker})

def mobile_list(request):
    data = ProductMobile.objects.all()
    user= request.user
    return render(request,'products/mobile.html',{'data':data})


def viewHeadset(request):
    data = Product.objects.filter(user_id=request.user.id,category='headset')
    user= request.user
    return render(request,'products/headset.html',{'data':data})

def viewSpeaker(request):
    data = Product.objects.filter(user_id=request.user.id,category='speaker')
    user= request.user
    return render(request,'products/speaker.html',{'data':data})

def viewMobile(request):
    data = Product.objects.filter(user_id=request.user.id,category='mobile')
    user= request.user
    return render(request,'products/mobile.html',{'data':data})

def viewLaptop(request):
    data=Product.objects.filter(user_id=request.user.id,category='laptop')
    user = request.user
    return render(request,'products/laptop.html',{'data':data})

def laptop_list(request):
    data=ProductLap.objects.all()
    user = request.user
    return render(request,'products/laptop.html',{'data':data})

def headset_list(request):
    data = ProductHeadset.objects.all()
    user = request.user
    return render(request,'products/headset.html',{'data':data})

def speaker_list(request):
    data = ProductSpeaker.objects.all()
    user = request.user
    return render(request,'products/speaker.html',{'data':data})


def headset_details(request,product_id):
    products = Product.objects.filter(id=product_id)
    headset = ProductHeadset.objects.get(product_id=product_id)
    return render(request,'details/headset.html',{'product':products,'headset':headset})

def speaker_details(request,product_id):
    product = Product.objects.filter(id=product_id)
    speaker = ProductSpeaker.objects.get(product_id=product_id)
    return render(request,'details/speaker.html',{'product':product,'speaker':speaker})

def laptop_details(request,product_id):
    product = Product.objects.filter(id=product_id)
    laptop = ProductLap.objects.get(product_id=product_id)
    return render(request,'details/laptop.html',{'product':product,'laptop':laptop})

def mobile_details(request,product_id):
    product = Product.objects.filter(id=product_id)
    mobile = ProductMobile.objects.get(product_id=product_id)
    return render(request,'details/mobile.html',{'product':product,'mobile':mobile})

def sellerDashboard(request):  
    return render(request,'sellerDashboard.html')

def product_form(request):
    return render(request,'product_form.html')

def allproducts(request):
    data = Product.objects.all()
    return render(request,'products/allproducts.html',{'data': data})

def product_details(request,product_id):
    product = get_object_or_404(Product, id=product_id)
    specific_product = None
    if product.category == 'mobile':
        specific_product = get_object_or_404(ProductMobile, product=product)
        # return render(request, 'details/mobile.html', {'product': product, 'specific_product': specific_product})
    elif product.category == 'headset':
        specific_product = get_object_or_404(ProductHeadset, product=product)
        # return render(request, 'details/mobile.html', {'product': product, 'specific_product': specific_product})
    elif product.category == 'speaker':
        specific_product = get_object_or_404(ProductSpeaker, product=product)
        # return render(request, 'details/mobile.html', {'product': product, 'specific_product': specific_product})
    elif product.category == 'laptop':
        specific_product = get_object_or_404(ProductLap, product=product)
        # return render(request, 'details/mobile.html', {'product': product, 'specific_product': specific_product})    
    else:
        specific_product = None
    return render(request, 'details/allproducts.html', {'product': product, 'specific_product': specific_product})

def addtowishlist(request,product_id):
    product = get_object_or_404(Product, id=product_id)
    wish_item, created = Wishlist.objects.get_or_create(product_id=product_id,user_id = request.user.id)
   
    if not created:
        wish_item.quantity += 1
        wish_item.save()
    else:
        wish_item.price = product.price
        wish_item.save()
    return redirect('wishlist')

def removewishlist(request,product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist_item = get_object_or_404(Wishlist, product=product, user=request.user)
    wishlist_item.delete()
    
    return redirect('wishlist')

def wishlist(request):
    wish = Wishlist.objects.filter(user_id=request.user.id)
    is_empty = not wish.exists()
    print(wish)
    if is_empty:
        messages.warning(request, f"Your wishlist is empty.")
    return render(request,'wishlist.html',{'wish':wish,'is_empty':is_empty})



def cart(request):
    product = Cart.objects.filter(user_id=request.user.id)
    sub_total = sum([item.price * item.quantity for item in product])
    total_price = sub_total
    is_empty = not product.exists()
    # cartstock = Cart.objects.filter(user_id=request.user.id)
    if is_empty:
        messages.warning(request, f"Your cart is empty.")
    return render(request,'cart.html',{'product':product,'total_price':total_price,'sub_total':sub_total,'is_empty':is_empty})

   
def addtocart(request,product_id):
    product = get_object_or_404(Product, id=product_id)
    print(product)
    cart_item, created = Cart.objects.get_or_create(product_id=product_id,user_id = request.user.id)
   
    if created:
        cart_item.price = product.price
        cart_item.save()
        
    return redirect('cart')


def delete_cart(request,product_id):
    remove = Cart.objects.filter(id=product_id)
    remove.delete()
    return redirect('cart')


def increase_item(request, item_id):
    try:
        cart_item = Cart.objects.get(id=item_id)

        if cart_item.product.stock > 0:
            cart_item.quantity += 1
            cart_item.save()

            # Decrease stock in Product model
            cart_item.product.stock -= 1
            cart_item.product.save()
        else:
            messages.warning(request, f"{cart_item.product.product_name} is out of stock.")
    except Cart.DoesNotExist:
        pass

    return redirect('cart')

def decrease_item(request, item_id):
    try:
        cart_item = Cart.objects.get(id=item_id)

        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()

            cart_item.product.stock += 1
            cart_item.product.save()
        else:
            messages.warning(request, f"{cart_item.product.product_name} cannot be removed.")
    except Cart.DoesNotExist:
        pass

    return redirect('cart')

razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
 
 
def payment(request):
    product = Cart.objects.filter(user_id=request.user.id)
    currency = 'INR'
    sub_total = sum([item.price * item.quantity for item in product])
    total_price = Decimal(sub_total)
    amount = int(total_price * 100) 
    
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                       currency=currency,
                                                       payment_capture='0'))
 
    razorpay_order_id = razorpay_order['id']
    from django.urls import reverse


    callback_url = reverse('paymenthandler')
 
    
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['total_price'] = total_price
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url
 
    return render(request, 'payment.html', context=context)
 
 

@csrf_exempt
def paymenthandler(request):
    print("paymenthandler")
   
    if request.method == "POST":

        
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
 
          
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            if result is not None:
                 razorpay_order = razorpay_client.order.fetch(razorpay_order_id)
                 authorized_amount = razorpay_order['amount']

           
                 razorpay_client.payment.capture(payment_id, authorized_amount)

                   
                 return redirect('http://127.0.0.1:8000/')
                
            else:
 
                
                return render(request, 'paymentfail.html')
    else:
       
        return HttpResponseBadRequest()