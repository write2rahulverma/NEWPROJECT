from django.db import models

class Product(models.Model):
    pid = models.CharField(max_length=11)
    pname = models.CharField(max_length=55)
    price = models.CharField(max_length=11)
    pdesc = models.CharField(max_length=55)
    class Meta():
        db_table = "product"
