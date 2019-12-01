from django.db import models
from django.contrib.auth.models import UserManager

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
    password = models.CharField(max_length=55)

    objects = UserManager()

    class Meta():
        db_table = "user"
