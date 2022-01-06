from django.core.validators import RegexValidator
from django.db import models


class Location(models.Model):
    """Location Class"""

    address = models.TextField(
        max_length=300,
        blank=True)

    def __str__(self):
        return '{}'.format(self.id)


class Customer(models.Model):
    """Base Customer Class"""

    email = models.CharField(
        max_length=100,
        blank=True)

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message='Phone number must be entered in the format:'
        '"+999999999". Up to 15 digits allowed.')
    phone = models.CharField(
        validators=[phone_regex],
        max_length=15,
        blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.id)


class Company(Customer):
    """ Company class identifies a unique physical person by its first name, last name"""

    name = models.CharField(
        max_length=100)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        ordering = ('name',)

    def __str__(self):
        return '{}'.format(self.name)


class Person(Customer):
    """ Person class identifies a unique physical person by its first name, last name"""

    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    first_name = models.CharField(
        max_length=100)

    last_name = models.CharField(
        max_length=100)

    gender = models.CharField(
        max_length=2,
        choices=GENDERS,
        default="0",
    )

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'
        unique_together = (('first_name', 'last_name'),)
        ordering = ('last_name', 'first_name')

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
