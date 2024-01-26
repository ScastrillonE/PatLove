from django.db import models
from tenant_schemas.models import TenantMixin

class AccountBank(models.Model):
    name = models.CharField('Bank name',max_length=120,default="")
    qr = models.ImageField()

# Create your models here.
class Foundation(TenantMixin):
    name = models.CharField('foundation name',max_length=120,default="")
    address = models.CharField('Address of foundation',max_length=100,default="0")
    email = models.CharField('Email of foundation',max_length=100,default="0")
    phone_number = models.CharField('Phone of foundation',max_length=100,default="0")
    logo = models.ImageField('Logo of foundation',upload_to="tenant_img")
    
    
    
    
    instagram = models.CharField('instagram of foundation',max_length=100,default="0")
    twitter = models.CharField('twitter of foundation',max_length=100,default="0")
    facebook = models.CharField('facebook of foundation',max_length=100,default="0")
    active_home_page = models.BooleanField('Activate home page?', help_text='Check to activate the home page. If not activated, the adoption page will be the home page.')
    active_about_page = models.BooleanField('Activate about page?', help_text='Check to activate the about page.')
    active_services_page = models.BooleanField('Activate services page?', help_text='Check to activate the services page.')