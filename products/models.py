from django.db import models
from wagtail.wagtailcore.fields import RichTextField
from longclaw.longclawproducts.models import ProductVariantBase

class ProductVariant(ProductVariantBase):

    # Enter your custom product variant fields here
    # e.g. colour, size, stock and so on.
    # Remember, ProductVariantBase provides 'price', 'ref', 'slug' fields
    # and the parental key to the Product model.
    _FORMAT_CHOICES = (
        ('CD', 'CD'),
        ('Vinyl', 'Vinyl')
    )
    music_format = models.CharField(max_length=10, choices=_FORMAT_CHOICES)
