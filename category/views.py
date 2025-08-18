from django.shortcuts import render
from django.views.generic import  DetailView
from .models import Category

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category/category_detail.html'