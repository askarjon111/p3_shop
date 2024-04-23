from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    weight = models.IntegerField(blank=True, null=True)
    price = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="products/", blank=True, null=True)

    def __str__(self):
        return self.name

