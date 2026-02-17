from django.db import models

class Product(models.Model):

    name = models.CharField(max_length=200)

    category = models.CharField(max_length=200)

    price = models.FloatField()

    description = models.TextField()

    def __str__(self):
        return self.name

# Create your models here.
