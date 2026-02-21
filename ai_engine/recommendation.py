from products.models import Product

def get_recommendations(product):

    # Get products with same category only
    recommendations = Product.objects.filter(
        category__iexact=product.category
    ).exclude(id=product.id)

    return recommendations