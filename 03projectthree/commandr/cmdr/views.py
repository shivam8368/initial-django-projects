from django.shortcuts import render
from django.views.generic import ListView
from .models import cmdr

class MyTemplate(ListView):
    model = cmdr
    template_name = 'buttons.html'
