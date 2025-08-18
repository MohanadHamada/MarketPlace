from django.db import models
from category.models import Category


class Product(models.Model):
    code_num = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    instock_items = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField()


    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True, blank=True)


    def __str__(self):
        return self.name
