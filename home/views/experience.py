from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

# Create your views here.

class experienceView(TemplateView):
    template_name = "experience.html"

    def get(self, request, *args, **kwargs):
        context = {}
        return render(self.request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        context = {}
        return render(self.request, self.template_name, context)
