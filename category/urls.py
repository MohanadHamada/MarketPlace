from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('', CategoryListView.as_view(), name='category_list'),
]