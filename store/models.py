from django.db import models
from django.urls import reverse
from category.models import Category

# Create your models here.

GENDER_CHOICES = [
        ('men', 'Men'),
        ('women', 'Women'),
        ('kid', 'Kid'),
        ('unisex', 'Unisex'),
    ]

COUNTRY_CHOICES = [
    ('Vietnam', 'Vietnam'),
    ('China', 'China'),
    ('Indonesia', 'Indonesia'),
    ('Thailand', 'Thailand'),
    ('India', 'India'),
    ('Philippines', 'Philippines'),
    ('Pakistan', 'Pakistan'),
    ('Taiwan', 'Taiwan'),
    ('Malaysia', 'Malaysia'),
    ('Bangladesh', 'Bangladesh'),
    ('Mexico', 'Mexico'),
    ('Italy', 'Italy'),
    ('Brazil', 'Brazil'),
    ('Egypt', 'Egypt'),
    ('Turkey', 'Turkey'),
    ('South Korea', 'South Korea'),
    ('United States', 'United States'),
    ('Cambodia', 'Cambodia'),
]


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_slug = models.SlugField(max_length=200, unique=True)
    product_description = models.TextField(max_length=500, blank=True)
    product_price = models.IntegerField()
    product_images = models.ImageField(upload_to="photos/products")
    product_stock = models.IntegerField()
    product_gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='unisex')
    product_made_in = models.CharField(max_length=100, choices=COUNTRY_CHOICES, default='VN')
    product_is_availabel = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_created_date = models.DateTimeField(auto_now_add=True)
    product_modifield_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.category_slug, self.product_slug])

    def __Str__(self):
        return self.product_name
