from django.contrib import admin
# Register your models here.
from . import models
from .models import JollofandChillHeroHead,SecondJollofandChillPostModel,ReviewJollofandChill


#The JollofandChill main post model admin
class JollofandChillHeroHeadPostModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'hero_slug': ('hero_title',)}
    list_display = ['hero_description','hero_img','hero_author']
admin.site.register(JollofandChillHeroHead, JollofandChillHeroHeadPostModelAdmin)


#The second_jollof_and_chill main post model admin
class SecondJollofandChillPostModelPostModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'second_jollof_and_chill_slug': ('second_jollof_and_chill_title',)}
    list_display = ['second_jollof_and_chill_description','second_jollof_and_chill_img','second_jollof_and_chill_author']
admin.site.register(SecondJollofandChillPostModel, SecondJollofandChillPostModelPostModelAdmin)


class ReviewJollofandChillPostModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'review_slug': ('review_name',)}
    list_display = ['review_description','review_img','review_author']
admin.site.register(ReviewJollofandChill, ReviewJollofandChillPostModelAdmin)