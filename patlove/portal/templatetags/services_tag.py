from django import template
from patlove.portal.models import ServiceInfo
register = template.Library()

@register.inclusion_tag("widgets/services.html")
def services():
    serviceSectionInfo = ServiceInfo.objects.get()
    services = serviceSectionInfo.services.all() 

    return{
        "serviceSectionInfo" : serviceSectionInfo,
        "services":services
    }