from django import template


register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """ Calculates the subtotal of each item in shopping cart """
    return price * quantity