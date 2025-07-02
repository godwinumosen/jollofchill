from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse
from django.urls import reverse_lazy
from .models import JollofandChillHeroHead,SecondJollofandChillPostModel,ReviewJollofandChill
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin  


def index (request):
    return render (request, 'jollofandchill/index.html')

def base_view(request):
    return render(request, 'base.html')

#The main HomeView page
class HomeView(ListView): 
    model = JollofandChillHeroHead 
    template_name = 'jollofandchill/home.html'
    #This model is for the second deus magnus sub category of the blog
    def get_context_data(self, **kwargs):  
        context = super().get_context_data(**kwargs)   
    #the first deus magnus home video 
        context['jollofandchills'] = SecondJollofandChillPostModel.objects.all() 
        context['reviewjollofandchills'] = ReviewJollofandChill.objects.all()
        return context  

    
#Jollof and chill article details class base view
class JolloAndChillArticleDetailView(DetailView):
    model = SecondJollofandChillPostModel
    template_name = 'jollofandchill/article_detail.html'
    def JolloAndChillArticleDetailView(request, pk): 
        object = get_object_or_404(SecondJollofandChillPostModel, pk=pk)
        return render(request, 'jollofandchill/article_detail.html',{'article_detail': object})
    
    
def contact (request):
    return render (request, 'jollofandchill/contact.html')

def About (request):
    return render (request, 'jollofandchill/about_us.html')

def Order (request):
    return render (request, 'jollofandchill/order.html')
