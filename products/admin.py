from django.contrib import admin
from .models import Product, Category, ProductImage

# Register your models here.
class ProductImageAdmin(admin.StackedInline):
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]

    class Meta:
       model = Product
admin.site.register(Product, ProductAdmin)

class ProductImageAdmin(admin.ModelAdmin):
    pass
admin.site.register(ProductImage, ProductImageAdmin)

admin.site.register(Category)
