import os
from django.db import models
from tenant_schemas.models import TenantMixin

# Create your models here.
class Tenant(TenantMixin):
    def __str__(self):
        return self.schema_name
    
