from django.db import models


class Order(models.Model):

    CHOICES = (
        ('pending', 'pending'),
        ('conform', 'conform'),
        ('dilever', 'dilever'),
    )

    name = models.CharField(max_length=50, null=True)
    image = models.URLField(null=True)
    price = models.IntegerField(null=True)
    unit = models.IntegerField(null=True)
    total = models.IntegerField(null=True)
    phone_no = models.IntegerField(null=True)
    adress = models.TextField(null=True)
    status = models.CharField(max_length=50, choices=CHOICES, null=True)

    def __str__(self):
        return self.name
