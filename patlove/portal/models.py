from django.db import models

class Banner(models.Model):
    title = models.CharField("Title banner",help_text="Add a title for show in banner", max_length=30)
    short_description = models.CharField("Short Description",help_text = "Add a short description for banner",max_length = 100)
    background_img = models.ImageField("Image background",help_text="Add a image for the background in banner",upload_to="banner")
    button_message = models.CharField("Button message",help_text = "Add a call to action message",max_length = 13,blank=True,null=True)
    
    def __str__(self) -> str:
        return self.title

class ServiceInfo(models.Model):
    title = models.CharField("Title service section",help_text="Title for section services")
    description = models.TextField("Description services section",help_text = "Description services section")
    image = models.ImageField("Image for services section",upload_to="service-section")
    
class Service(models.Model):
    title = models.CharField("Title service",help_text="Title for services")
    description = models.TextField("Description services ",help_text = "Description services ")
    icon = models.CharField("Select Icon",help_text="Select icon for services",max_length=100)
    serviceInfo = models.ForeignKey(
    ServiceInfo,
    on_delete=models.CASCADE,
    related_name="services"
  )
    

