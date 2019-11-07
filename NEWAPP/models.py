from django.db import models

class Product(models.Model):
    pid = models.CharField(max_length=11)
    pname = models.CharField(max_length=55)
    price = models.CharField(max_length=11)
    pdesc = models.CharField(max_length=55)
    class Meta():
        db_table = "product"

class User(models.Model):
    username = models.CharField(max_length=11)
    firstname = models.CharField(max_length=55)
    lastname = models.CharField(max_length=55)
    mobile = models.IntegerField
    u_email = models.EmailField
    password = models.CharField(max_length=55)
    class Meta():
        db_table = "user"
