from home import views

#check imp
from django.urls import path, include
from django.contrib import admin 

# Describing your url patterns here:

urlpatterns = [
    path('', views.excel_data_request, name="home"),
    path('fire-safety/', views.fire_safety, name="fire-safety"),

]
