from django.db import models


class Order(models.Model):

    CHOICES = (
        ('pending', 'pending'),
        ('conform', 'conform'),
        ('dilever', 'dilever'),
    )

    name = models.CharField(max_length=50)
    image = models.URLField()
    price = models.IntegerField()
    unit = models.IntegerField()
    total = models.IntegerField()
    phone_no = models.IntegerField()
    adress = models.TextField()
    status = models.CharField(max_length=50, choices=CHOICES)

    def __str__(self):
        return self.name
