from django import template

register = template.Library()

@register.filter
def color_from_name(value):
    a = ord('a')
    k = 255.0 / 26
    s = "#" + "".join(format(int((ord(x) - a)*k), 'x') for x in value + '123')
    return s.replace('-', '')[0:7]
