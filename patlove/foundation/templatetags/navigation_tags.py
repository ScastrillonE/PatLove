from django import template

register = template.Library()

@register.inclusion_tag('nav.html',takes_context=True)
def nav_menu(context):
    foundation_name = context['foundation_name']
    return {
        'foundation_name': foundation_name
    }

@register.inclusion_tag('preloader.html')
def preloader():
    pass

@register.inclusion_tag('footer.html', takes_context = True)
def footer(context):
    foundation_name = context['foundation_name']
    return {
        'foundation_name': foundation_name
    }