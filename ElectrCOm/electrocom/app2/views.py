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

# def add_to_cart(request,category,product_id):
    
    existing_item = Cart.objects.filter(product_id=product_id, user=request.user).first()
    if existing_item:
        existing_item.quantity += 1
        existing_item.save()
    elif category=="headset":
        Cart.objects.create(user=request.user, product_id=product_id, quantity=1)

    
    
    else:
        Cart.objects.create(user=request.user, product_id=product_id, quantity=1)
        
    return redirect('cart')

# def cart(request):
    items=Cart.objects.filter(user_id=request.user.id)
    return render(request,'cart.html',{'items':items})

# def add_to_cart(request,category, product_id):
    if request.user.is_authenticated:
        product = get_object_or_404(ProductHeadset, id=product_id)
        cart_item, created = CartItem.objects.get_or_create(user=request.user, product_id=product.id)

        if not created:
            cart_item.quantity += 1
            cart_item.save()
        return redirect('cart')

# def cart(request): 
    cart_items = CartItem.objects.filter(user=request.user) 
    total_items = sum(cart_item.quantity for cart_item in cart_items)
    total_price = sum(cart_item.product.price * cart_item.quantity for cart_item in cart_items)
    context = {
        'cart_items': cart_items,
        'total_items': total_items,
        'total_price': total_price,
            # ... other context variables ... 
    } 
    return render(request, 'customer_Cart.html',context) 
 
# def remove_from_cart(request, product_id): 
    cart_item = get_object_or_404(CartItem, user=request.user, id=product_id) 
    print(f"Received product_id: {product_id}")  #Fixed the typo here 
    cart_item.delete() 
    return redirect('cart')

# def decrease_item(request, item_id): 
#     try: 
#         cart_item = CartItem.objects.get(id=item_id) 
#         if cart_item.quantity > 1: 
#             cart_item.quantity -= 1 
#             cart_item.save() 
#     except CartItem.DoesNotExist: 
#         pass  # Handle the case when the item does not exist in the cart 
#     return redirect('cart')  # Redirect back to the cart page after decreasing the item quantity 
 
# def increase_item(request, item_id): 
    try: 
        cart_item = CartItem.objects.get(id=item_id) 
        cart_item.quantity += 1 
        cart_item.save() 
    except CartItem.DoesNotExist: 
        pass  # Handle the case when the item does not exist in the cart 
    return redirect('cart')

# def add_to_cart(request, product_id):
    product = ProductLap.objects.get(id=product_id)
    
    existing_item = CartItem.objects.filter(product=product, user=request.user).first()
    
    if existing_item:
        existing_item.quantity += 1
        existing_item.save()
    else:
        CartItem.objects.create(user=request.user, product=product, quantity=1)
        
    return redirect('cart')

# def add_to_cart(request, product_type, product_id):
#     # Determine the product type and get the corresponding product model
#     product_model = None
#     if product_type == 'laptop':
#         product_model = ProductLap
#     elif product_type == 'mobile':
#         product_model = ProductMobile
#     elif product_type == 'headset':
#         product_model = ProductHeadset
#     elif product_type == 'speaker':
#         product_model = ProductSpeaker

#     if product_model:
#         # Get the product instance
#         product_instance = get_object_or_404(product_model, pk=product_id)

#         # Check if the user already has this product in the cart
#         cart_item, created = CartItem.objects.get_or_create(
#             user=request.user, product_type=product_type, product_id=product_id
#         )

#         if not created:
#             # If the item already exists in the cart, increment the quantity
#             cart_item.quantity += 1
#             cart_item.save()
#         else:
#             # If the item doesn't exist in the cart, create a new cart item
#             CartItem.objects.create(
#                 user=request.user,
#                 product_type=product_type,
#                 product_id=product_id,
#                 quantity=1,
#                 total_price=product_instance.price,
#                 total_items=1
#             )

#     return redirect('cart') 


# def cart(request):
#     # You can retrieve the product details for each cart item here

#     return render(request, 'cart.html')