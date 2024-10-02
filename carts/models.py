from django.db import models
from store.models import Product, Variation
from accounts.models import Account
# Create your models here.

class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    cart_date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id
    

class CartItem(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variations = models.ManyToManyField(Variation, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    cart_item_quantity = models.IntegerField()
    cart_item_is_active = models.BooleanField(default=True)


    @property
    def sub_total(self):
        return self.product.product_price * self.cart_item_quantity

    def __unicode__(self):
        return self.product
