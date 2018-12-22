from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from . import views
from django.urls import path


app_name = 'exhibitionsummary'
urlpatterns = [
    path('', views.summary_list, name='summary_list'),
    path('conference/<int:pk>/', views.conference_detail, name='conference_detail')
]