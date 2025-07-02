
from django.urls import path
from . import views
from .views import HomeView,JolloAndChillArticleDetailView
#from .views import SubPictureDetailView,SubVideoDetailView

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', HomeView.as_view(), name="home"),
    path('contact/', views.contact, name='contact'),
    path('home/', HomeView.as_view(), name='home'),
    path('article/<int:pk>/', JolloAndChillArticleDetailView.as_view(), name="detail"),
    #path('article2/<int:pk>/', SecondConstructionDetailViewArticleDetailView.as_view(), name="second_detail"),
]


