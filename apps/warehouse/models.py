from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.snippets.models import register_snippet


@register_snippet
class ProductCategory(models.Model):

    name = models.CharField(max_length=60)

    description = models.TextField(
        blank=True,
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('description'),
    ]

    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categories'
        ordering = ('name',)

    def __str__(self):
        return '{}'.format(self.name)


@register_snippet
class Product(models.Model):

    name = models.CharField(max_length=60)

    price = models.DecimalField(
        default=0,
        decimal_places=2,
        max_digits=10,
        blank=True,
    )

    category = models.ForeignKey(
        ProductCategory,
        related_name='products',
        help_text='Company that the person is related to',
        on_delete=models.CASCADE,
        blank=True,
        null=True,)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Commodities'
        ordering = ('price',)

    def __str__(self):
        return '{}'.format(self.name)


@register_snippet
class Stock(models.Model):

    count = models.IntegerField(
        default=0,
    )

    product = models.ForeignKey(
        Product,
        related_name='stock',
        help_text='Stock of the product',
        on_delete=models.CASCADE,
        blank=True,
        null=True,)

    class Meta:
        verbose_name = 'Stock'
        verbose_name_plural = 'Stock'

    def __str__(self):
        return '{}'.format(self.count)
