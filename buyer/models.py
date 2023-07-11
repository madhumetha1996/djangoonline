from django.db import models

class Buyer(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    

    def __str__(self):
        return self.username

class Order(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name='buyer_carts')
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.buyer} - {self.product}"

class Cart(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name='buyer_orders')
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.buyer} - {self.product}"

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name
