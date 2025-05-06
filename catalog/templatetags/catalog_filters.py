from django import template
from django.contrib.humanize.templatetags.humanize import intcomma

register = template.Library()

@register.filter
def intspace(value):
    return intcomma(value).replace(',', ' ')
