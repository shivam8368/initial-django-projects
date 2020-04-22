from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.MyTemplate.as_view(), name='home'),
]
