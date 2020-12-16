from django.db import models

# Create your models here.


class Product(models.Model):
    CHOICES = (
        ('BREAKFIRST', 'උදේ'),
        ('LUNCH', 'දවල්'),
        ('DINNER', 'රාත්‍රි'),
        ('SNACK', 'බයිට්'),

    )

    name = models.CharField(max_length=50)
    discription = models.CharField(max_length=250)
    category = models.CharField(max_length=50, choices=CHOICES)
    price = models.IntegerField()
    image = models.ImageField(upload_to='product', blank=True, null=True)
    is_stock_avalable = models.BooleanField(default=True)

    def __str__(self):
        return self.name
