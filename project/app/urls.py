from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('search-jobs/', views.search_jobs, name='search_jobs'),
]
