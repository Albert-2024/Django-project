from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth import login as auth_login ,authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from .forms import ProductForm,SpecificationForm

from django.contrib  import messages,auth
# from .models import Brand, Category, CustomUser, Product
from .models import CustomUser, Product, ProductHeadset, ProductLap, ProductMobile, ProductSpeaker
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

def addlaptop(request):
    user = request.user
    userid = user.id
    if request.method == 'POST':
        # Create a new Category instance and assign values
        newproduct = ProductLap(
        screensize = request.POST.get('screen_size'),
        storage = request.POST.get('storage'),
        processor = request.POST.get('processor'),
        ram = request.POST.get('ram'),
        os = request.POST.get('os'),
        graphics = request.POST.get('graphics'),
        color = request.POST.get('color'),
        user_id=userid
        
        )
        
        newproduct.save()   
        
        return redirect("/")
    return render(request,'addproduct/laptop.html')

def addmobile(request):
    user = request.user
    userid = user.id
    if request.method == 'POST':
        # Create a new Category instance and assign values
        newproduct = ProductMobile(
            wireless=request.POST.get('wireless'),
            m_os=request.POST.get('m_os'),
            cellular=request.POST.get('cellular'),
            memory=request.POST.get('memory'),
            connectivity=request.POST.get('connectivity'),
            m_screen=request.POST.get('m_screen'),
            wireless_network_technology=request.POST.get('wireless_network_technology'),
            color=request.POST.get('color'),
            ram=request.POST.get('ram'),
            processor=request.POST.get('processor'),
            camrear=request.POST.get('camrear'),
            camfront=request.POST.get('camfront'),
            user_id=userid
        )
        
        newproduct.save()   
        
        return redirect("/")
    return render(request, 'addproduct/mobile.html')

def addheadset(request):
    user = request.user
    userid = user.id
    if request.method == 'POST':
        # Create a new Category instance and assign values
        newproduct = ProductHeadset(
        battery = request.POST.get('battery'),
        color = request.POST.get('color'),
        form_factor = request.POST.get('form_factor'),
        h_connectivity = request.POST.get('h_connectivity'),
        weight = request.POST.get('weight'),
        charging = request.POST.get('charging'),
        working = request.POST.get('working'),
        user_id=userid
        
        )
        
        newproduct.save()   
        
        return redirect("/")
    return render(request,'addproduct/headset.html')

def addspeaker(request):
    user = request.user
    userid = user.id
    if request.method == 'POST':
        # Create a new Category instance and assign values
        newproduct = ProductSpeaker(
        battery = request.POST.get('battery'),
        s_connectivity = request.POST.get('s_connectivity'),
        s_type = request.POST.get('s_type'),
        special_features = request.POST.get('special_features'),
        weight = request.POST.get('weight'),
        charging = request.POST.get('charging'),
        working = request.POST.get('working'),
        user_id=userid
        
        )
        
        newproduct.save()   
        
        return redirect("/")
    return render(request,'addproduct/speaker.html')

def mobile_list(request):
    data = ProductMobile.objects.all()
    user= request.user
    return render(request,'products/mobile.html',{'data':data})

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
    products = ProductHeadset.objects.filter(id=product_id)
    return render(request,'details/headset.html',{'product':products})

def speaker_details(request,product_id):
    product = ProductSpeaker.objects.filter(id=product_id)
    return render(request,'details/speaker.html',{'product':product})

def laptop_details(request,product_id):
    product = ProductLap.objects.filter(id=product_id)
    return render(request,'details/laptop.html',{'product':product})

def mobile_details(request,product_id):
    product = ProductMobile.objects.filter(id=product_id)
    return render(request,'details/mobile.html',{'product':product})

def sellerDashboard(request):
    
    return render(request,'sellerDashboard.html')

def product_form(request):
    return render(request,'product_form.html')

