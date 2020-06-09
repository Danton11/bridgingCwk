
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView, DetailView
from .models import Post


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'