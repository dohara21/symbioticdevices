from __future__ import unicode_literals

from django.urls import path
from . import views

app_name='calendar'
urlpatterns = [
    path('', views.EventMonthView.as_view(), name='list'),
    path('month/shift/', views.EventMonthView.as_view(), name='month_shift'),
    path('event-list/shift/', views.EventMonthView.as_view(), name='event_list_shift'),
    path('cal-and-list/shift/', views.EventMonthView.as_view(), name='cal_and_list_shift'),
    path('event/(<pk>[\w-]+)/', views.EventDetailView.as_view(), name='detail'),
    path('(<year>\d{4})/(<month>\d{2}|\d{1})/', views.EventMonthView.as_view(), name='list'),
    path('(<year>\d{4})/(<month>\d{2}|\d{1})/(<day>\d{2}|\d{1})/', views.EventDayView.as_view(), name='day_list'),
]
