from django import template
from ..models import Rates

register = template.Library()

def key(d, col):
    print(col)
    return d[col]


register.filter(key)