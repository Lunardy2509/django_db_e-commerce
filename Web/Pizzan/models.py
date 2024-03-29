from django.db import models
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Product(models.Model):
    food_name = models.CharField(max_length=200)
    food_stock = models.CharField(max_length=100)
    food_price = models.DecimalField(max_digits=10, decimal_places=2)
    food_disc = models.CharField(max_length=100)
    food_image = models.ImageField(upload_to='media/')
    food_desc = models.TextField(max_length=200)
    food_reviews = models.CharField(max_length=100)
    food_sku = models.CharField(max_length=100)
    food_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    food_tag = models.CharField(max_length=200)
    product_desc = models.TextField(max_length=200)
    def __str__(self):
        return self.food_name

class Chef(models.Model):
    chef_name = models.CharField(max_length=200) #chef name
    chef_role = models.CharField(max_length=200) #chef role
    chef_image = models.ImageField(upload_to='media/') #chef image
    def __str__(self):
        return self.chef_name
    
class Reviewer(models.Model):
    rev_name = models.CharField(max_length=200)
    rev_date = models.DateField()
    rev_desc = models.TextField(max_length=200)
    rev_image = models.ImageField(upload_to='media/')
    def __str__(self):
        return self.rev_name