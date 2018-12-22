from django.contrib import admin
from products.models import Company, Category, Solution, Publication, Product

admin.site.register(Company)
admin.site.register(Category)
admin.site.register(Solution)
admin.site.register(Publication)
admin.site.register(Product)
