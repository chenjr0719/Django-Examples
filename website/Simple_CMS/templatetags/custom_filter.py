from django import template
import mistune

register = template.Library()

@register.filter()
def MDParser(content):
    return mistune.markdown(content)

@register.filter()
def Remainder(num, int):
    return num % int
