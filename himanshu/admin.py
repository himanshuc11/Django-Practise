from django.contrib import admin
from .models import People, Todo

# Register your models here.
admin.site.register(People)
admin.site.register(Todo)