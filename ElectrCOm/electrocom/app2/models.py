from urllib import request
from django.db import models
from django.db import migrations

# Create your models here.
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.shortcuts import redirect, render

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, name, email, password=None):
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            name=name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractUser):
    CUSTOMER = 1
    SELLER = 2
    DELIVERY = 3

    ROLE_CHOICE = (
        (CUSTOMER, 'Customer'),
        (SELLER, 'Seller'),
        (DELIVERY, 'Delivery'),
    )

    username=None
    USERNAME_FIELD = 'email'
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True) 
    password = models.CharField(max_length=128)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICE, default=1 ,blank=True, null=True)

    # date_joined = models.DateTimeField(auto_now_add=True)
    # last_login = models.DateTimeField(auto_now_add=True)
    # created_date = models.DateTimeField(auto_now_add=True)
    # modified_date = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)

    
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def str(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
    
class Product(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255, null=True)
    product_name = models.CharField(max_length=255, null=True)
    brand_name = models.CharField(max_length=255, null=True)
    price = models.CharField(max_length=255, null=True)
    image1 = models.ImageField(upload_to='sample/', null=True, blank=True, max_length=255)
    image2 = models.ImageField(upload_to='sample/', null=True, blank=True, max_length=255)
    image3 = models.ImageField(upload_to='sample/', null=True, blank=True, max_length=255)
    description = models.TextField(max_length=255, null=True)
    category = models.CharField(max_length=255, null=True)
    stock = models.PositiveIntegerField(max_length=255, default=0)
    
     
    def __str__(self):
        return self.product_name
    
class ProductLap(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    screen_size = models.CharField(max_length=255, null=True)
    space = models.CharField(max_length=255, null=True)
    ram = models.CharField(max_length=255, null=True)
    os = models.CharField(max_length=255, null=True)
    graphics = models.CharField(max_length=255, null=True)
    color= models.CharField(max_length=255,null=True)
    processor = models.CharField(max_length=255, null=True)
    storage = models.CharField(max_length=255, null=True)
    
    
class ProductMobile(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    wireless = models.CharField(max_length=255, null=True)
    m_os = models.CharField(max_length=255, null=True)
    cellular = models.CharField(max_length=255, null=True)
    memory = models.CharField(max_length=255, null=True)
    connectivity = models.CharField(max_length=255, null=True)
    m_screen = models.CharField(max_length=255, null=True)
    wireless_network_technology = models.CharField(max_length=255, null=True)
    color= models.CharField(max_length=255,null=True)
    ram = models.TextField(max_length=255, null=True)
    processor = models.CharField(max_length=255, null=True)
    camrear = models.CharField(max_length=255, null=True)
    camfront = models.CharField(max_length=255, null=True)  

    
class ProductHeadset(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    battery = models.CharField(max_length=255, null=True)
    color= models.CharField(max_length=255,null=True)
    form_factor = models.CharField(max_length=255, null=True) 
    h_connectivity = models.CharField(max_length=255, null=True) 
    weight = models.CharField(max_length=255, null=True)
    charging = models.CharField(max_length=255, null=True) 
    working = models.CharField(max_length=255, null=True)
    


class ProductSpeaker(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    battery = models.CharField(max_length=255, null=True) 
    s_connectivity = models.CharField(max_length=255, null=True)
    s_type = models.CharField(max_length=255, null=True)
    special_features = models.CharField(max_length=255, null=True)
    weight = models.CharField(max_length=255, null=True)
    charging = models.CharField(max_length=255, null=True)
    working = models.CharField(max_length=255, null=True)
    
class Wishlist(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    
class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    cartstock = models.PositiveIntegerField(default=1)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    # subtotal = models.IntegerField(default=0)
    # total = models.IntegerField(default=0)
    # def update_total(self):
    #     self.price = self.quantity * self.product.price
    
    def carttotal(self):
        self.cartstock = self.product.stock


class Order(models.Model):
    class PaymentStatusChoices(models.TextChoices):
        PENDING = 'pending', 'Pending'
        SUCCESSFUL = 'successful', 'Successful'
        FAILED = 'failed', 'Failed'

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    razorpay_order_id = models.CharField(max_length=255)
    # payment_id = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    payment_status = models.CharField(
        max_length=20, choices=PaymentStatusChoices.choices, default=PaymentStatusChoices.PENDING)
    timestamp = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField(Product)  # Use the correct model name 'Book'

    def str(self):
        return f"Order for {self.user.username}"

    class Meta:
        ordering = ['-timestamp']