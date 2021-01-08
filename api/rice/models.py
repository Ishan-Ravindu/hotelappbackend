from django.db import models


class Rice(models.Model):

    name = models.CharField(max_length=50)
    price = models.IntegerField()
    is_stock_avalable = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Curry(models.Model):

    name = models.CharField(max_length=50)
    price = models.IntegerField()

    is_stock_avalable = models.BooleanField(default=True)

    def __str__(self):
        return self.name
