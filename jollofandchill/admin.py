from django.contrib import admin
# Register your models here.
from . import models
from .models import JollofandChillHeroHead


#The DeusMagnus main post model admin
class JollofandChillHeroHeadPostModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'hero_slug': ('hero_title',)}
    list_display = ['hero_description','hero_img','hero_author']
admin.site.register(JollofandChillHeroHead, JollofandChillHeroHeadPostModelAdmin)