from django import template
from patlove.configuration.models import Foundation

register = template.Library()

@register.inclusion_tag('core/nav.html')
def nav_menu():
    foundation_data = Foundation.objects.only("name","logo").get()
    foundation_logo = foundation_data.logo
    foundation_name = foundation_data.name
    return {
        'foundation_name': foundation_name,
        'foundation_logo':foundation_logo
    }

@register.inclusion_tag('core/preloader.html')
def preloader():
    pass

@register.inclusion_tag('core/footer.html')
def footer():
    foundation_name = Foundation.objects.only("name").get().name
    return {
        'foundation_name': foundation_name
    }