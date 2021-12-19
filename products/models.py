from django.db import models


class Category(models.Model):
    """
    Model for creating categories
    """
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Model for adding products to website
    """
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name
