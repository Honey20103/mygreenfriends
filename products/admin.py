from django.contrib import admin
from .models import Product, Category, ProductImage

# Register your models here.
class ProductImageAdmin(admin.StackedInline):
    model = ProductImage

admin.site.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]

    class Meta:
       model = Product
 
admin.site.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category)
