from django.shortcuts import render
from .models import MenuItem, Review

def home(request):
    popular_dishes = MenuItem.objects.all()[:4] # Just get first 4 for home
    reviews = Review.objects.filter(is_approved=True)[:3]
    return render(request, 'home.html', {
        'popular_dishes': popular_dishes,
        'reviews': reviews
    })

def about(request):
    return render(request, 'home.html', {'scroll_to': 'about'})

def menu(request):
    menu_items = MenuItem.objects.filter(is_available=True)
    return render(request, 'menu.html', {'menu_items': menu_items})

def gallery(request):
    return render(request, 'gallery.html')

def reviews(request):
    all_reviews = Review.objects.filter(is_approved=True)
    return render(request, 'reviews.html', {'reviews': all_reviews})

def order(request):
    return render(request, 'order.html')

def contact(request):
    return render(request, 'contact.html')
