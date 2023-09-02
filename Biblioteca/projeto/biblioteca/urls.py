from django.urls import path
from . import views

urlpatterns = [
    path('livros/', views.livro_list),
    path('livros/<int:pk>/', views.livro_detail),
]