from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth import login as auth_login ,authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from .forms import ProductForm,SpecificationForm

from django.contrib  import messages,auth
# from .models import Brand, Category, CustomUser, Product
from .models import CustomUser, Product, ProductHeadset, ProductLap, ProductMobile, ProductSpeaker,Cart
# from accounts.backends import EmailBackend
from django.contrib.auth import get_user_model
#from .forms import UserForm, ServiceForm 

User = get_user_model()

# Create your views here.

def register(request):
    if request.method == 'POST':
        name1 = request.POST.get('name', None)
        email = request.POST.get('email', None)
        password = request.POST.get('pass', None)
        role = 1
        print(email)

        if name1 and email and role and password:
            if User.objects.filter(email=email).exists():
                error_message = "Email is already registered."
                return render(request, 'register.html', {'error_message': error_message})
            
            else:
                user = User(name=name1, email=email, role=role)
                user.set_password(password)  # Set the password securely
                user.save()
                return redirect('login')  
            
    return render(request, 'register.html')

def userlogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pass')
        print(email,password)

        if email and password:
            user = authenticate(request, email=email, password=password)
            print(user)
            if user is not None:
                auth_login(request, user) 
                print(user)
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
    

def sellerreg(request):
    user=request.user
    if user.role==2:
        return redirect('sellerDashboard')
    else:
        if request.method == 'POST':
            user.role = 2
            user.save()
            return redirect('sellerDashboard')
                
        return render(request, 'sellerreg.html')

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
    print("laptop")
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
    print("speaker")
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
        # Create a new Category instance and assign values
        print(laptop)
        laptop.screen_size = request.POST.get('screen_size')
        laptop.storage = request.POST.get('storage')
        laptop.processor = request.POST.get('processor')
        laptop.ram = request.POST.get('ram')
        laptop.os = request.POST.get('os')
        laptop.graphics = request.POST.get('graphics')
        laptop.color = request.POST.get('color')
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

def cart(request):
    product = Cart.objects.filter(user_id=request.user.id)
    return render(request,'cart.html',{'product':product})


def addtocart(request,product_id):
    print(product_id)
    product = get_object_or_404(Product, id=product_id)
    print(product)
    cart_item, created = Cart.objects.get_or_create(product_id=product_id,user_id = request.user.id)
   
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')
