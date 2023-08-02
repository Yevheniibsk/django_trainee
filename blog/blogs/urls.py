""" Defines URL patterns for blos."""

from django.urls import path

from .import views

app_name = 'blogs'
urlpatterns = [
    # головна сторінка    
    path('', views.index, name='index'),
    # сторінка з темами
     path('titles/', views.titles, name='titles'),
    # # сторінка присвячена окремій темі.
     path('titles/<int:title_id>/', views.title, name='title'),
    # # сторінка для додавання теми
    path('new_title/', views.new_title, name='new_title'),
    # # Сторінка для додавання нового допису
    path('new_entry/<int:title_id>/', views.new_entry, name='new_entry'),
    # # Сторінка для редагування допису.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]