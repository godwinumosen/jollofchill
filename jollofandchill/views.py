from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse
from django.urls import reverse_lazy
from .models import JollofandChillHeroHead,SecondJollofandChillPostModel,ReviewJollofandChill,MenuJollofandChil
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
    email='Jollofandchill17@gmail.com'
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        #message_subject = request.POST['message-subject']
        message = request.POST['message'] 
        messages.success(request, f'Your email was Successfully sent to Jollo and Chill {message_name}..!')
        return redirect('/message')
    else:
        context={
            'email':email
        } 
        return render(request, 'jollofandchill/contact.html', {})

def message (request):
    return render (request, 'jollofandchill/message.html', {})

def About (request):
    return render (request, 'jollofandchill/about_us.html')

def Order (request):
    return render (request, 'jollofandchill/order.html')

def Wallect (request):
    return render (request, 'jollofandchill/wallect.html')

def Menu (request):
    return render (request, 'jollofandchill/menu.html')

#This deus_magnus_events view
class Menu(ListView):
    model = MenuJollofandChil
    template_name = 'jollofandchill/menu.html'

#The event of deus magnus' article details class base view
class MenuArticleDetailView(DetailView):
    model = MenuJollofandChil
    template_name = 'jollofandchill/menu_article.html'
    def MenuArticleDetailView(request, pk): 
        object = get_object_or_404(MenuJollofandChil, pk=pk)
        return render(request, 'jollofandchill/menu_article.html',{'menu_detail': object})
