from django.db import models


class Address(models.Model):
    city = models.CharField(
        verbose_name='City',
        max_length=64
    )
    street = models.CharField(
        verbose_name='Street',
        max_length=64
    )
    house_number = models.CharField(
        verbose_name='HouseNumber',
        max_length=32
    )
    flat_number = models.SmallIntegerField(
        verbose_name='FlatNumber'
    )


class Person(models.Model):
    name = models.CharField(
        verbose_name='Name',
        max_length=32
    )
    surname = models.CharField(
        verbose_name='Surname',
        max_length=32
    )
    description = models.CharField(
        verbose_name='Description',
        max_length=128,
        null=True
    )
    # photo = models.ImageField(
    #     verbose_name='Photo',
    #     upload_to='photo/%Y/%m/%D',
    #     blank=True,
    #     null=True
    # )
    address = models.ForeignKey(
        Address,
        verbose_name='Address',
        on_delete=models.CASCADE,
        null=True
    )


