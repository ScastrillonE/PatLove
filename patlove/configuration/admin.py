from django.contrib import admin
from .models import Foundation
# Register your models here.

@admin.register(Foundation)
class FoundationAdmin(admin.ModelAdmin):
    pass