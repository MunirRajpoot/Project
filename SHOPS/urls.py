from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login, name='Login'),
    path('Signup/', views.Signup, name='signup'),
    path('about/', views.About, name='About'),
    path('contact/', views.Contact, name='Contact'),
    path('trackorder/', views.TrackOrder, name='Trackorder'),
    path('addtocart/', views.Addtocart, name='addtocart'),
    path('authorization/', views.Authorization, name="Useratuhorization"),
    path('Services/', views.Services, name="services")
    path('New_lister/', views.New_lister, name="services")
]
