
from django.urls import path
from . import views
from .views import HomeView,JolloAndChillArticleDetailView,Menu
#from .views import SubPictureDetailView,SubVideoDetailView

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', HomeView.as_view(), name="home"),
    path('contact/', views.contact, name='contact'),
    path('home/', HomeView.as_view(), name='home'),
    path('article/<int:pk>/', JolloAndChillArticleDetailView.as_view(), name="detail"),
    path('order/', views.Order, name='order'),
    path('wallect/', views.Wallect, name='wallect'),
    path('about/', views.About, name='about'),
    path('message/', views.message, name='message'),
    #path('menu/', views.Menu, name='menu'),
    path('menu/', Menu.as_view(), name='menu'),
    #path('article2/<int:pk>/', MenuArticleDetailView.as_view(), name="menu_detail"),
    
]


