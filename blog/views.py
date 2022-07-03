from django.views.generic import DetailView, ListView
from .models import Post
# from django.shortcuts import render


class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post