from django.contrib import admin
# Register your models here.
from . import models
from .models import DeusMagnusMainPost, SecondDeusMagnusMainPicturePost,SubPicture_2
from .models import SubPicture_1, VideoSubImage

#The DeusMagnus main post model admin
class DeusMagnusMainPostModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'deus_magnus_slug': ('deus_magnus_title',)}
    list_display = ['deus_magnus_status','deus_manus_video','deus_magnus_author']
admin.site.register(DeusMagnusMainPost, DeusMagnusMainPostModelAdmin)