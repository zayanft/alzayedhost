from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(home_slide)

# EQUIPMET

admin.site.register(Category)


class itemChange(admin.ModelAdmin):
    list_display = ['title','category','description','image']
    list_editable = ['category','description','image']
admin.site.register(Equipment,itemChange)

# Service
class serviceChange(admin.ModelAdmin):
    list_display = ['title','description','image']
    list_editable = ['description','image']
admin.site.register(Service,serviceChange)
