from django.db import models


class Order(models.Model):

    CHOICES = (
        ('pending', 'pending'),
        ('conform', 'conform'),
        ('dileved', 'dileved'),
        ('rejected', 'rejected'),
    )

    name = models.CharField(max_length=50, )
    phone_no = models.IntegerField()
    orders = models.TextField()
    total = models.IntegerField()
    adress = models.TextField()
    status = models.CharField(
        max_length=50, choices=CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
