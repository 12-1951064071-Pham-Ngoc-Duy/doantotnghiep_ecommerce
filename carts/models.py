from django.db import models
from store.models import Product
# Create your models here.

class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    cart_date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id
    

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    cart_item_quantity = models.IntegerField()
    cart_item_is_active = models.BooleanField(default=True)


    @property
    def sub_total(self):
        return self.product.product_price * self.cart_item_quantity

    def __str__(self):
        return self.product
