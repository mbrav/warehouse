from autoslug import AutoSlugField
from django.db import models
from wagtail.admin.edit_handlers import (FieldPanel, FieldRowPanel,
                                         MultiFieldPanel)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet


@register_snippet
class ProductCategory(models.Model):

    name = models.CharField(max_length=60)
    slug = AutoSlugField(
        populate_from='name',
        unique=True,
        null=False,
        editable=False)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='children',
        null=True,
        blank=True)

    description = models.TextField(
        blank=True,
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('description'),
        SnippetChooserPanel('parent'),
    ]

    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categories'
        ordering = ('name',)
        unique_together = ('slug', 'parent',)

    def __str__(self):
        full_path = [self.name]
        parent = self.parent
        while parent is not None:
            full_path.append(parent.name)
            parent = parent.parent
        return ' / '.join(full_path[::-1])
        # return '{}'.format(self.name)


@register_snippet
class Product(models.Model):

    name = models.CharField(max_length=60)

    category = models.ForeignKey(
        ProductCategory,
        related_name='products',
        help_text='Company that the person is related to',
        on_delete=models.CASCADE,
        blank=True,
        null=True,)

    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Product image',
        null=True,
        blank=True,)

    price = models.DecimalField(
        default=0,
        decimal_places=2,
        max_digits=10,
        blank=True,
    )

    description = models.TextField()

    panels = [
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('name', classname="col8"),
                FieldPanel('price', classname="col4"),
            ])
        ], "Name"),
        FieldPanel('description'),
        SnippetChooserPanel('category'),
        ImageChooserPanel('image'),
    ]

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
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
