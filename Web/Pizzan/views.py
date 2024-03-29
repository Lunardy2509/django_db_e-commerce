from django.shortcuts import get_object_or_404, render
from .models import *
# Create your views here.
def home(request):
    product = Product.objects.all()
    chef = Chef.objects.all()
    reviewer = Reviewer.objects.all()
    context = {'product':product,
               'chef':chef,
               'reviewer':reviewer,}
    return render(request, 'home.html', context)

def shop(request):
    product = Product.objects.all()
    context = {'product':product}
    return render(request, 'shop.html', context)

def shop_details(request, id):
    shop_details = get_object_or_404(Product, pk=id)
    product = Product.objects.filter(pk=id)
    reviewer = Reviewer.objects.filter(pk=id)
    context = {
        'shop_details': shop_details,
        'product':product,
        'reviewer':reviewer,
    }
    return render(request, 'shop-details.html', context)

def cart(request):
    product = Product.objects.all()
    context = {'product':product}
    return render(request, 'cart.html', context)

def checkout(request):
    product = Product.objects.all()
    context = {'product':product}
    return render(request, 'checkout.html', context)

def subtotal(request):
    product = Product.objects.all()
    total_price = sum(product.food_price for product in product)
    print("Total Price:", total_price)
    context = {
        'product': product, 
        'total_price': total_price
        }
    return render(request, 'cart.html', context)