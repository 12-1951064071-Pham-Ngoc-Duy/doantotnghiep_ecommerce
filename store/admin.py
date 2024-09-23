from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
      list_display = ('product_name', 'product_price', 'product_stock', 'category', 'product_gender', 'product_modifield_date', 'product_is_availabel')
      prepopulated_fields = {'product_slug': ('product_name',)}

admin.site.register(Product, ProductAdmin)