from django.db import models
from django.core.validators import MinValueValidator


SPECIES_CHOICES = [
    ("DG","DOG"),
    ("CT","CAT")
]

GENDER_CHOICES = [
    ('M','Male'),
    ('F','Female')
]

SIZE_CHOICES = [
    ('B','Big'),
    ('M','Medium'),
    ('S','Small')
]

AGE_CHOICES=[
    ("A","Adult"),
    ("K","Kitten"),
    ("Y","Young"),
    ("S","Senior")
]

class RescuePet(models.Model):
    name = models.CharField("Name of Rescue Pet",max_length=100)
    species = models.CharField("Specie of rescue pet",max_length = 4,choices=SPECIES_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.CharField("Age of rescue pet",choices=AGE_CHOICES,max_length=1)
    neutered = models.BooleanField("It's neutered?",default=False)
    vaccinated = models.BooleanField("It's vaccinated",default = False)
    size = models.CharField("Size rescue pet",choices=SIZE_CHOICES,max_length=1 )
    about = models.TextField("About rescue pet")
    amount_adoption_fee = models.CharField("Amount adoption fee",blank=True,null=True,default="0")
    adopted = models.BooleanField("Adopted pet",default =False)
    
    def __str__(self) -> str:
        return self.name

class RescuePetPhoto(models.Model):
    image=models.ImageField(upload_to="rescuePet")
    rescuePet = models.ForeignKey(RescuePet,on_delete=models.CASCADE,related_name = "rescuePetPhoto")
    

