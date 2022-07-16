from ..encrypt import decrypt
from django import template

register = template.Library()

@register.simple_tag
def detxt(text):
    new = decrypt(text)
    return new