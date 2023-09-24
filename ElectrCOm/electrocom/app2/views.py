from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth import login as auth_login ,authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from .forms import ProductForm,SpecificationForm

from django.contrib  import messages,auth
# from .models import Brand, Category, CustomUser, Product
from .models import CustomUser, ProductMobile,ProductLap, ProductHeadset, ProductSpeaker
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
        role = User.CUSTOMER
        print(email)

        if name1 and email and role and password:
            if User.objects.filter(email=email).exists():
                error_message = "Email is already registered."
                return render(request, 'login.html', {'error_message': error_message})
            
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

        if email and password:
            user = authenticate(request, email=email, password=password)
            if user is not None:
                auth_login(request, user) 
                if user.role == CustomUser.SELLER:       
                    return redirect('sellerindex')
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
    if request.method == 'POST':
        name1 = request.POST.get('name', None)
        email = request.POST.get('email', None)
        password = request.POST.get('pass', None)
        role = User.SELLER
        print(email)

        if name1 and email and role and password:
            if User.objects.filter(email=email).exists():
                error_message = "Email is already registered."
                return render(request, 'login.html', {'error_message': error_message})
            
            else:
                user = User(name=name1, email=email, role=role)
                user.set_password(password)  # Set the password securely
                user.save()
                return redirect('login')  
            
    return render(request, 'sellerreg.html')

def sellerindex(request):
    return render(request,'sellerindex.html')



def addmobile(request):
    user = request.user
    userid = user.id
    if request.method == 'POST':
        # Create a new Category instance and assign values
        newproduct = ProductMobile(
        brand_name = request.POST.get('brand_name'),
        product_name = request.POST.get('product_name'),
        color = request.POST.get('color'),
        ram = request.POST.get('ram'),
        processor = request.POST.get('processor'),
        storage = request.POST.get('storage'),
        camrear = request.POST.get('camrear'),
        camfront = request.POST.get('camfront'),
        price = request.POST.get('price'),
        warranty = request.POST.get('warranty'),
        description = request.POST.get('description'),
        display = request.POST.get('display'), 
        quantity = request.POST.get('quantity'),
        product_images1 = request.FILES.get('product_images1'),
        product_images2 = request.FILES.get('product_images2'),
        product_images3 = request.FILES.get('product_images3'),
        product_images4 = request.FILES.get('product_images4'),
        user_id=userid
        
        )
        
        newproduct.save()   
        
        return redirect("/")
    return render(request,'addproduct/mobile.html')

def addlaptop(request):
    user = request.user
    userid = user.id
    if request.method == 'POST':
        # Create a new Category instance and assign values
        newproduct = ProductLap(
        brand_name = request.POST.get('brand_name'),
        product_name = request.POST.get('product_name'),
        color = request.POST.get('color'),
        ram = request.POST.get('ram'),
        processor = request.POST.get('processor'),
        storage = request.POST.get('storage'),
        price = request.POST.get('price'),
        warranty = request.POST.get('warranty'),
        description = request.POST.get('description'),
        quantity = request.POST.get('quantity'),
        product_images1 = request.FILES.get('product_images1'),
        product_images2 = request.FILES.get('product_images2'),
        product_images3 = request.FILES.get('product_images3'),
        product_images4 = request.FILES.get('product_images4'),
        user_id=userid
        
        )
        
        newproduct.save()   
        
        return redirect("/")
    return render(request,'addproduct/laptop.html')

def addheadset(request):
    user = request.user
    userid = user.id
    if request.method == 'POST':
        # Create a new Category instance and assign values
        newproduct = ProductHeadset(
        brand_name = request.POST.get('brand_name'),
        product_name = request.POST.get('product_name'),
        battery = request.POST.get('battery'),
        description = request.POST.get('description'),
        price = request.POST.get('price'),
        color = request.POST.get('color'),
        quantity = request.POST.get('quantity'),
        product_images1 = request.FILES.get('product_images1'),
        product_images2 = request.FILES.get('product_images2'),
        product_images3 = request.FILES.get('product_images3'),
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
        brand_name = request.POST.get('brand_name'),
        product_name = request.POST.get('product_name'),
        battery = request.POST.get('battery'),
        quality = request.POST.get('quality'),
        size = request.POST.get('size'),
        description = request.POST.get('description'),
        price = request.POST.get('price'),
        quantity = request.POST.get('quantity'),
        product_images1 = request.FILES.get('product_images1'),
        product_images2 = request.FILES.get('product_images2'),
        product_images3 = request.FILES.get('product_images3'),
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

def cart(request):
    return render(request,'cart.html')

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