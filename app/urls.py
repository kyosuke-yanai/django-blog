from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(),name="index"),
    path('detail/<int:pk>/', views.BlogDetailView.as_view(),name="blog_detail"),
    path('create/', views.BlogCreateView.as_view(),name="blog_create"),
]