from django.contrib import admin
from .models import Category, Food, CustomUser

admin.site.register(Category)
admin.site.register(Food)

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number', 'is_staff')