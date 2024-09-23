from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category

def store(request, category_slug_path=None):
    categories = None
    products = None
    if category_slug_path != None:
        categories = get_object_or_404(Category, category_slug=category_slug_path)
        products = Product.objects.filter(category=categories, product_is_availabel=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(product_is_availabel=True)
        product_count = products.count()
    
    context = {
        'products': products,
        'product_count':product_count,
    }
    return render(request, 'store/store.html', context)

def product_detail(request, category_slug_path, product_slug_path):
    try:
        single_product = Product.objects.get(category__category_slug = category_slug_path, product_slug=product_slug_path)
    except Exception as e:
        raise e
    
    context = {
        'single_product': single_product,
    }
    return render(request, 'store/product_detail.html', context)