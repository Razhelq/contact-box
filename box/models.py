from django.db import models


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
    photo = models.ImageField(
        verbose_name='Photo',
        upload_to='photos/',
        blank=True,
        default='photos/None/no-img.jpg'
    )


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
    person = models.ForeignKey(
        Person,
        verbose_name='Person',
        on_delete=models.CASCADE,
        null=True
    )


class Phone(models.Model):
    home_phone = models.CharField(
        verbose_name='HomePhone',
        max_length=32,
        default='-'
    )
    work_phone = models.CharField(
        verbose_name='WorkPhone',
        max_length=32,
        default='-'
    )
    person = models.ForeignKey(
        Person,
        verbose_name='Person',
        on_delete=models.CASCADE,
        null=True
    )


class Email(models.Model):
    home_email = models.CharField(
        verbose_name='HomeEmail',
        max_length=32,
        default='-'
    )
    work_email = models.CharField(
        verbose_name='WorkEmail',
        max_length=32,
        default='-'
    )
    person = models.ForeignKey(
        Person,
        verbose_name='Person',
        on_delete=models.CASCADE,
        null=True
    )


class Group(models.Model):
    name = models.CharField(
        verbose_name='Name',
        max_length=32,
        default='-'
    )
    person = models.ManyToManyField(
        Person,
        verbose_name='Group',
        null=True
    )
