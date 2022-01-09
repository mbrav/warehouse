from apps.warehouse.models import Product
from django import template

register = template.Library()


# Retrieves a single gallery item and returns a gallery of images
@register.inclusion_tag('tags/products.html', takes_context=True)
def gallery(context, gallery):
    products = Product.objects.filter(collection=gallery)

    return {
        'images': images,
        'request': context['request'],
    }
