from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth import login as auth_login ,authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from .forms import ProductForm,SpecificationForm

from django.contrib  import messages,auth
# from .models import Brand, Category, CustomUser, Product
from .models import CustomUser, ProductMobile
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

def mobile_list(request):
    data = ProductMobile.objects.all()
    # products= Product.objects.all()
    user= request.user
    return render(request,'products/mobile.html',{'data':data})

def laptop_list(request):
    return render(request,'products/laptop.html')

def headset_list(request):
    return render(request,'products/headset.html')

def speaker_list(request):
    return render(request,'products/speaker.html')

def cart(request):
    return render(request,'cart.html')

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

""" def create_product(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        specification_form=SpecificationForm(request.POST)
        if product_form.is_valid() and specification_form.is_valid():
            product = product_form.save()
            specification = specification_form.save(commit=False)
            specification.product = product
            specification.save()
            return redirect('seller_dashboard')
        else:
            product_form = ProductForm()
            specification_form = SpecificationForm()
        
        brands = Brand.objects.all()
        categories = Category.objects.all()
        
        return render(request,'add_product.html',{
            'product_form': product_form,
            'specification_form': specification_form,
            'brands': brands,
            'categories': categories,
        }) """
        
        