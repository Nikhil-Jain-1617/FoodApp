from app.models import Menu, Restaurant
from django.contrib import admin
from .models import *


class MenuAdmin(admin.ModelAdmin):
    list_display=['restaurant_name','items','price']
admin.site.register(Menu, MenuAdmin)
admin.site.register(Restaurant)
admin.site.register(User)
#admin.site.register(Menu)
# Register your models here.

