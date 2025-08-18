from django.shortcuts import render
from django.views.generic import  DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Category
from .forms import CategoryForm

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category/category_detail.html'
    context_object_name = 'category'

class CategoryListView(ListView):
    model = Category
    template_name = 'category/category_list.html'
    context_object_name = 'categories'

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/category_form.html'
    success_url = reverse_lazy('category:category_list')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/category_form.html'
    success_url = reverse_lazy('category:category_list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category/category_confirm_delete.html'
    success_url = reverse_lazy('category:category_list')