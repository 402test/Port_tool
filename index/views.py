from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
# Create your views here.



class Index_View(TemplateView):
    template_name = "index.html"
