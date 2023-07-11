from django.db import models

class Seller(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as per your requirements

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as per your requirements

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    seller_name = models.CharField(max_length=100)  

    def __str__(self):
        return self.name
    

class Buyer(models.Model):
    name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name


class Order(models.Model):
    buyer_name = models.CharField(max_length=100)  
    product_name = models.CharField(max_length=100)  
    

    def __str__(self):
        return f"{self.buyer_name} - {self.product_name}"

class Cart(models.Model):
    buyer_name = models.CharField(max_length=100)  
    product_name = models.CharField(max_length=100)  


    def __str__(self):
        return f"{self.buyer_name} - {self.product_name}"
