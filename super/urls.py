from unicodedata import name
from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('add/', views.add, name='add'),
    path('search/', views.search, name='search'),
    path('update/<str:pk>/', views.update, name='update'),
    path('delete/<str:pk>/', views.delete, name='delete'),
    path('profile/<str:pk>/', views.profile, name="profile"),
    path('addtype/', views.addtype, name="addtype"),
    path('order/', views.order, name='order'),
    path('addlaptop/', views.addlaptop, name='addlaptop'),
]