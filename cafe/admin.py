from django.contrib import admin
from .models import Category, MenuItem, Review

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_available')
    list_filter = ('category', 'is_available')
    search_fields = ('name', 'description')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'is_approved', 'created_at')
    list_filter = ('rating', 'is_approved')
    search_fields = ('name', 'comment')
