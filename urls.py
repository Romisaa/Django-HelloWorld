from django.urls import path
from . import views


#URL Configration
urlpatterns = [
    path('hello/', views.say_hello)
]
