from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('load-cities/', views.load_cities, name='ajax_load_cities'),
    path('load-villages/', views.load_villages, name='ajax_load_villages'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate')
]
