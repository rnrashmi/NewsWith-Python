from django.shortcuts import render,redirect
from django.views.generic import TemplateView

# HomePage rendering view
class HomeTemplateView(TemplateView):
    template_name='home.html'

