from django import template
from patlove.portal.models import Banner

register = template.Library()

@register.inclusion_tag("widgets/slider.html")
def slider_banner():
    banners = Banner.objects.all()
    print(banners)
    return{
        "banners":banners
    }