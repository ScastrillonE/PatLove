# from django.contrib import admin
# from django.http.request import HttpRequest
# from tenant_schemas.utils import connection, get_public_schema_name
# from .models import Tenant,AccountBank,Foundation

# class AccountBankInline(admin.TabularInline):
#     model = AccountBank
#     extra=1
    
# @admin.register(Foundation)
# class FoundationAdmin(admin.ModelAdmin):
#     inline = [AccountBankInline]
    
# @admin.register(Tenant)
# class TenantAdmin(admin.ModelAdmin):
    
    
#     def has_add_permission(self, request, obj=None):
#         tenant = connection.tenant
#         principal_schema_name = get_public_schema_name()
#         if tenant.schema_name == principal_schema_name:
#             return True
#         return False
    
#     def has_change_permission(self, request: HttpRequest, obj = None) -> bool:
#         tenant = connection.tenant
#         principal_schema_name = get_public_schema_name()
#         if tenant.schema_name == principal_schema_name:
#             return True
#         return False
    
    
# #admin.site.register(AccountBank) # Uncomment to have model registered independently

