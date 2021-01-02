from django.db import models


class Image(models.Model):
    CHOICES = (
        ('BF', 'උදේ'),
        ('LU', 'දවල්'),
        ('DI', 'රාත්‍රි'),
    )

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='product', blank=True, null=True)
    category = models.CharField(max_length=50, choices=CHOICES)

    def __str__(self):
        return self.name


class Rice(models.Model):
    CHOICES = (
        ('BF', 'උදේ'),
        ('LU', 'දවල්'),
        ('DI', 'රාත්‍රි'),
        ('SN', 'බයිට්'),
        ('BF-LU', 'උදේ-දවල්'),
        ('BF-DI', 'උදේ-රාත්‍රි'),
        ('LU-DI', 'දවල්-රාත්‍රි'),
        ('BF-LU-DI', 'උදේ-දවල්-රාත්‍රි'),


    )
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices=CHOICES)
    price = models.IntegerField()
    is_stock_avalable = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Curry(models.Model):
    CHOICES = (
        ('BF', 'උදේ'),
        ('LU', 'දවල්'),
        ('DI', 'රාත්‍රි'),
        ('SN', 'බයිට්'),
        ('BF-LU', 'උදේ-දවල්'),
        ('BF-DI', 'උදේ-රාත්‍රි'),
        ('LU-DI', 'දවල්-රාත්‍රි'),
        ('BF-LU-DI', 'උදේ-දවල්-රාත්‍රි'),


    )
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    category = models.CharField(max_length=50, choices=CHOICES)
    is_stock_avalable = models.BooleanField(default=True)

    def __str__(self):
        return self.name
