from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)

class Category(models.Model):
    name = models.CharField(max_length=200)

class Comment(models.Model):
    company =  Company
    category = Category
    rate = models.IntegerField
    comments = models.CharField(max_length=400)
