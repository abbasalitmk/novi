from django.urls import path
from . import views



urlpatterns = [
    path('create/', views.create_binary_tree_node, name='create'),
    path('view/', views.view_binary_tree, name='view'),
]
