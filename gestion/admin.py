
from django.contrib import admin

from .models import User, Product

class UserInline(admin.TabularInline):
    model = User
    extra = 3

admin.site.register(User)
