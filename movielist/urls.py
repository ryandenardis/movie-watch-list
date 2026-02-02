from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movie/<int:movie_id>/', views.detail, name='detail'),
    path('movie/add/', views.add_movie, name='add_movie'),
]