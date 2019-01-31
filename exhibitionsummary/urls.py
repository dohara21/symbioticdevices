from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from . import views
from django.urls import path


app_name = 'exhibitionsummary'
urlpatterns = [
    path('', views.index, name='index'),
    path('conference', views.conference, name='conference'),
    path('conference/<int:pk>/', views.conference_detail, name='conference_detail'),
    path('products', views.products, name='products'),
    path('publications', views.publications, name='publications'),
]
