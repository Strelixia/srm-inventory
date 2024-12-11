
from django.contrib import admin

from .models import Delivery, Product , Order, User, Payment

admin.site.register(Delivery)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(User)
admin.site.register(Payment)