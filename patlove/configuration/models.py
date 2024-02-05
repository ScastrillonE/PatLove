from django.db import models
from solo.models import SingletonModel


class Foundation(SingletonModel):
    name = models.CharField('foundation name',max_length=120,default="")
    address = models.CharField('Address of foundation',max_length=100,default="0")
    email = models.CharField('Email of foundation',max_length=100,default="0")
    phone_number = models.CharField('Phone of foundation',max_length=100,default="0")
    logo = models.ImageField('Logo of foundation', upload_to="logos",null=True)
    nit = models.CharField('Nit of foundation',max_length=9,default="0")
    
    
    instagram = models.CharField('instagram of foundation',max_length=100,default="0")
    twitter = models.CharField('twitter of foundation',max_length=100,default="0")
    facebook = models.CharField('facebook of foundation',max_length=100,default="0")
    active_home_page = models.BooleanField('Activate home page?', help_text='Check to activate the home page. If not activated, the adoption page will be the home page.',default=True)
    active_about_page = models.BooleanField('Activate about page?', help_text='Check to activate the about page.',default=True)
    active_services_page = models.BooleanField('Activate services page?', help_text='Check to activate the services page.',default=True)
    is_verify = models.BooleanField('Is verify foundation?',default=False)
    adoption_fee = models.BooleanField("Adoption fee?",default = False)

    def __str__(self):
        return self.name
    
        

class AccountBank(models.Model):
    foundation = models.ForeignKey(Foundation,on_delete=models.CASCADE)
    name = models.CharField('Bank name',max_length=120,default="")
    number=models.CharField('Bank account number',max_length=20,default="")
    qr = models.ImageField(upload_to="qr_bank",blank=True,null=True)
    
    def __str__(self) -> str:
        return f"{self.name} - {self.foundation}"
    
    