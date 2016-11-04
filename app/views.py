from django.shortcuts import render
from app.models import Child, Profile
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView


class ChildCreateView(CreateView):
    model = Child
    fields = ('name', 'parent', 'age', 'pin')
    success_url = '/'


class IndexView(TemplateView):
    template_name = "index.html"
