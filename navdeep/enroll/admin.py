from django.contrib import admin
from .models import add
# Register your models here.

class ad(admin.ModelAdmin):
    list_display = ("name","email","password")

admin.site.register(add,ad)
