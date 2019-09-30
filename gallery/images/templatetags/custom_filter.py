from django.template import Library

register = Library()

@register.filter(is_safe=True)
def get(d, k):
    """
    removes leading underscore from dictionary key
    :param d: value
    :param k: argument
    :return: value without leading underscore
    """
    return d.get(k, None)