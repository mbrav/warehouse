from django.db import models

from apps.customers.models import Customer
from apps.warehouse.models import Product


class Payment(models.Model):

    PAYMENT_PAID = (
        ('0', 'Pending'),
        ('1', 'Paid'),
    )

    PAYMENT_TYPE = (
        ('0', 'Cash'),
        ('1', 'Transfer'),
        ('2', 'Card'),
    )

    date = models.DateField()

    written_off = models.BooleanField(
        'Set whether the payment should be written off from finances',
        default=False,
    )

    amount = models.DecimalField(
        default=0,
        decimal_places=2,
        max_digits=10,
        blank=True,
    )

    method = models.CharField(
        'Payment method',
        max_length=2,
        choices=PAYMENT_TYPE,
        default='0',
    )

    status = models.CharField(
        'Payment status',
        max_length=2,
        choices=PAYMENT_PAID,
        default='1',
    )

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='payments',
        help_text='Payments that customer has made',
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'
        ordering = ('-date',)
        get_latest_by = 'date'

    def __str__(self):
        return '#{} – ({})'.format(self.id, self.date)


class ProductOrder(models.Model):

    product = models.ForeignKey(
        Product,
        related_name='products',
        on_delete=models.CASCADE,
        # unique=True,
    )

    payment = models.ForeignKey(
        Payment,
        related_name='product_purchases',
        on_delete=models.CASCADE,
        # unique=True,
    )

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='orders',
        help_text='Orders that the customer has made',
        # unique=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def date(self):
        return self.payment.date

    class Meta:
        verbose_name = 'Product Order'
        verbose_name_plural = 'Product Orders'

    def __str__(self):
        return 'Order %s by ' % (self.product)
