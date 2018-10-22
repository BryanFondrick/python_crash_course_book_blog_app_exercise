"""Defines url patterns for blogs."""

from django.urls import path

from . import views

app_name = 'blogs'

urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
    
    # Show titles.
    #path('titles/', views.titles, name='titles'),
    
    #Detail page for a single blog
    #path('title/<int:title_id>/', views.title, name='title'),
    
    
    #page for adding a new blog entry
    path('new_entry/', views.new_entry, name='new_entry'),
    
    #page for editing an existing entry
    path('edit_entry/<int:title_id', views.edit_entry, name='edit_entry'),
    
]
