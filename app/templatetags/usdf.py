from django import template

register=template.Library()

def swap(value):
    return value.swapcase()

register.filter('swapping',swap)

def count(value,cc):
    return value.lower().count(cc.lower())

register.filter(count)

@register.filter('deleting')
def delete(value,dc):
    return value.replace(dc,'')

@register.filter()
def startswith(value,sc):
    return value.startswith(sc)