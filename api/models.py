from datetime import timezone
from django.db import models

# Create your models here.


class Store(models.Model):
    store_id = models.IntegerField(unique=True)
    store_location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.store_id} - {self.store_location}"
    
class Product(models.Model):
    product_id = models.IntegerField(unique=True)
    product_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.product_id} - {self.product_name}"

class Date(models.Model):
    date_id = models.IntegerField(primary_key=True) 
    date_field = models.DateField()  
    
    def __str__(self):
        return f"{self.date_id} - {self.date_field}"