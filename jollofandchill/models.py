from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from datetime import datetime, date

#The first main video on jollof website

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
    
    

class SecondJollofandChillPostModel(models.Model):
    second_jollof_and_chill_title = models.CharField(max_length=255, blank=True, null=True)
    second_jollof_and_chill_description = models.TextField()
    second_jollof_and_chill_slug = models.SlugField (max_length=255,blank=True, null=True)
    second_jollof_and_chill_img = models.ImageField(upload_to='images/') 
    second_jollof_and_chill_publish_date = models.DateTimeField (auto_now_add= True)
    second_jollof_and_chill_author = models.ForeignKey(User, on_delete=models.CASCADE)

       
    class Meta:
        ordering =['-second_jollof_and_chill_publish_date']
    
    def __str__(self):
        return self.second_jollof_and_chill_title + ' | ' + str(self.second_jollof_and_chill_author)
    
    def get_absolute_url(self):
        return reverse('home')
    


class ReviewJollofandChill(models.Model):
    review_name = models.CharField(max_length=255, blank=True, null=True)
    review_profession = models.CharField(max_length=255, blank=True, null=True)
    review_description = models.TextField()
    review_slug = models.SlugField (max_length=255,blank=True, null=True)
    review_img = models.ImageField(upload_to='review_images/') 
    review_publish_date = models.DateTimeField (auto_now_add= True)
    review_author = models.ForeignKey(User, on_delete=models.CASCADE)

       
    class Meta:
        ordering =['-review_publish_date']
    
    def __str__(self):
        return self.review_name + ' | ' + str(self.review_author)
    
    def get_absolute_url(self):
        return reverse('home')
    


from django.db import models
from django.urls import reverse

class MenuJollofandChil(models.Model):
    menu_name = models.CharField(max_length=255, blank=True, null=True)
    menu_description = models.TextField()
    menu_img = models.ImageField(upload_to='menu_images/')
    
    meat_pie = models.DecimalField(max_digits=70, decimal_places=2, default=0.00)
    Fried_Plantain= models.DecimalField(max_digits=70, decimal_places=2, default=0.00)

    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering =['-created_at']

    def total_amount(self):
        return sum(
            getattr(self, f'item{i}', 0) for i in range(1, 9)
        )

    def __str__(self):
        return self.menu_name or f"FoodRecord #{self.id} on {self.created_at.date()}"

    def get_absolute_url(self):
        return reverse('home')
