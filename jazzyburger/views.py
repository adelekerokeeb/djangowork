from typing import Any, Dict
from django.shortcuts import render
from .models import Product
from django.views.generic import TemplateView, DetailView

# Create your views here.
# creating class based view cbv
class ProductView(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context
    

class ProductDetailView(DetailView):
    template_name = "detail.html"
    model = Product
