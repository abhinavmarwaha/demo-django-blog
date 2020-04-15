from django.shortcuts import render
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter
