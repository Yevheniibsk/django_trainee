from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    # додати уставні url auth (аутентифікації)
    path('', include('django.contrib.auth.urls')),
    # Сторінка реєстрації
    path ('register/', views.register, name='register'),

]