from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('second/',views.second,name='second'),




]