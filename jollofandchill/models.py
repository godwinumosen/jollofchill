from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from datetime import datetime, date

#The first main video on deusmagnus website

class JollofandChillHeroHead(models.Model):
    hero_title_head = models.CharField(max_length=255, blank=True, null=True)
    hero_title = models.CharField(max_length=255, blank=True, null=True)
    hero_description = models.TextField()
    hero_slug = models.SlugField (max_length=255,blank=True, null=True)
    hero_img = models.ImageField(upload_to='hero_images/') 
    hero_publish_date = models.DateTimeField (auto_now_add= True)
    hero_author = models.ForeignKey(User, on_delete=models.CASCADE)

       
    class Meta:
        ordering =['-hero_publish_date']
    
    def __str__(self):
        return self.hero_title_head + ' | ' + str(self.hero_author)
    
    def get_absolute_url(self):
        return reverse('home')