from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

app_name = 'category'

urlpatterns = [
    path('<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('', CategoryListView.as_view(), name='category_list'),
    path('create/', login_required(CategoryCreateView.as_view()), name='category_create'),
]