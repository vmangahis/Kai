from django import template

register = template.Library()


@register.filter
def concatenate_url(url, string):
    return str(url) + str(string)