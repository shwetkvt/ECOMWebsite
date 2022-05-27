from django.db import models

# Create your models here.
class Product (models.Model):
    product_Id = models.AutoField
    product_name = models.CharField(max_length=100)
    desc = models.CharField (max_length=300)
    pub_date = models.DateField()


