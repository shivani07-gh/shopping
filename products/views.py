from django.shortcuts import render
from .models import Product
from ai_engine.recommendation import get_recommendations

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    recommendations = get_recommendations(product)

    return render(request, 'products/product_detail.html', {
        'product': product,
        'recommendations': recommendations
    })


# Create your views here.
