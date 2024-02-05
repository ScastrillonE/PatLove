from django.core.files.storage import FileSystemStorage
from tenant_schemas.utils import connection

class TenantFileSystemStorage(FileSystemStorage):
  @property
  def tenant_model(self):
    if hasattr(self, '_tenant_model'):  
       return self._tenant_model

    tenant = connection.tenant 
    self._tenant_model = tenant
    return self._tenant_model
  
  def generate_filename(self, filename):
    filename_with_tenant = f"{self.tenant_model.schema_name}/{filename}"
    return super().generate_filename(filename=filename_with_tenant)