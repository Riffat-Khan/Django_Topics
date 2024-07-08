from django import template

register = template.Library()

@register.filter(name='toupper')
def toupper(string):
    return string.upper()