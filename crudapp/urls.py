
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path("",views.empviews,name="empviews"),
    path("insert",views.insert,name="insert"),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),


]
