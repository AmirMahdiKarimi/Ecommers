
from django.contrib import admin
from .models import Product, Image, Category


class ImageAdmin(admin.TabularInline):
    model = Image
    

class ProductAdmin(admin.ModelAdmin):
    model = Product
    inlines = [ImageAdmin]


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    # list_display = ('name', 'image' )
    # exclude = ['slug']


admin.site.register(Product, ProductAdmin)
admin.site.register(Image)
admin.site.register(Category, CategoryAdmin)
