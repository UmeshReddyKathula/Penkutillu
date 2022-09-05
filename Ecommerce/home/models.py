from distutils.command.upload import upload
from unicodedata import category
from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=300)
    publish_date = models.DateField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.product_name