# chat/urls.py
from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('variant/', views.variant, name='variant')
#     url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]

