from django.contrib import admin
from .models import RescuePet,RescuePetPhoto


class RescuePetPhotoInline(admin.StackedInline):
    model= RescuePetPhoto
    extra=1
    
@admin.register(RescuePet)
class RescuePetAdmin(admin.ModelAdmin):
    inlines=[RescuePetPhotoInline]
