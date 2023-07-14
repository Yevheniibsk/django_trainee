""" Defines URL patterns for learning_logs."""

from django.urls import path

from .import views

app_name = 'learning_logs'
urlpatterns = [
    # головна сторінка    
    path('', views.index, name='index'),
    # сторінка з темами
    path('topics/', views.topics, name='topics'),
    # сторінка присвячена окремій темі.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # сторінка для додавання теми
    path('new_topic/', views.new_topic, name='new_topic'),
    # Сторінка для додавання нового допису
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    

]