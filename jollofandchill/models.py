from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from datetime import datetime, date

#The first main video on deusmagnus website

# The main model for Deus Magnus Model category
class DeusMagnusMainPost(models.Model):
    deus_magnus_title = models.CharField(max_length=255, blank=True, null=True)
    deus_magnus_status = models.CharField(max_length=255, blank=True, null=True)
    deus_magnus_description = models.TextField()
    deus_magnus_slug = models.SlugField (max_length=255,blank=True, null=True)
    deus_manus_video = models.FileField(upload_to='videos/') 
    #thumbnail = models.ImageField(max_length=100, null=True, blank=True)
    deus_magnus_publish_date = models.DateTimeField (auto_now_add= True)
    deus_magnus_author = models.ForeignKey(User, on_delete=models.CASCADE)

       
    class Meta:
        ordering =['-deus_magnus_publish_date']
    
    def __str__(self):
        return self.deus_magnus_title + ' | ' + str(self.deus_magnus_author)
    
    def get_absolute_url(self):
        return reverse('home','sub_video_img_detail','sub_detail_video','sub_detail',
                       'board_detail','blog_detail','last_detail','second_detail','detail')
    