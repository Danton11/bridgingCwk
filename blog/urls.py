from django.urls import path
from . import views
from .views import ArticleDetailView

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('article/<int:pk>',ArticleDetailView.as_view(),name='article-detail'),
]
