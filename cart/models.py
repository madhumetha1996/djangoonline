from django.db import models

class Cart(models.Model):
    buyer_name = models.CharField(max_length=100, null=True, default='store')
    product_name = models.CharField(max_length=100)
    

    def __str__(self):
        return f"{self.buyer_name} - {self.product_name}"

class Billing(models.Model):
    cart = models.ForeignKey('cart.Cart', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    

    def __str__(self):
        return f"Billing for Cart: {self.cart}"

class Invoice(models.Model):
    cart = models.OneToOneField('cart.Cart', on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    

    def __str__(self):
        return f"Invoice for Cart: {self.cart}"
