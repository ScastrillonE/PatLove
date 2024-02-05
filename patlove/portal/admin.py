from django.contrib import admin
from .models import Banner,Service,ServiceInfo

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    pass

class ServiceInline(admin.TabularInline):
    model = Service
    extra = 1  # Número de formularios en línea para mostrar

class ServiceInfoAdmin(admin.ModelAdmin):
    inlines = [ServiceInline]

admin.site.register(ServiceInfo, ServiceInfoAdmin)