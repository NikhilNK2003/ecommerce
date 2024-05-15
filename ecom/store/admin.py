from django.contrib import admin

from .models import Category
from .models import Product
from .models import Customer
from .models import order

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(order)