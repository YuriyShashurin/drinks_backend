from django.contrib import admin

# Register your models here.
from .models import Drink

@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'rating']