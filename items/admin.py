from django.contrib import admin

# Register your models here.

from .models import Item,Post

admin.site.register(Item)
admin.site.register(Post)