import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cafe_project.settings')
django.setup()

from cafe.models import Category, MenuItem, Review

def populate():
    # Categories
    arabic, _ = Category.objects.get_or_create(name="Arabic Dishes")
    main, _ = Category.objects.get_or_create(name="Main Course")
    snacks, _ = Category.objects.get_or_create(name="Snacks")
    beverages, _ = Category.objects.get_or_create(name="Beverages")

    # Menu Items
    MenuItem.objects.get_or_create(
        name="Spicy Shawarma",
        description="Freshly grilled chicken with traditional spices and garlic sauce.",
        price=90.00,
        category=arabic
    )
    MenuItem.objects.get_or_create(
        name="Chilli Chicken",
        description="Tangy and spicy chicken glazed with premium sauces.",
        price=160.00,
        category=main
    )
    MenuItem.objects.get_or_create(
        name="Porota & Beef Roast",
        description="The ultimate combination: flakey porota with spicy beef roast.",
        price=180.00,
        category=main
    )
    MenuItem.objects.get_or_create(
        name="Alfaham Mandi",
        description="Arabic grilled chicken served with fragrant long grain mandi rice.",
        price=220.00,
        category=arabic
    )

    # Reviews
    Review.objects.get_or_create(
        name="Rahul Das",
        comment="The beef roast here is legendary! Perfect spice level and the porota is so flaky.",
        rating=5
    )
    Review.objects.get_or_create(
        name="Anjali Menon",
        comment="Love their Alfaham Mandi. The charcoal flavor is amazing. Open till 2 AM!",
        rating=5
    )
    Review.objects.get_or_create(
        name="Suresh Babu",
        comment="Very affordable and generous portions. Highly recommended for family dinners.",
        rating=5
    )

    print("Database populated successfully!")

if __name__ == '__main__':
    populate()
