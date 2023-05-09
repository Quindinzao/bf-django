from django.urls import path
from app_first_proj import views

urlpatterns = [
    path('home/index.html', views.home, name='home'),
    path('form/index.html', views.buy_tickets, name='form'),
    path('data/index.html', views.show_ticket, name='data'),
]
