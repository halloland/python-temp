from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('api/put', views.my_form_handler)
]