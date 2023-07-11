from django.db import models

class Order(models.Model):
    order_number = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
   

    def __str__(self):
        return self.order_number

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
   
    def __str__(self):
        return self.product_name
