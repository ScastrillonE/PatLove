from django import template
from django.core.paginator import Paginator
from patlove.rescuePet.models import RescuePet


register = template.Library()

@register.inclusion_tag("widgets/adopt_cards.html")
def adopt_cards():
    rescuepets = RescuePet.objects.filter(adopted = False)
    paginator = Paginator(rescuepets,5)
    return {
        "rescuePets":paginator.object_list
    }
    
    