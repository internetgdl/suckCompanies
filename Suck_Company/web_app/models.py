from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)
    complain = models.CharField(max_length=400)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)

