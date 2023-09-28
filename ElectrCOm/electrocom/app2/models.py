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
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICE, blank=True, null=True)

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
    brand_name = models.CharField(max_length=255, null=True)
    product_name = models.CharField(max_length=255, null=True)
    color= models.CharField(max_length=255,null=True)
    price = models.CharField(max_length=255, null=True)
    image1 = models.ImageField(upload_to='sample/', null=True, blank=True, max_length=255)
    image2 = models.ImageField(upload_to='sample/', null=True, blank=True, max_length=255)
    image3 = models.ImageField(upload_to='sample/', null=True, blank=True, max_length=255)
    description = models.TextField(max_length=255, null=True)
    category = models.CharField(max_length=255, null=True), """ mobile, laptop, headset, speaker"""
    warranty = models.CharField(max_length=255,null=True)
     
    def __str__(self):
        return self.product_name
    
class ProductLap(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    screen_size = models.CharField(max_length=255, null=True)
    space = models.CharField(max_length=255, null=True) ,""" hard disk /ssd"""
    cpu = models.CharField(max_length=255, null=True),'''core i7/ Ryzen 5'''
    ram = models.CharField(max_length=255, null=True)
    os = models.CharField(max_length=255, null=True), """ windows 10, linux, mac os"""
    graphics = models.CharField(max_length=255, null=True), """ nvidia, amd, intel"""
    color= models.CharField(max_length=255,null=True)
    ram = models.TextField(max_length=255, null=True)
    processor = models.CharField(max_length=255, null=True)
    storage = models.CharField(max_length=255, null=True)
    

    
    def __str__(self):
        return self.product_name
    
class ProductMobile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    wireless = models.CharField(max_length=255, null=True), """ unlocked for all carriers"""
    m_os = models.CharField(max_length=255, null=True), """ android 13.0"""
    cellular = models.CharField(max_length=255, null=True), """ 4g, 5g"""
    memory = models.CharField(max_length=255, null=True), """ 128gb, 256gb"""
    connectivity = models.CharField(max_length=255, null=True), """ wifi, bluetooth"""
    m_screen = models.CharField(max_length=255, null=True), """ 6.5 inch"""
    wireless_network_technology = models.CharField(max_length=255, null=True), """ unlocked for all carriers"""
    color= models.CharField(max_length=255,null=True)
    ram = models.TextField(max_length=255, null=True)
    processor = models.CharField(max_length=255, null=True)
    storage = models.CharField(max_length=255, null=True)
    camrear = models.CharField(max_length=255, null=True)
    camfront = models.CharField(max_length=255, null=True)
    display = models.TextField(max_length=255, null=True)  

    status=models.BooleanField(default=False)

    def __str__(self):
        return self.product_name
    
class ProductHeadset(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    battery = models.CharField(max_length=255, null=True)
    color= models.CharField(max_length=255,null=True)
    form_factor = models.CharField(max_length=255, null=True), """ in-ear, over-ear, on-ear"""
    h_connectivity = models.CharField(max_length=255, null=True), """ bluetooth, wired"""  
    
    def __str__(self):
        return self.product_name

class ProductSpeaker(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    battery = models.CharField(max_length=255, null=True) 
    s_connectivity = models.CharField(max_length=255, null=True), """ bluetooth, wired"""
    s_type = models.CharField(max_length=255, null=True), """ portable, home, outdoor"""
    special_features = models.CharField(max_length=255, null=True), """ waterproof, dustproof"""
    
    def __str__(self):
        return self.product_name
