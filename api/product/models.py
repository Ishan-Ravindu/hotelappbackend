from django.db import models

# Create your models here.


class Product(models.Model):
    CHOICES = (
        ('BF', 'උදේ'),
        ('LU', 'දවල්'),
        ('DI', 'රාත්‍රි'),
        ('SN', 'බයිට්'),
        ('OT', 'වෙනත්'),
        ('BF-LU', 'උදේ-දවල්'),
        ('BF-DI', 'උදේ-රාත්‍රි'),
        ('LU-DI', 'දවල්-රාත්‍රි'),
        ('BF-LU-DI', 'උදේ-දවල්-රාත්‍රි'),


    )

    name = models.CharField(max_length=50)
    discription = models.CharField(max_length=250)
    category = models.CharField(max_length=50, choices=CHOICES)
    price = models.IntegerField()
    image = models.ImageField(upload_to='product', blank=True, null=True)
    is_stock_avalable = models.BooleanField(default=True)

    def __str__(self):
        return self.name
