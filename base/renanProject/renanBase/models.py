from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=20)
    creationDate = models.DateTimeField(auto_now_add=True)

# Create your models here.
