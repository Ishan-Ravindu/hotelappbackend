from django.db import models

# Create your models here.


class Banner(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='banner', blank=True, null=True)

    def __str__(self):
        return self.name
